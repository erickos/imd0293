# Smart Contract: poupanca.sol

Usando a IDE [Remix](http://remix.ethereum.org), desenvolva um contrato inteligente que implemente um sistema simplificado de **poupança** descentralizado e autônomo. Esse *smart contract* será implantado no blockchain de testes do Ethereum conhecido como *Ropsten Test Network*. Para integração com o Remix, lembre que é necessário uma carteira (*wallet*) MetaMask instalada em seu navegador. Também é necessário ao menos uma conta na rede Ropsten com saldo positivo. Para obter *ether* nesta rede, utilize um dos Faucets abaixo, conforme já feito em sala de aula:

[](https://faucet.metamask.io/)

https://faucet.metamask.io

[](https://faucet.ropsten.be/)

https://faucet.ropsten.be

## Metodologia e Avaliação

O trabalho deve ser realizado **individualmente ou em dupla**. O contrato desenvolvido (ou contratos, caso sejam múltiplos arquivos) deve ser submetido no SIGAA ** até o dia 12/11 as 16:50**, contendo no cabeçalho os nomes dos componentes e o *link* para o *block explorer* (ropsten.etherescan.io)  referente a conta do seu contrato após o *deploy* na rede Ropsten do Ethereum. Note que talvez você precise realizar o deploy múltiplas vezes, porém, envie o *link* somente daquela versão que você considera a final para submissão. **Além disso, o contrato deverá ser apresentado em sala de aula no mesmo dia 12/11**.

Veja como ficará o cabeçalho do seu arquivo *.sol*:
```javascript
// Nome: <nome do componente 1>
// Nome: <nome do componente 2>
// Conta do contrato: <link da conta do seu contrato após o deploy>

// Seu contrato começa aqui!
```

## Requisitos

Seu contrato deve permitir que usuários depositem determinado valor de *ether* e especifiquem um tempo, em dias, de no máximo 30 dias e mínimo 1 dia. Esse valor não poderá ser resgatado pelo usuário até a data estipulada, e caso queira sacar antes do tempo determinado, deverá ser paga uma taxa de 10% do valor originalmente depositado (que ficará para o contrato). Caso o tempo estipulado já tenha sido cumprido, o resgate é realizado sem custos adicionais, e somente pode ser realizado de forma integral (todo o valor originalmente depositado).

Note que o objetivo desta poupança não é prover rendimentos para o cliente, e sim funcionar como uma maneira de não permitir que tal valor seja gasto antes do tempo estipulado, sendo assim uma "poupança forçada", sem a necessidade de terceiros.

Implemente as seguintes funções:

- Função para depositar um valor definindo o tempo (em dias) em que o valor ficará bloqueado.

*Ex: Se eu quiser posso depositar 10 ether por 10 dias.*

- Função para consultar o valor depositado pelo remetente da transação.

*Ex: Se eu quiser posso consultar o meu saldo na poupança, retornando 10 ether.*

- Função para consultar o tempo restante para resgatar meu depósito sem multas.

*Ex: Se eu quiser posso consultar o tempo restante do meu depósito, por exemplo, 9 dias.*

- Função para consultar o valor da multa caso queira sacar o valor antes do tempo.

*Ex: Se eu quiser posso consultar minha multa, a função retornará 0,1 ether.*

- Função para resgatar o valor depositado em sua totalidade.

*Ex: Se eu quiser posso sacar meu valor depositado. Caso o tempo já tenha sido cumprido, não é necessário enviar nenhum valor na transação. Caso o tempo ainda não tenha sido cumprido, é necessário incluir como valor da transação o valor da multa.*

- Função para transferir a propriedade de um depósito para outro endereço.

*Ex: Se eu quiser eu posso depositar 10 ether, e depois trocar a propriedade desse depósito para um outro endereço. Desta forma, este outro endereço será o novo dono do depósito e poderá sacar o valor.*

## Código Base

Para agilizar o desenvolvimento já é fornecido um código base com um modificador `onlyOwner` que verifica se o endereço que invocou a transação é o dono do contrato (aquele que realizou o *deploy* do contrato). Utilize o código base somente se quiser (*poupanca.sol*).

```javascript
// Nome: <nome do componente 1>
// Nome: <nome do componente 2>
// Conta do contrato: <link da conta do seu contrato após o deploy>

pragma  solidity  ^0.4.25; // Fique a vontade caso queira utilizar outra versão.

contract  Poupanca {

	address owner;

	constructor() public {
		owner =  msg.sender;
	}

	modifier onlyOwner {
		require(msg.sender == owner, "Somente o dono do contrato pode invocar essa função!");
		_;
	}
	
}
```
