# Interact with your Umbrel Bitcoin Node via RPC and REST
This guide will help you interact with your Umbrel Bitcoin Node via RPC and REST. This will allow you to query your node for information and perform actions on the blockchain. This guide will also help you setup a python environment to run the scripts provided. The scripts provided will allow you to query your node for information and perform actions on the blockchain.

# Setup
1. **Enable RPC and REST in your Umbrel Bitcoin Node**
   - Login to your Umbrel Node
   - Navigate to the Bitcoin Node
   - Click on the "Advanced Settings" tab
   - Under "RPC and REST" toggle "Public REST API"
   - Click "Save and Restart Bitcoin Node"
2. **Get your RPC credentials**
   - Navigate to the Bitcoin Node
   - Click "Connect"
   - Find the "RPC (Local Network)" credentials (you'll need them in the next step)
3. **Prepare your local environment**
   - Fork/Clone this repository
   - Install requirements (`pip install -r requirements.txt`)
   - Copy the `example.env` file to `.env` and fill in the necessary fields
4. **Test the connection**
   - Run the script (`python main.py`)
   - If you see the current block height, you're all set!
