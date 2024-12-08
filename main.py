import json
from coreQuery import BitcoinRPC

def parse_blockchain_info(blockchain_json):
    # Parse the JSON
    try:
        blockchain_info = json.loads(blockchain_json)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    
    # Extract the required information
    return {
        'chain': blockchain_info['chain'],
        'blocks': blockchain_info['blocks'],
        'bestblockhash': blockchain_info['bestblockhash']
    }

def main():
    rpc = BitcoinRPC()
    blockchain_info_json = rpc.get_blockchain_info()
    if "Exception" in blockchain_info_json:
        raise ValueError(blockchain_info_json)
    
    parsed_info = parse_blockchain_info(blockchain_info_json)
    
    print("Parsed Blockchain Information:")
    print(f"- Chain: {parsed_info['chain']}")
    print(f"- Blocks: {parsed_info['blocks']}")
    print(f"- Best Block Hash: {parsed_info['bestblockhash']}")

if __name__ == "__main__":
    main()