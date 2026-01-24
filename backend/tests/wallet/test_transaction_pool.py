from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.transaction import Transaction
from backend.wallet.wallet import Wallet

def test_transaction_pool():
    transaction_pool = TransactionPool()
    transaction = Transaction(Wallet(), 'recipient', 50)
    transaction_pool.set_transaction(transaction)

    assert transaction_pool.transaction_map[transaction.id] == transaction
