import time
import uuid

from backend.wallet.wallet import Wallet
from backend.config import MINING_REWARD, MINING_REWARD_INPUT

class Transaction:
    """
    Document of an exchange in currency from a sender to one or more recipients.
    """
    def __init__(self, sender_wallet, recipient, amount):
        self.id = str(uuid.uuid4())[0:8]
        self.output = self.create_output(
            sender_wallet,
            recipient,
            amount
        )
        self.input = self.create_input(
            sender_wallet,
            self.output
        )


    def create_output(self, sender_wallet, recipient, amount):
        """
        Structures the output data for a transaction.
        :param sender_wallet:
        :param recipient:
        :param amount:
        :return:
        """
        if amount > sender_wallet.balance:
            raise Exception('Amount exceeds balance')

        output = {}
        output[recipient] = amount
        output[sender_wallet.address] = sender_wallet.balance - amount

        return output

    def create_input(self, sender_wallet, output):
        """
        Structures the input data for a transaction.
        Signs the transaction and includes the sender's public key and address.
        :param sender_wallet:
        :param output:
        :return:
        """
        return {
            'timestamp': time.time_ns(),
            'amount': sender_wallet.balance,
            'address': sender_wallet.address,
            'public_key': sender_wallet.public_key,
            'signature': sender_wallet.sign(output)
        }

    def update(self, sender_wallet, recipient, amount):
        """
        Updates the transaction with an existing or new recipient.
        :param sender_wallet:
        :param recipient:
        :param amount:
        :return:
        """
        if amount > self.output[sender_wallet.address]:
            raise Exception('Amount exceeds balance')

        if recipient in self.output:
            self.output[recipient] += amount
        else:
            self.output[recipient] = amount

        self.output[sender_wallet.address] = self.output[sender_wallet.address] - amount
        self.input = self.create_input(sender_wallet, self.output)

def main():
    transaction = Transaction(Wallet(), 'recipient', 10)
    print(f'transaction.__dict__: {transaction.__dict__}')

if __name__ == '__main__':
    main()
