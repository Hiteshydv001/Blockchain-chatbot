# 🚀 Blockchain-Powered AI Chatbot

A chatbot that integrates **Blockchain (Ethereum, Solidity)** and **AI (Gemini LLM)** to log chat messages immutably on the blockchain while generating AI-powered responses.

## 📁 Project Structure
```
└── hiteshydv001-blockchain-chatbot/
    ├── main.py             # Main chatbot application
    ├── requirements.txt    # Required dependencies
    └── test.py             # Solidity version test script
```

![image](https://github.com/user-attachments/assets/147389ae-86f0-43fd-8a10-df26008e4703)

![image](https://github.com/user-attachments/assets/39874126-50d7-4f7e-ab1d-22b05435f847)

![image](https://github.com/user-attachments/assets/9d856e84-977a-4330-91c3-6f9613eea5b1)


## 🌟 Features
- ✅ **AI Chatbot** powered by Google Gemini LLM
- ✅ **Immutable Chat Logging** using Ethereum blockchain (Ganache)
- ✅ **Solidity Smart Contract** for event-based message logging
- ✅ **Automatic Solidity Compiler Management** with `solcx`
- ✅ **Seamless Interaction** between AI and blockchain

## 🛠️ Setup & Installation
### 1️⃣ Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- **Ganache** (for local Ethereum blockchain simulation)
- **Node.js & npm** (for managing dependencies, if required)

### 2️⃣ Clone the Repository
```sh
$ git clone https://github.com/hiteshydv001/blockchain-chatbot.git
$ cd hiteshydv001-blockchain-chatbot
```

### 3️⃣ Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4️⃣ Start Ganache
Ensure Ganache is running on `http://127.0.0.1:7545`.

### 5️⃣ Set Up Environment Variables
Create a `.env` file and add your **Google Gemini API Key**:
```
GEMINI_API_KEY=your_api_key_here
```

### 6️⃣ Run the Chatbot
```sh
$ python main.py
```

## 📜 Smart Contract (Solidity)
The chatbot logs messages on the Ethereum blockchain using the following Solidity contract:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ChatLog {
    event MessageLogged(address indexed sender, string message, uint256 timestamp);
    
    function logMessage(string calldata message) public {
        emit MessageLogged(msg.sender, message, block.timestamp);
    }
}
```

## 🔍 Testing Solidity Compiler
Run the following command to check available Solidity compiler versions:
```sh
$ python test.py
```

## 🤖 How It Works
1. **User enters a message** → Sent to Google Gemini AI.
2. **Gemini AI processes the message** → Generates a response.
3. **Response is logged on the blockchain** → Immutable chat history.
4. **User and Bot messages are recorded** securely.

## 🏆 Future Enhancements
- [ ] Integrate a frontend UI for better interaction.
- [ ] Deploy the smart contract on a public Ethereum testnet.
- [ ] Implement a database for AI response tracking.
- [ ] Add multi-user support with authentication.

## 🎯 Contributing
Pull requests are welcome! Feel free to fork the repo, make changes, and submit a PR.

## 📜 License
This project is licensed under the **MIT License**.

---
💡 **Developed by Hitesh Kumar | 2025** 🚀

