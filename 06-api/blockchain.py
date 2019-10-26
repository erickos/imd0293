import hashlib
import json
from time import time
import copy
import random

from flask import Flask, request
import requests

from bitcoin.wallet import CBitcoinSecret
from bitcoin.signmessage import BitcoinMessage, VerifyMessage, SignMessage

DIFFICULTY = 4 # Quantidade de zeros (em hex) iniciais no hash valido.

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.nodes = set() # Conjunto para armazenar os nos registrados.
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

        return tx  #self.prevBlock['index'] + 1

    def isValidChain(self, chain):
        # Dados uma chain passada como parametro, faz toda a verificacao se o blockchain e valido
        # 1. PoW valido
        # 2. Transacoes assinadas e validas
        # 3. Merkle Root valido

        for block in chain:
            
            # verify the previous hash in genesis block
            if block['index'] == 1 and block['previousHash'] != ('0'*64):
                print( 'genesis prev hash' )
                return False 
            
            # Is not valid PoW
            if not Blockchain.isValidProof(block, block['nonce']):
                print( 'valid proof' )
                return False

            aux = Blockchain.getBlockID( chain[ block['index'] -2 ] )
            # The previous hash reference is not valid
            if block['index'] > 1:
                if block['previousHash'] != Blockchain.getBlockID( chain[ block['index'] -2 ] ):
                    print( 'block prev hash ')
                    print( type(block['previousHash']) )
                    print( block['previousHash'] )
                    print( type(aux) )
                    print(aux)
                    return False

            # Valid Merkle Root
            if block['merkleRoot'] != Blockchain.generateMerkleRoot(block['transactions']):
                print( 'merkle root' )
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
                    print( 'tx error' )
                    return False
                
                # if the tx is not signed and if is valid
                txCopy = copy.copy(tx)
                txCopy.pop('signature', None)
                if ( not Blockchain.verifySignature(tx["sender"], tx['signature'], json.dumps(txCopy, sort_keys=True))):
                    print( 'signature error' )
                    return False

        return True

    def resolveConflicts(self):
        
        # set of the registered nodes
        neighbours = self.nodes
        # future new valid chain
        newChain = None

        # future new valid mempool
        # newMempool = None

        # length of the current chain
        currentChainLength = len(self.chain)
        
        # request every registered node chain
        for node in neighbours:
            responseChain = requests.get(f'http://{node}/chain')
            print( 'getting chain from ' + node )
            currentNodeChain = responseChain.json()['chain']
            currentNodeLength = len(currentNodeChain)

            print( currentChainLength )
            print( currentNodeLength  )
            
            if currentNodeLength > currentChainLength and self.isValidChain(currentNodeChain):
                currentChainLength = currentNodeLength
                newChain = currentNodeChain

        if newChain:    
            self.chain = newChain 
            return True
        print('resolveConfl')
        return False

    @staticmethod
    def generateMerkleRoot(transactions):
        if (len(transactions) == 0): # Para o bloco genesis
            return '0'*64

        txHashes = [] 
        for tx in transactions:
            txHashes.append(Blockchain.generateHash(tx))

        return Blockchain.hashTxHashes(txHashes)

    @staticmethod
    def hashTxHashes(txHashes):
        if (len(txHashes) == 1): # Condicao de parada.
            return txHashes[0]

        if (len(txHashes)%2 != 0): # Confere se a quantidade de hashes e par.
            txHashes.append(txHashes[-1]) # Se nao for, duplica o ultimo hash.

        newTxHashes = []
        for i in range(0,len(txHashes),2):       
            newTxHashes.append( Blockchain.generateHash( txHashes[i] + txHashes[i+1] ) )
        
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
privKey = 'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U'

##################################################################################################################################

app = Flask(__name__) 

@app.route('/transactions/create', methods=['POST'])
def transactions_create():
    sender = request.args['sender']
    recipient = request.args['recipient']
    amount = float(request.args['amount'])
    timestamp = int(time())

    if not blockchain.createTransaction(sender, recipient, amount, timestamp, privKey):
        return 'Status code 500. Error TX not created'
    return 'Status code 200. TX created'

@app.route('/transactions/mempool', methods=['GET'])
def get_mempool():
    return { 'mempool' : blockchain.memPool }

@app.route('/mine', methods=['GET'])
def mine():
    if not blockchain.createBlock():
        return 'Status code 500. Block not created'
    blockchain.mineProofOfWork(blockchain.prevBlock)
    return 'Status code 200. Block created'

@app.route('/chain', methods=['GET'])
def get_chain():
    return { 'chain': blockchain.chain }

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    nodes = request.args['nodes'] # address in this form [ip1:port1, ip2:port2]
    
    # clean and split the data
    nodes = nodes.replace('[', '')
    nodes = nodes.replace(']', '')
    nodes = nodes.split(',')

    for node in nodes:
        print( node )
        blockchain.nodes.add(node)
    
    return {'registered_nodes': list(blockchain.nodes)}

@app.route('/nodes/resolve', methods=['GET'])
def resolve_nodes():
    if not blockchain.resolveConflicts():
        return 'Chain not changed'
    return 'Chain changed'