from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x62De59c08eB5dAE4b7E6F7a8cAd3006d6965ec16"
)

# Test from replayed transaction: https://etherscan.io/tx/0x31a88ec3977a4cd4ab0a105607a9ac1d350e1f2a2148345f6bdf9b583a74518b

def test_kelp_claimLST(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x6dbaf9ee000000000000000000000000ac3e018457b222d93114458476f3e3416abbe38f"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

