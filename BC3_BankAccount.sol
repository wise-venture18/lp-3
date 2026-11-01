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
