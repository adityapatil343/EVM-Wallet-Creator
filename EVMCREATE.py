from eth_account import Account
from mnemonic import Mnemonic

# Enable HD wallet features
Account.enable_unaudited_hdwallet_features()

# Ask user
count = int(input("How many wallets do you want to create? "))

# Files
private_keys_file = "private_keys.txt"
mnemonics_file = "mnemonics.txt"
addresses_file = "addresses.txt"
full_output_file = "wallets_full.txt"

# Clear files
for file in [private_keys_file, mnemonics_file, addresses_file, full_output_file]:
    open(file, 'w').close()

# Init mnemonic generator
mnemo = Mnemonic("english")

# Generate wallets
for i in range(count):
    mnemonic = mnemo.generate(strength=128)
    acct = Account.from_mnemonic(mnemonic)
    private_key = acct.key.hex()
    address = acct.address

    # Write individual files
    with open(private_keys_file, "a") as f:
        f.write(f"{private_key}\n")
    with open(mnemonics_file, "a") as f:
        f.write(f"{mnemonic}\n")
    with open(addresses_file, "a") as f:
        f.write(f"{address}\n")
    with open(full_output_file, "a") as f:
        f.write(f"{address},{private_key},{mnemonic}\n")

    print(f"[{i+1}] Wallet created: {address}")

# Done
print(f"\n✅ {count} wallets created.")
print("Files:")
print(f"- {addresses_file}")
print(f"- {private_keys_file}")
print(f"- {mnemonics_file}")
print(f"- {full_output_file}")
