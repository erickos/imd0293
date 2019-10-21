# Atividade Final: API e Consenso

Esta atividade tem como objetivo implementar uma API de acesso ao nosso blockchain. Isso permitirá a interação entre múltiplos nós que implementem nosso protocolo. Outro objetivo desta atividade é definir o modelo de consenso.

## Metodologia e Avaliação

Essa atividade encerra o projeto de desenvolvimento de nosso *blockchain* privado. A entrega será realizada no formato de apresentação presencial ao professor, no dia **22/10/2019**. O trabalho deve ser desenvolvido individualmente ou em dupla. Plágios não serão tolerados, resultando em nota zero para todos os envolvidos.

A nota da Unidade 1 será formada a partir dos seguintes componentes e seus respectivos pesos:

- Nota da prova escrita (50%)
- Nota das atividades anteriores (20%)
- Nota desta atividade final (30%)

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários.

## Descrição

Sua API precisará implementar 5 *end-points*:

- [POST] `/transactions/create` para criar uma nova transação a ser incluída no próximo bloco. No corpo da requisicão HTTP, usando POST, inclua as informações necessárias para criação de uma nova transação.
- [GET] `/transactions/mempool` para retornar a *memory pool* do nó.
- [GET] `/mine` para informar o nó para criar e minerar um novo bloco.
- [GET] `/chain` para retornar o blockchain completo.
- [POST] `/nodes/register` para aceitar uma lista de novos nós no formato de URLs. Note que já existe uma variável do tipo conjunto (*set*) chamado `nodes` para armazenar os nós registrados.
- [GET] `/nodes/resolve` para executar o modelo de consenso, resolvendo conflitos e garantindo que contém a cadeia de blocos correta.

Utilize qualquer *framework* que desejar. Uma sugestão é o *framework* [Flask](https://palletsprojects.com/p/flask/), bastante leve e de fácil utilização.

Para auxiliar no desenvolvimento, implemente os métodos `isValidChain()` e `resolveConflicts()`. As assinaturas já estão no código exemplo.

Para testar, será necessário executar no mínimo dois nós simultaneamente, no caso de ser na mesma máquina, instâncias em execução em portas diferentes.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
