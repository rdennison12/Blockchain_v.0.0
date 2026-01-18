from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain: is a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions.
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def replace_chain(self, chain):
        """
        Replaces the local chain with the incoming one if the following applies:
            - The incoming chain is longer than the local chain.
            - The incoming chain is formatted properly.
        :param chain:
        :return:
        """
        if len(chain) <= len(self.chain):
            raise Exception('Cannot replace. The incoming chain must be longer.')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot replace. The incoming chain is invalid: {e}')

        self.chain = chain

    def to_json(self):
        """
        Serialize th blockchain into a list of blocks.
        :return:
        """
        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def is_valid_chain(chain):
        """
        Validates the incoming chain.
        Enforce the following conditions:
            - The chain must start with the genesis block
            - Blocks must be formatted correctly.
        :param chain:
        :return:
        """
        if chain[0] != Block.genesis():
            raise Exception('The blockchain must start with the genesis block')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)

def main():
    blockchain = Blockchain()
    blockchain.add_block("One")
    blockchain.add_block("Two")

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')


if __name__ == "__main__":
    main()
