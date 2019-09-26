import hashlib
import json
from time import time
import copy
import random

from collections import OrderedDict

from bitcoin.wallet import CBitcoinSecret
from bitcoin.signmessage import BitcoinMessage, VerifyMessage, SignMessage

DIFFICULTY = 4 # Quantidade de zeros (em hex) iniciais no hash válido.

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
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
        new_transaction = {
        	"sender": sender,
        	"recipient": recipient,
        	"amount": amount,
        	"timestamp": timestamp
        }

        signature = self.sign(privKey, json.dumps(new_transaction, sort_keys=True))
        
        new_transaction['signature'] = signature
        self.memPool.append(new_transaction)

    @staticmethod
    def generateMerkleRoot(transactions):
        listoftransaction = copy.copy(transactions)
        past_transaction = OrderedDict()
        temp_transaction = []

        # 3.1 Loop until the list finishes
        for index in range(0,len(listoftransaction),2):

# 3.2 Get the most left element 
            current = listoftransaction[index]

# 3.3 If there is still index left get the right of the left most element
            if index+1 != len(listoftransaction):
                current_right = listoftransaction[index+1]

# 3.4 If we reached the limit of the list then make a empty string
            else:
                current_right = ''

# 3.5 Apply the Hash 256 function to the current values
            current_hash = hashlib.sha256(current)

# 3.6 If the current right hash is not a '' <- empty string
            if current_right != '':
                current_right_hash = hashlib.sha256(current_right)

# 3.7 Add the Transaction to the dictionary 
            past_transaction[listoftransaction[index]] = current_hash.hexdigest()

# 3.8 If the next right is not empty
            if current_right != '':
                past_transaction[listoftransaction[index+1]] = current_right_hash.hexdigest()

# 3.9 Create the new list of transaction
            if current_right != '':
                temp_transaction.append(current_hash.hexdigest() + current_right_hash.hexdigest())

# 3.01 If the left most is an empty string then only add the current value
            else:
                temp_transaction.append(current_hash.hexdigest())

# 3.02 Update the variables and rerun the function again 
            if len(listoftransaction) != 1:
                self.listoftransaction = temp_transaction
                self.past_transaction = past_transaction

# 3.03 Call the function repeatly again and again until we get the root 
                self.generateMerkleRoot(listoftransaction)
        return listoftransaction[0]

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


# Teste
blockchain = Blockchain()

sender = '19sXoSbfcQD9K66f5hwP5vLwsaRyKLPgXF'
recipient = '1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N'

# Cria 5 blocos, incluindo o Genesis, contendo de 1-4 transações cada, com valores aleatórios, entre os endereços indicados em sender e recipient.
for x in range(0, 4): 
    for y in range(0, random.randint(1,4)) : 
        timestamp = int(time())
        amount = random.uniform(0.00000001, 100)
        blockchain.createTransaction(sender, recipient, amount, timestamp, 'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U')
    blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)

blockchain.printChain()
