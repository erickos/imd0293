# Atividade: Proof-of-Work

Esta atividade tem como objetivo implementar o algoritmo responsável por minerar um novo bloco ao encontrar um *nonce* válido para os dados de entrada (*proof-of-work*), considerando uma dificuldade fixa.

## Metodologia e Avaliação

O desenvolvimento das atividades avaliativas em sala de aula será realizada individualmente, em computador pessoal ou em computador do laboratório, com livre consulta a recursos na internet (*consulta != cópia*) e discussão entre colegas. Utilize o sistema operacional Linux e a  IDE de sua preferência (sugestão: Visual Studio Code).

Ao finalizar a atividade, chame o professor para que seja realizada a avaliação. As atividades são cumulativas, de forma que ao final teremos um blockchain funcional usando as técnicas e os conceitos téoricos vistos em sala de aula.

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários.

## Descrição

A atividade consiste na implementação do método `mineProofOfWork()` para retornar e atribuir um *nonce* válido para o último bloco criado. A dificuldade é fixa e definida pela variável `DIFFICULTY`, que representa a quantidade de zeros em hexadecimais exigidas no início do *hash* do cabeçalho do bloco. A assinatura do método é definida como:

```python
def mineProofOfWork(self, prevBlock):
```

Implemente também o método `isValidProof(block, nonce)`, que retorna `true` caso o `nonce` passado como argumento é válido para o bloco `block` passado também como argumento.

```python
def isValidProof(block, nonce):
```

A dificuldade definida para essa atividade é que o *hash* do cabeçalho do bloco deve ser menor que o alvo (*target*) abaixo:

```alvo = 0x0001000000000000000000000000000000000000000000000000000000000000```

Isso quer dizer que o *hash* encontrado deve ter um prefixo de quatro caracteres hexadecimais 0's. Exemplos:

- [INVÁLIDO] 00078112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
- [INVÁLIDO] 0001e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d
- [VÁLIDO]   00002c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6

Por fim, implemente também o método auxiliar `getBlockID(block)`, que retorna o *hash* do cabeçalho do bloco passado como argumento.

```python
def getBlockID(block):
```

## Dicas

Note que, para facilitar, foi criado uma propriedade (*@property*) chamada `prevBlock` que retorna o último bloco incluído na lista `chain`.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
