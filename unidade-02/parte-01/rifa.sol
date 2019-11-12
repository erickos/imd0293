// Nome: Erick de Oliveira Silva
// Nome: Juliana Barbosa dos Santos
// Conta do contrato: <https://ropsten.etherscan.io/address/0x7650614d86d92f25796bedf7c6b26c003f30d669>

pragma  solidity  ^0.4.25; // Fique a vontade caso queira utilizar outra versão.

contract Rifa {

    address owner;
    address winner;
    
    constructor() public {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Somente o dono do contrato pode chamar essa função!");
        _;
    }
    
    modifier onlyWinner {
        require(msg.sender == winner, "Somente o vencedor pode sacar!");
        _;
    }
    
    
    mapping (uint => address) private rifaToBuyer;
    mapping (address => uint) ownerRifaCount;
    
    uint private totalRifasBought = 0;
    
    // id da rifa sempre será o totalRifasBought(atual) + 1
    function comprarRifa() external payable {
        
        uint qtdRifas = msg.value/(0.1 ether);
        
        for( uint i=0; i < qtdRifas; i++ ){
            totalRifasBought++;
            rifaToBuyer[totalRifasBought] = msg.sender;
            ownerRifaCount[msg.sender]++;
        }

    }
    
    function actualPoolPrize() public view returns (uint) {
         return (totalRifasBought * 0.1 ether)/2;
    }
    
    function accountTotalRifas() public view returns (uint) {
        return ownerRifaCount[msg.sender];
    } 
    
    function raffle() public onlyOwner {
        uint winnerRifa = uint(keccak256(abi.encodePacked(now, msg.sender)))%(totalRifasBought);
        winner = rifaToBuyer[winnerRifa];
    }
    
    function transferPrize() public onlyWinner {
        winner.transfer( address(this).balance/2 );
    }
    
    
}
