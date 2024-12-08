import requests
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from dotenv import load_dotenv
import os
import json
from decimal import Decimal

load_dotenv()

# Custom JSON encoder to handle Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

class BitcoinRPC:
    def __init__(self):
        self.rpc_user = os.getenv("rpcUser")
        self.rpc_password = os.getenv("rpcPassword")
        self.rpc_host = os.getenv("rpcAddress")
        self.rpc_port = os.getenv("rpcPort")

        if not all([self.rpc_user, self.rpc_password, self.rpc_host, self.rpc_port]):
            raise ValueError("One or more RPC connection environment variables are not set")

        self.rpc_connection = f"http://{self.rpc_user}:{self.rpc_password}@{self.rpc_host}:{self.rpc_port}"
        self.rpc_client = AuthServiceProxy(self.rpc_connection, timeout=120)

    def get_blockchain_info(self):
        try:
            blockchain_info = self.rpc_client.getblockchaininfo()
            return json.dumps(blockchain_info, indent=4, cls=DecimalEncoder)
        except JSONRPCException as json_exception:
            return f"A JSON RPC Exception occurred: {json_exception}"
        except Exception as general_exception:
            return f"An error occurred: {general_exception}"

    def get_network_info(self):
        try:
            network_info = self.rpc_client.getnetworkinfo()
            return json.dumps(network_info, indent=4, cls=DecimalEncoder)
        except JSONRPCException as json_exception:
            return f"A JSON RPC Exception occurred: {json_exception}"
        except Exception as general_exception:
            return f"An error occurred: {general_exception}"