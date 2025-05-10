# 🔐 EVM Wallet Creator

This is a simple Python tool to generate multiple EVM-compatible wallets (Ethereum, BSC, Polygon, etc.) with support for:

- ✅ Automatic generation of addresses, private keys, and mnemonic phrases
- ✅ Clean separation of each component into separate files
- ✅ Full consolidated output in a single CSV-style file

## 📦 Features

- Generate **unlimited** wallets quickly
- Saves output in 4 clear formats:
| File Name          | Description                                  |
| ------------------ | -------------------------------------------- |
| `addresses.txt`    | EVM wallet addresses                         |
| `private_keys.txt` | Private keys (hex format)                    |
| `mnemonics.txt`    | 12-word mnemonic phrases                     |
| `wallets_full.txt` | All 3 in CSV: `address,private_key,mnemonic` |

- Uses secure BIP39 mnemonics and `eth-account` for HD wallet support

<br>

# 🛠 STEPS

### Install Python:

      sudo apt install python3 python3-pip -y

### Create a virtual environment named 'venv' & Active 

    python3 -m venv venv
    source venv/bin/activate

### Once activated, you can install the required packages:
   
    pip install eth-account mnemonic

### Clone this repository:

    https://github.com/adityapatil343/EVM-Wallet-Creator
    cd EVM-Wallet-Creator

### Run the wallet creator:

    python3 EVMCREATE.py

### Done!
