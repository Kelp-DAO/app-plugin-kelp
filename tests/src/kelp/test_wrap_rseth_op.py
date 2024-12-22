from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0x87eEE96D50Fb761AD85B1c982d28A042169d61b1"
)

# Test from replayed transaction: https://optimistic.etherscan.io/tx/0x0eb30eb13059602f22d05c82ff9bda35136e5ce522d0469c76cbe5d80fd85e1b

def test_wrap_rseth_op(backend, firmware, navigator, test_name, wallet_addr):
    data = "0x47e7ef240000000000000000000000004186bfc76e2e237523cbc30fd220fe055156b41f00000000000000000000000000000000000000000000000000005af3107a4000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

