# Atividade: Transações

Esta atividade tem como objetivo implementar o modelo de dados responsável por representar uma transação em nosso blockchain, além de implementar métodos responsáveis pela criação destas transações.

## Metodologia e Avaliação

O desenvolvimento das atividades avaliativas em sala de aula será realizada individualmente, em computador pessoal ou em computador do laboratório, com livre consulta a recursos na internet (*consulta != cópia*) e discussão entre colegas. Utilize o sistema operacional Linux e a  IDE de sua preferência (sugestão: Visual Studio Code).

Ao finalizar a atividade, chame o professor para que seja realizada a avaliação. As atividades são cumulativas, de forma que ao final teremos um blockchain funcional usando as técnicas e os conceitos téoricos vistos em sala de aula.

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários.

## Descrição

A estrutura para representar um bloco deve seguir o seguinte modelo:

```json
transaction = {
        "sender": "19sXoSbfcQD9K66f5hwP5vLwsaRyKLPgXF",
        "recipient": "1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N",
        "amount": 0.01,
        "timestamp": 1569509839,
        "signature": "H7p3IGJAXvOnKv2dzhNHuSSHh5yyzDgehxBqWHoB+j4EZiMrep4SDH0zAk6jTGnnA1UIfW1RK4JorCVtA6Er6R8="
}
```

Onde:

- `sender` : remetente da transação;
- `recipient` : destinatário da transação;
- `amount`: valor a ser transferido do endereço do `sender` para o endereço do `recipient`;
- `timestamp` : data (formato unix) de criação da transação;
- `signature` : assinatura digital assinado pela chave privada da pessoa que criou a transação (`sender`). A mensagem assinada é correspondente a estrutura da transação completa com exceção do atributo `signature`.

A assinatura do método de criação de transações já está presente na classe `Blockchain`:

```python
def createTransaction(self, sender, recipient, amount, timestamp, privKey):
```

Note que a chave privada `privKey` é passada como parâmetro, mas o que é persistido na transação é a assinatura gerada por essa chave privada em conjunto com a mensagem (no caso, a mensagem é a transação completa com exceção do atributo `signature`).

Lembre que toda transação criada deve ser adicionada ao *memory pool*, representada no nosso blockchain pelo atributo `memPool`. Revise seu método `createBlock()` para implementar a inclusão dessas transações no ato de criação do bloco, assim como implemente o método responsável por gerar o *Merkle Root* das transações de um bloco e incluir em seu cabeçalho. A assinatura do método para geração do *Merkle Root* já está definida:

```python
def generateMerkleRoot(transactions):
```

Ajuste também o seu método `printChain` para imprimir na tela também os detalhes de cada transação incluída em cada bloco.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
