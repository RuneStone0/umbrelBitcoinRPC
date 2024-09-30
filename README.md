## Start with enabling RPC and REST [here](https://github.com/Juniorduc44/umbrelBitcoinRPC/blob/main/umbrelBitcoinRPC.md)
### If you have already enabled RPC and REST in Bitcoin Node "Advanced Settings" you can skip this step.
</br>
</br>

## Next you can get your python environment setup [here](https://github.com/Juniorduc44/umbrelBitcoinRPC/blob/main/loadPythonEnv.md)
### If you have an environment prestaged and active just load the requirements.txt file
- (Linux) `pip3 install -r requirements.txt`
- (Windows) `pip install -r requirements.txt`

#### Change the example.env
- from "example.env" to ".env"

## Next you will need to ssh into umbrel and change one [file]()
- ssh login syntax
 - `ssh umbrel@192.168.x.x`    
- navigate to data folder
 - `cd /data/`
- copy and paste bitcoin.conf examples into the file with a text editor of choice
 - `sudo nano bitcoin.conf`
### reference your .env file to make sure user and pass match for logging in

## Lastly Run the program
- Make sure you have [loaded](https://github.com/Juniorduc44/umbrelBitcoinRPC/blob/main/loadPythonEnv.md) your python environment and its now active
- Type the following into the remote device which should be on the same local network
  - (Linux) `python3 main.py`
  - (Windows) `python main.py`