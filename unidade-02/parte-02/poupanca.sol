// Nome: Erick de Oliveira Silva
// Nome: Juliana Barbosa dos Santos
// Conta do contrato: <link da conta do seu contrato após o deploy>

pragma  solidity  ^0.4.25; // Fique a vontade caso queira utilizar outra versão.

contract  Poupanca {

	address owner;
	
	struct DepositTime {
	    uint value;
	    uint creationTime;
	    uint timeToUnlock;
	}
	
    mapping (address => DepositTime) private UserToDeposits;

	
 	constructor() public {
		owner =  msg.sender;
	}

	modifier onlyOwner {
		require(msg.sender == owner, "Somente o dono do contrato pode invocar essa função!");
		_;
	}
	
	function deposit( uint _daysToUnlock ) external payable {
        require( _daysToUnlock >= 1 && _daysToUnlock <= 30, "Quantidade de dias que o depósito permanece bloqueado deve estar entre 1 e 30" );
        
        UserToDeposits[msg.sender] = DepositTime( msg.value * 1 wei, now, (now + (_daysToUnlock * 1 days) ) );	    
	}
	
	function getUserBalance() public view returns (uint) {
	    // Returns at wei unit
	    return UserToDeposits[msg.sender].value;
	}
	
	function getRemainingTimeToUnlock() public view returns (uint) {
	    return ( UserToDeposits[msg.sender].timeToUnlock - now ) / 1 days;
	}
	
	function consultPenalty() public view returns (uint) {
	    // in wei unit
	    return UserToDeposits[msg.sender].value/10;
	}
	
	function withdraw() public {
	    
	    if( now >= UserToDeposits[msg.sender].timeToUnlock  ) {
	        msg.sender.transfer( UserToDeposits[msg.sender].value );
	    } else {
	        uint penalty = UserToDeposits[msg.sender].value/10;
	        UserToDeposits[msg.sender].value -= penalty;
	        msg.sender.transfer( UserToDeposits[msg.sender].value );
	    }
	    
	    delete UserToDeposits[msg.sender];
	}
        	
    function transferDepositOwner( address _newOwner ) public {
        UserToDeposits[_newOwner] = UserToDeposits[msg.sender];
        
        delete UserToDeposits[msg.sender];
    } 	
}