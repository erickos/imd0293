import hashlib
import json
from time import time
import copy

DIFFICULTY = 5 # Quantidade de zeros (em hex) iniciais no hash válido.

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock() 
    
    ## Semana 2
    def createGenesisBlock(self):
        self.createBlock(previousHash='0'*64, nonce=0)
        self.mineProofOfWork(self.prevBlock)

    def createBlock(self, nonce=0, previousHash=None): 
        previous_hash = '0'*64 #hash para o atributo previousHash do bloco genesis
        
        ## calculo de hash dois a dois
        if (previousHash == None):
            previousBlock = self.chain[-1]
            previousBlockCopy = copy.copy(previousBlock)
            previousBlockCopy.pop("transactions", None)

        block = {
            'index': len(self.chain)+1,
            'timestamp': int(time()), #truncando o timestamp
            'nonce': nonce,
            'merkleRoot': '0'*64,
            'previousHash': previousHash or self.generateHash(previousBlockCopy),
            'transactions': self.memPool
        }
        self.memPool = []
        self.chain.append(block)
        return block
    ## Fim Semana 2

    ## Semana 1
    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    def printChain(self):
        for x in self.chain:
            print(json.dumps(x, sort_keys=True).encode())
    ## Fim Semana 1

    ## Semana 3
    def mineProofOfWork(self, prevBlock):
        auxNonce = 0
        while (not Blockchain.isValidProof(prevBlock, auxNonce)):
            auxNonce+=1

    @staticmethod
    def isValidProof(block, nonce):
        block["nonce"] = nonce
        return Blockchain.getBlockID(block)[:DIFFICULTY] == '0'*DIFFICULTY

    @staticmethod
    def getBlockID(block):
        copia = copy.deepcopy(block)
        copia.pop('transactions')
        return Blockchain.generateHash(copia)

    @property
    def prevBlock(self):
        return self.chain[-1]
    ## Fim Semana 4

#print('>>>>>>>>>> Teste 2')
# Teste 1
#blockchain = Blockchain()
#for x in range(0, 3): blockchain.createBlock()
#blockchain.printChain()
# Fim Teste 1
#print('>>>>>>>>>> Fim do Teste 2')

print('>>>>>>>>>> Teste 3')
# Teste 3
blockchain = Blockchain()
for x in range(0, 4): 
    blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)

for x in blockchain.chain :
    print('[Bloco #{} : {}] Nonce: {} | É válido? {}'.format(x['index'], Blockchain.getBlockID(x), x['nonce'], Blockchain.isValidProof(x, x['nonce'])))
# Fim Teste 3
print('>>>>>>>>>>> Fim do Teste 3')