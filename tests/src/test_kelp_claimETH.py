from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x62De59c08eB5dAE4b7E6F7a8cAd3006d6965ec16"
)

# Test from replayed transaction: https://etherscan.io/tx/0xa5458f18af5bd00d7bda4332f33af93e0f7cd7294c6715dbf5a4c143f0a1d6e3

def test_kelp_claimETH(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x6dbaf9ee000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

