# Atividade: Assinaturas Digitais

Esta atividade tem como objetivo implementar o algoritmo responsável por assinar uma mensagem utilizando uma chave privada, e posteriormente verificar a assinatura e a mensagem utilizando uma chave pública fornecida. Essa ideia será utilizada para garantirmos a autenticidade e a integridade de transações que serão incluídas em nossa blockchain.

## Metodologia e Avaliação

O desenvolvimento das atividades avaliativas em sala de aula será realizada individualmente, em computador pessoal ou em computador do laboratório, com livre consulta a recursos na internet (*consulta != cópia*) e discussão entre colegas. Utilize o sistema operacional Linux e a  IDE de sua preferência (sugestão: Visual Studio Code).

Ao finalizar a atividade, chame o professor para que seja realizada a avaliação. As atividades são cumulativas, de forma que ao final teremos um blockchain funcional usando as técnicas e os conceitos téoricos vistos em sala de aula.

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários.

## Descrição

A atividade consiste na implementação do método `def sign(privKey, message)` para retornar a assinatura digital da mensagem `message` criada a partir da chave privada `privKey` fornecida como argumento.

```python
def sign(privKey, message):
```

Implemente também o método `def verifySignature(address, signature, message)`, que retorna `True` caso a assinatura digital esteja coerente com a mensagem `message`  e a chave pública `address` fornecida como argumento.

```python
def verifySignature(address, signature, message):
```

Para testar precisaremos gerar um par de chave pública e privada. Como usamos o algoritmo implementado no protocolo Bitcoin, vamos utilizar uma carteira web para gerar o par de chaves:

https://www.bitaddress.org

Note que após a geração a chave pública é denominada e codificada como um endereço bitcoin (*bitcoin address*), e a chave privada como chave privada (*private key*).

Voce também pode verificar assinaturas digitais com mensagens e endereços bitcoin neste [link](https://btc.coin.space/messages/verify)

## Dicas

[GitHub do bitcoinlib](https://github.com/petertodd/python-bitcoinlib)

[Exemplo de uso dos módulos de assinatura](https://github.com/petertodd/python-bitcoinlib/blob/master/examples/sign-message.py)

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
