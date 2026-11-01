"""
Group C: Blockchain Technology (BC-1, BC-2 & BC-3)
Here are 40 important combined viva questions with answers in normal text format.

1. Blockchain Basics

1. What is Blockchain?
Blockchain is a decentralized digital ledger that stores transactions in blocks connected together securely.

2. What is Cryptocurrency?
Cryptocurrency is a digital currency that uses cryptography to secure transactions.

3. What is Ethereum?
Ethereum is a blockchain platform that supports cryptocurrency transactions and smart contracts.

4. What is Ether (ETH)?
Ether is the native cryptocurrency of the Ethereum blockchain. It is used to pay transaction fees and interact with smart contracts.

5. What is a Decentralized Network?
A network where control is distributed among multiple computers instead of a single central authority.

2. MetaMask and Wallet (BC-1 & BC-2)

6. What is MetaMask?
MetaMask is a cryptocurrency wallet used to manage Ethereum accounts and interact with blockchain applications.

7. Why do we use MetaMask?
To create wallets, manage crypto assets, send and receive ETH, and connect to decentralized applications.

8. What is a Crypto Wallet?
A crypto wallet is a tool that manages cryptographic keys used to access and control cryptocurrency.

9. What is a Public Key?
A public key is used to generate a wallet address and can be shared to receive cryptocurrency.

10. What is a Private Key?
A private key is a secret key used to authorize transactions. It should never be shared.

11. What is a Wallet Address?
A wallet address is a unique identifier used to send and receive cryptocurrency. Ethereum addresses usually start with 0x.

12. What is a Seed Phrase?
A seed phrase is a sequence of 12 or 24 words used to recover a wallet.

13. What is the difference between a Public Key and Private Key?
Public Key	                       Private Key
Used to derive wallet addresses	   Used to authorize transactions
Can be shared	                     Must remain secret
Helps receive funds	               Helps control funds

14. What is a Test Network?
A test network is a blockchain environment used to test transactions and smart contracts without using real ETH.

15. What is Sepolia?
Sepolia is an Ethereum test network used by developers to test smart contracts and transactions.

3. Ether Transactions and Gas Fees (BC-1)
16. What is a Transaction in Blockchain?
A transaction is an operation recorded on the blockchain, such as transferring ETH from one wallet to another.

17. What is Gas in Ethereum?
Gas is the unit used to measure the computational effort required to perform an operation on Ethereum.

18. What is a Gas Fee?
A gas fee is the amount of ETH paid to process a transaction on the Ethereum network.

19. How is the Gas Fee calculated?
Gas Fee = Gas Used × Gas Price.

20. What is Gwei?
Gwei is a smaller unit of Ether used to express gas prices.

1 ETH = 1,000,000,000 Gwei.

21. Why does every Ethereum transaction require a gas fee?
To compensate validators for processing transactions and executing smart contracts.

22. Does every transaction have the same gas fee?
No. Gas fees depend on the computational work required and network demand.

23. What happens if a transaction fails?
The transaction may still consume gas, so the sender generally pays the gas fee even if the operation fails.

4. Smart Contracts (BC-3)
24. What is a Smart Contract?
A smart contract is a program stored on a blockchain that automatically executes when its conditions are met.

25. Which programming language is used to write your smart contract?
Solidity.

26. What is Remix IDE?
Remix is an online development environment used to write, compile, deploy, and test Solidity smart contracts.

27. What is a Solidity Contract?
A contract is a collection of functions and data stored at a specific address on the blockchain.

28. What is mapping in Solidity?
Mapping is a key-value data structure. In your Bank contract, it maps a wallet address to its balance.

Example:
mapping(address => uint) public balanceOf;


29. Explain the three operations in your Bank smart contract.
- Deposit: Uses msg.value to receive ETH and adds it to the user's balance.
- Withdraw: Checks the user's balance and transfers the ETH back to the user.
- Show Balance: Displays the ETH balance recorded for the connected wallet address.

30. What is the difference between payable, view, and require in Solidity?
Keyword	Purpose
payable	Allows a function to receive ETH
view	Allows reading contract data without modifying it
require	Checks a condition and reverts if it is false

5. Smart Contract Code-Based Questions
31. What is msg.sender?
It represents the address of the account that called the current function.

32. What is msg.value?
It represents the amount of ETH sent with the current transaction, measured in Wei.

33. What is Wei?
Wei is the smallest unit of Ether.

1 ETH = 1,000,000,000,000,000,000 Wei.

34. Why do we use require() in the deposit function?
To ensure that the deposited amount is greater than zero.

35. Why do we set the user's balance to zero before transferring ETH during withdrawal?
To follow the checks-effects-interactions pattern and help prevent reentrancy attacks.

36. What is Reentrancy?
Reentrancy is a smart contract vulnerability where an external contract repeatedly calls a function before the previous execution finishes.

37. Why is showBalance() declared as view?
Because it only reads the stored balance and does not modify blockchain data.

38. What is the difference between ETH and Wei?
ETH is the main currency unit, while Wei is its smallest denomination.

39. What is the difference between a transaction and a smart contract?
A transaction is an operation submitted to the blockchain. A smart contract is a program deployed on the blockchain that can execute operations.

40. What is a Transaction Hash?
A transaction hash is a unique identifier generated for a blockchain transaction. It can be used to track the transaction on a block explorer.
"""
