from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x62De59c08eB5dAE4b7E6F7a8cAd3006d6965ec16"
)

# Test from replayed transaction: https://etherscan.io/tx/0xa44d01da432225b7ad2cc49b0160d57464439107044af3497a9b71d7677c82c7

def test_kelp_initiateWithdrawalLST(backend, firmware, navigator, test_name, wallet_addr):
    data = "0xc8393ba9000000000000000000000000a35b1b31ce002fbf2058d22f30f95d405200a15b0000000000000000000000000000000000000000000000000f99f5f1987e8000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

