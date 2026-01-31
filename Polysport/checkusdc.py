from web3 import Web3

# Connect to Polygon
w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))

# USDC.e contract
usdc_address = Web3.to_checksum_address('0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174')
wallet = Web3.to_checksum_address('0xd8ce113d419bc5307714a77c5e52fa881c32504a')

# ABI for balanceOf
abi = [{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]

contract = w3.eth.contract(address=usdc_address, abi=abi)
balance = contract.functions.balanceOf(wallet).call()
print(f"Balance: {balance / 10**6} USDC.e")