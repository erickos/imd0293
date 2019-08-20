# Atividade: Blocos

Esta atividade tem como objetivo implementar o modelo de dados responsável por representar um bloco em nosso blockchain, além de implementar métodos responsáveis pela criação destes blocos.

## Metodologia e Avaliação

O desenvolvimento das atividades avaliativas em sala de aula será realizada individualmente, em computador pessoal ou em computador do laboratório, com livre consulta a recursos na internet (*consulta != cópia*) e discussão entre colegas. Utilize o sistema operacional Linux e a  IDE de sua preferência (sugestão: Visual Studio Code).

Ao finalizar a atividade, chame o professor para que seja realizada a avaliação. As atividades são cumulativas, de forma que ao final teremos um blockchain funcional usando as técnicas e os conceitos téoricos vistos em sala de aula.

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários.

## Descrição

A estrutura para representar um bloco deve seguir o seguinte modelo:

```json
block = {
    'index': 2,
    'timestamp': 1506057125,
    'nonce': 324984,
    'merkleRoot': "13c8bbf1dde38d5f86bfc48a5c027df0d8eb19c8a647de49976755e1b35b31ca",
    'previousHash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ]
}
```

Onde:

- `index`: índice do bloco, que representa a profundidade do bloco no blockchain (o bloco genesis tem `index` 0);
- `timestamp` : data (formato unix) de criação do novo bloco;
- `nonce` : por enquanto pode deixar esse atributo com valor 0;
- `merkleRoot` : por enquanto pode deixar esse atributo com valor 0;
- `previousHash` : *hash* do cabeçalho do bloco anterior. O cabeçalho é formado pelos campos `index`, `timestamp`, `nonce`, `merkleRoot` e `previousHash`. Calcule o *hash* do bloco a partir do dicionário que representa a estrutura, lembrando de excluir o atributo `transactions`, que não faz parte do cabeçalho;
- `transactions` : lista de transações incluídas no bloco; por enquanto pode deixar como uma lista vazia, não é necessário modelar a estrutura da transação.

A assinatura do método já está presente na classe `Blockchain`:

```python
def createBlock(self, nonce=0, previousHash=None)
```

Implemente também o método `createGenesisBlock()`, responsável por criar o bloco Genêsis, invocando o método `createBlock()` previamente implementado:

```python
def createGenesisBlock(self):
```

Note que o construtor foi definido, assim como alguns atributos da classe `Blockchain`:

- `chain` : uma lista de blocos, representando o blockchain;
- `memPool` : o *memory pool*, responsável por armazenar, temporariamente, transações que aidna não foram incluídas em um bloco;

Por fim, implemente o método `printChain()`, responsável por imprimir no terminal uma saída que represente o estado atual do seu blockchain, ressaltando os atributos de cada bloco. Um exemplo de *output* pode ser visto abaixo, mas sinta-se a vontade para implementar da maneira que desejar:

```
 __________________________________________________________________
| 8e853d40b1931e0272ad33fae0f3854d9914aa6696653f01fa7a05584ac250dc |                
 ------------------------------------------------------------------                
| Índice:         Timestamp:              Nonce:                   |
| 4               1566323766              0                        |                
|                                                                  |                
| Merkle Root:                                                     |
| 0000000000000000000000000000000000000000000000000000000000000000 |                
|                                                                  |                
| Transações:                                                      |
| 0                                                                |                
|                                                                  |                
| Hash do último bloco:                                            |
| ea1d3930d2d494cfec7e030679f74cbe997f1fc0eeadeb67a24f1943d104b723 |                
 ------------------------------------------------------------------
                                A                                    
                                |                                    
 __________________________________________________________________
| ea1d3930d2d494cfec7e030679f74cbe997f1fc0eeadeb67a24f1943d104b723 |                
 ------------------------------------------------------------------                
| Índice:         Timestamp:              Nonce:                   |
| 3               1566323766              0                        |                
|                                                                  |                
| Merkle Root:                                                     |
| 0000000000000000000000000000000000000000000000000000000000000000 |                
|                                                                  |                
| Transações:                                                      |
| 0                                                                |                
|                                                                  |                
| Hash do último bloco:                                            |
| e41cd82c0f0556dbee53a037be6871048005cda39140fde5b5deeaaf66e8a52b |                
 ------------------------------------------------------------------
                                A                                    
                                |                                    
 __________________________________________________________________
| e41cd82c0f0556dbee53a037be6871048005cda39140fde5b5deeaaf66e8a52b |                
 ------------------------------------------------------------------                
| Índice:         Timestamp:              Nonce:                   |
| 2               1566323766              0                        |                
|                                                                  |                
| Merkle Root:                                                     |
| 0000000000000000000000000000000000000000000000000000000000000000 |                
|                                                                  |                
| Transações:                                                      |
| 0                                                                |                
|                                                                  |                
| Hash do último bloco:                                            |
| 0ce9ea8b4e967cc39b7db116164d0c067083ff351c21ee0454f9eda672be59a7 |                
 ------------------------------------------------------------------
                                A                                    
                                |                                    
 __________________________________________________________________
| 0ce9ea8b4e967cc39b7db116164d0c067083ff351c21ee0454f9eda672be59a7 |                
 ------------------------------------------------------------------                
| Índice:         Timestamp:              Nonce:                   |
| 1               1566323766              0                        |                
|                                                                  |                
| Merkle Root:                                                     |
| 0000000000000000000000000000000000000000000000000000000000000000 |                
|                                                                  |                
| Transações:                                                      |
| 0                                                                |                
|                                                                  |                
| Hash do último bloco:                                            |
| 0000000000000000000000000000000000000000000000000000000000000000 |                
 ------------------------------------------------------------------
```


## Dicas

- [https://docs.python.org/3/library/time.html]

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
