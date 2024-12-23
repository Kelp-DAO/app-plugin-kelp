from web3 import Web3
from tests.utils import run_test, load_contract

contract = load_contract(
    "0xB185D98056419029daE7120EcBeFa0DbC12c283A"
)

# Test from replayed transaction: https://etherscan.io/tx/0x9d4e7c166d2bf8f21afe6cde11a9b1c8dd3b02e0bf5b594bc89393f990bef038

def test_growth_vault_withdraw(backend, firmware, navigator, test_name, wallet_addr):
    data = "0xe088747b000000000000000000000000c824a08db624942c5e5f330d56530cd1598859fd000000000000000000000000000000000000000000000001c9990c9974dd8000000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000086b656c705f64616f000000000000000000000000000000000000000000000000"
    run_test(
        contract, 
        data, 
        backend, 
        firmware, 
        navigator, 
        test_name, 
        wallet_addr
    )

