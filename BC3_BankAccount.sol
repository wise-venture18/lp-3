// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Bank Account Smart Contract
contract BankAccount {

    // Store account balance
    mapping(address => uint) public balance;

    // Deposit money
    function deposit() public payable {
        require(msg.value > 0, "Amount must be greater than zero");

        balance[msg.sender] += msg.value;
    }

    // Withdraw money
    function withdraw(uint amount) public {
        require(amount > 0, "Invalid amount");

        require(balance[msg.sender] >= amount,
                "Insufficient balance");

        balance[msg.sender] -= amount;

        payable(msg.sender).transfer(amount);
    }

    // Show account balance
    function showBalance() public view returns (uint) {
        return balance[msg.sender];
    }
}

//-------------- END OF PROGRAM----------





//(Alternative Code) Try Below Program If Above Doesn't Work

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {

    // Store customer balances
    mapping(address => uint) public balanceOf;

    // Deposit money
    function deposit() public payable {
        require(msg.value > 0, "Deposit must be greater than zero");

        balanceOf[msg.sender] += msg.value;
    }

    // Withdraw entire balance
    function withdraw() public payable {

        // Do not accept additional ETH during withdrawal
        require(msg.value == 0, "Do not send ETH while withdrawing");

        uint amount = balanceOf[msg.sender];

        require(amount > 0, "Insufficient balance");

        // Update balance before transferring ETH
        balanceOf[msg.sender] = 0;

        // Transfer money to customer
        payable(msg.sender).transfer(amount);
    }

    // Show account balance
    function showBalance() public view returns (uint) {
        return balanceOf[msg.sender];
    }
}
