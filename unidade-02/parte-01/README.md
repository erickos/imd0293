# Smart Contract: rifa.sol

Usando a IDE [Remix](http://remix.ethereum.org), desenvolva um contrato inteligente que implemente um sistema de **rifa** descentralizado. Esse *smart contract* será implantado no blockchain de testes do Ethereum conhecido como *Ropsten Test Network*. Para integração com o Remix, lembre que é necessário uma carteira (*wallet*) MetaMask instalada em seu navegador. Também é necessário ao menos uma conta na rede Ropsten com saldo positivo. Para obter *ether* nesta rede, utilize um dos Faucets abaixo, conforme já feito em sala de aula:

[](https://faucet.metamask.io/)

https://faucet.metamask.io

[](https://faucet.ropsten.be/)

https://faucet.ropsten.be

## Metodologia e Avaliação

O trabalho deve ser realizado **individualmente ou em dupla**. O contrato desenvolvido (ou contratos, caso sejam múltiplos arquivos) deve ser submetido no SIGAA **até as 18:30**, contendo no cabeçalho os nomes dos componentes e o *link* para o *block explorer* (ropsten.etherescan.io)  referente a conta do seu contrato após o *deploy* na rede Ropsten do Ethereum. Note que talvez você precise realizar o deploy múltiplas vezes, porém, envie o *link* somente daquela versão que você considera a final para submissão.

Veja como ficará o cabeçalho do seu arquivo *.sol*:
```javascript
// Nome: <nome do componente 1>
// Nome: <nome do componente 2>
// Conta do contrato: <link da conta do seu contrato após o deploy>

// Seu contrato começa aqui!
```

## Requisitos

Implemente as seguintes funções:

- Função para comprar quantas rifas quiser, baseado no valor (`msg.value`) enviado na transação. O preço deve ser de 0,1 *ether* cada rifa. 

*Ex: Se eu quiser posso comprar 3 rifas de uma vez incluindo 0,3 *ether* na transação.*

- Função para retornar o prêmio atual (em *wei*). O prêmio é 50% do total arrecadado até o momento. O restante fica como saldo do contrato.

*Ex: Se no momento que essa função é chamada já tiverem sido vendidas 100 rifas, a função deve retornar 5000000000000000000, equivalente a 5 ether.*

- Função para retornar o total de rifas compradas pela conta que gerou a transação para esta função.  

*Ex: Se a conta `0x8cb32fEc81882D046b95D9e761fC09931e2E8F7b` comprou 3 rifas, quando esta conta gerar uma transação chamando essa função deve retornar o valor 3.*

- Função para sortear a rifa, com a restrição de que somente o dono do contrato (aquele que fez o *deploy* pode chamar essa função. Ao chamar essa função deve ser sorteado, aleatoriamente uma das rifas previamente criadas. Essa função não deve transferir o prêmio para o ganhador, mas sim liberar a possibilidade do ganhador sacar o prêmio a partir da chamada da função de sacar prêmio. Para gerar um número aleatório utilize a função abaixo, adaptado para o seu programa:

```javascript
// Gerando números aleatórios entre 1 e 100:
uint random = uint(keccak256(abi.encodePacked(now, msg.sender))) % 100;
```

- Função para sacar todo o prêmio (transferir para da conta do contrato para a conta do ganhador), caso o remetente (`msg.sender`) da transação seja o ganhador do rifa, retornando o valor sacado.

*Ex: Se a conta `0x8cb32fEc81882D046b95D9e761fC09931e2E8F7b` é o ganhador, ao chamar essa função haverá uma transferência do prêmio da conta do contrato para conta desse usuário, retornando o valor transferido.*

## Extras

Para pontuação extra, torne seu contrato reaproveitável, ou seja, poder gerenciar outra rifa após o término de um sorteio.

Para pontuação extra, crie Eventos para:
- Notificar quando uma rifa é comprada;
- Notificar quando a rifa é sorteada.

Desenvolva outra funcionalidades bacanas e ganhe pontos extras!

## Código Base

Para agilizar o desenvolvimento já é fornecido um código base com um modificador `onlyOwner` que verifica se o endereço que invocou a transação é o dono do contrato (aquele que realizou o *deploy* do contrato). Utilize o código base somente se quiser (*rifa.sol*).

```javascript
// Nome: <nome do componente 1>
// Nome: <nome do componente 2>
// Conta do contrato: <link da conta do seu contrato após o deploy>

pragma  solidity  ^0.4.25; // Fique a vontade caso queira utilizar outra versão.

contract  Rifa {

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
