import hashlib
import json
import time

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock() 

    def createGenesisBlock(self):
        self.createBlock()

    def createBlock(self, nonce=0, previousHash=None): 
        previous_hash = '0'*64
        ## calculo de hash dois a dois
        if( len(self.chain) > 0 ):
           previousBlock = dict(self.chain[-1])
           previousBlock.pop('transactions')
           previous_hash = self.generateHash( previousBlock )

        block = {
            'index': len(self.chain),
            'timestamp': str(int(time.time())),
            'nonce': nonce,
            'merkleRoot': '0'*64,
            'previousHash': previous_hash,
            'transactions': self.memPool
        }
        self.chain.append(block)

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    def printChain(self):
        for x in reversed(self.chain):
            print( json.dumps(x, sort_keys=True).encode())
            ## imprimindo hash do proprio bloco para comparar
           

# Teste
blockchain = Blockchain()
for x in range(0, 3): blockchain.createBlock()
blockchain.printChain()

