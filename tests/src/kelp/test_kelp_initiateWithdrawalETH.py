from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x62De59c08eB5dAE4b7E6F7a8cAd3006d6965ec16"
)

# Test from replayed transaction: https://etherscan.io/tx/0x5a6a235be8865c5989bd5f604e9f4c14c442e5db0ee06b64e93a74ead5b5b14c

def test_kelp_initiateWithdrawalETH(backend, firmware, navigator, test_name, wallet_addr):
    data = "0xc8393ba9000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000000000000000000000000000015f021397cf0000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

