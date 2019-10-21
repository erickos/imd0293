import hashlib
import json
from time import time
import copy
import random

from bitcoin.wallet import CBitcoinSecret
from bitcoin.signmessage import BitcoinMessage, VerifyMessage, SignMessage

DIFFICULTY = 4 # Quantidade de zeros (em hex) iniciais no hash válido.

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.nodes = set() # Conjunto para armazenar os nós registrados.
        self.createGenesisBlock()

    def createGenesisBlock(self):
        self.createBlock(previousHash='0'*64, nonce=0)
        self.mineProofOfWork(self.prevBlock) 

    def createBlock(self, nonce=0, previousHash=None):
        if (previousHash == None):
            previousBlock = self.chain[-1]
            previousBlockCopy = copy.copy(previousBlock)
            previousBlockCopy.pop("transactions", None)

        block = {
            'index': len(self.chain) + 1,
            'timestamp': int(time()),
            'transactions': self.memPool,
            'merkleRoot': self.generateMerkleRoot(self.memPool),
            'nonce': nonce,
            'previousHash': previousHash or self.generateHash(previousBlockCopy),
        }

        self.memPool = []
        self.chain.append(block)
        return block

    def mineProofOfWork(self, prevBlock):
        nonce = 0
        while self.isValidProof(prevBlock, nonce) is False:
            nonce += 1

        return nonce

    def createTransaction(self, sender, recipient, amount, timestamp, privKey):
        tx = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'timestamp': timestamp
        }
 
        tx['signature'] = Blockchain.sign(privKey, json.dumps(tx, sort_keys=True)).decode('utf-8')
        self.memPool.append(tx)

        return self.prevBlock['index'] + 1

    def isValidChain(self, chain):
        # Dados uma chain passada como parâmetro, faz toda a verificação se o blockchain é válido
        # 1. PoW válido
        # 2. Transações assinadas e válidas
        # 3. Merkle Root válido

        for index, block in enumerate(chain):
            
            # verify the previous hash in genesis block
            if index == 0 and block['previousHash'] != ('0'*64):
                return False 
            
            # Is not valid PoW
            if not Blockchain.isValidProof(block, block['nonce']):
                return False

            # The previous hash reference is not valid
            if index > 0:
                if block['previousHash'] != Blockchain.getBlockID(chain[index-1]):
                    return False

            # Valid Merkle Root
            if block['merkleRoot'] != Blockchain.generateMerkleRoot(block['transactions']):
                return False

            # Invalid TXs
            for tx in block["transactions"]:
                if (
                    not tx["sender"]
                    or not tx["recipient"]
                    or tx["timestamp"] > int(time())
                    or tx["amount"] <= 0
                    or not tx["signature"]
                ):
                    return False
                
                # if is not signed
                txCopy = copy.copy(tx)
                txCopy.pop('signature', None)
                if ( not Blockchain.verifySignature(tx["sender"], tx['signature'], json.dumps(txCopy, sort_keys=True))):
                    return False

        return True

    def resolveConflicts(self):
        # Consulta todos os nós registrados, e verifica se algum outro nó tem um blockchain com mais PoW e válido. Em caso positivo,
        # substitui seu próprio chain.
        pass

    @staticmethod
    def generateMerkleRoot(transactions):
        if (len(transactions) == 0): # Para o bloco genesis
            return '0'*64

        txHashes = [] 
        for tx in transactions:
            txHashes.append(Blockchain.generateHash(str(tx)))

        return Blockchain.hashTxHashes(txHashes)

    @staticmethod
    def hashTxHashes(txHashes):
        if (len(txHashes) == 1): # Condição de parada.
            return txHashes[0]

        if (len(txHashes)%2 != 0): # Confere se a quantidade de hashes é par.
            txHashes.append(txHashes[-1]) # Se não for, duplica o último hash.

        newTxHashes = []
        for i in range(0,len(txHashes),2):        
            newTxHashes.append( hashlib.sha256( (txHashes[i] + txHashes[i+1]).encode() ).hexdigest() )
        
        return Blockchain.hashTxHashes(newTxHashes)

    @staticmethod
    def isValidProof(block, nonce):
        block['nonce'] = nonce
        guessHash = Blockchain.getBlockID(block)
        return guessHash[:DIFFICULTY] == '0' * DIFFICULTY 

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    @staticmethod
    def getBlockID(block):
        blockCopy = copy.copy(block)
        blockCopy.pop("transactions", None)
        return Blockchain.generateHash(blockCopy)

    def printChain(self):
        for block in reversed(self.chain):
            generated_hash = Blockchain.getBlockID(block)
            print(hex(int(generated_hash, 16)))
            print('\t\t\t\t\tA')
            print('\t\t\t\t\t|\n')
            print(' =================================== %s° BLOCK ==================================' % block['index'])
            print('| Self Hash: ', generated_hash)
            print('| Timestamp: ', block['timestamp'])
            print('| Nonce: ', block['nonce'])
            print('| merkleRoot: ', block['merkleRoot'])
            print('| previousHash: ', block['previousHash'])
            print('| transactions: ', block['transactions'])
            print(' ================================================================================')

    @property
    def prevBlock(self):
        return self.chain[-1]

    @staticmethod
    def sign(privKey, message):
        secret = CBitcoinSecret(privKey)
        msg = BitcoinMessage(message)
        return SignMessage(secret, msg)
        
    @staticmethod
    def verifySignature(address, signature, message):
        msg = BitcoinMessage(message)
        return VerifyMessage(address, msg, signature)

# Implemente sua API com os end-points indicados no GitHub.
# https://github.com/danilocurvelo/imd0293/tree/master/06-api
# Implemente um teste com ao menos 2 nós simultaneos.

blockchain = Blockchain()

sender = '19sXoSbfcQD9K66f5hwP5vLwsaRyKLPgXF'
recipient = '1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N'

for x in range(0, 4): 
    for y in range(0, random.randint(1,4)) : 
        timestamp = int(time())
        amount = random.uniform(0.00000001, 100)
        blockchain.createTransaction(sender, recipient, amount, timestamp, 'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U')
    blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)

blockchain.printChain()

print( blockchain.isValidChain(blockchain.chain) )

# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/transactions/create', methods=['POST'])
# def transactions_create():
#     sender = request.args['sender']
#     recipient = request.args['recipient']