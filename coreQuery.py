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

# RPC connection details
rpc_user = os.getenv("rpcUser")
rpc_password = os.getenv("rpcPassword")
rpc_host = os.getenv("rpcAddress")
rpc_port = os.getenv("rpcPort")
rpc_connection = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
print("RPC connection string created")

try:
    rpc_client = AuthServiceProxy(rpc_connection, timeout=120)
    print("RPC client initialized")

    # Get blockchain info
    blockchain_info = rpc_client.getblockchaininfo()
    print("Blockchain Info:")
    print(json.dumps(blockchain_info, indent=4, cls=DecimalEncoder))

    # Get network info
    network_info = rpc_client.getnetworkinfo()
    print("\nNetwork Info:")
    print(json.dumps(network_info, indent=4, cls=DecimalEncoder))

except JSONRPCException as json_exception:
    print(f"A JSON RPC Exception occurred: {json_exception}")
except Exception as general_exception:
    print(f"An error occurred: {general_exception}")

print("Script execution completed.")