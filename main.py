import os
from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

if not w3.is_connected():
    raise Exception("Error: Could not connect to Ganache. Make sure Ganache is running.")

# Set the first Ganache account as the default account
w3.eth.default_account = w3.eth.accounts[0]

# Solidity smart contract as a string
contract_source_code = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ChatLog {
    event MessageLogged(address indexed sender, string message, uint256 timestamp);
    
    function logMessage(string calldata message) public {
        emit MessageLogged(msg.sender, message, block.timestamp);
    }
}
'''

# Ensure the correct Solidity version is installed
solc_version = "0.8.0"
try:
    set_solc_version(solc_version)
except:
    print(f"Solidity {solc_version} not found. Installing now...")
    install_solc(solc_version)
    set_solc_version(solc_version)

# Compile the Solidity contract
compiled_sol = compile_source(contract_source_code)
contract_id, contract_interface = compiled_sol.popitem()

# Extract bytecode and ABI
bytecode = contract_interface['bin']
abi = contract_interface['abi']

# Deploy the contract to Ganache
ChatLog = w3.eth.contract(abi=abi, bytecode=bytecode)
print("Deploying chatbot contract...")

tx_hash = ChatLog.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt.contractAddress

print("Contract deployed at this address:", contract_address)

# Create a contract instance to interact with
chatlog_contract = w3.eth.contract(address=contract_address, abi=abi)

# Function to log messages on the blockchain
def log_message_on_blockchain(message):
    try:
        tx_hash = chatlog_contract.functions.logMessage(message).transact()
        w3.eth.wait_for_transaction_receipt(tx_hash)
        print('Logged on blockchain. Tx Hash:', tx_hash.hex())
    except Exception as e:
        print("Error logging on Blockchain:", e)

# Function to get chatbot response from Gemini API
def get_chatbot_response(user_message):
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)
        
        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            return "I'm unable to process your request."
    
    except Exception as e:
        print("Error getting response from LLM:", e)
        return "I am having trouble processing that."

# Main chatbot function
def main():
    print("Welcome to Blockchain + AI Simple Chatbot")
    print("Type 'exit' or 'quit' to end the chatbot.\n")
    
    while True:
        user_message = input("You: ")
        if user_message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        bot_response = get_chatbot_response(user_message)
        print("Bot:", bot_response)
        
        log_message_on_blockchain(f"User: {user_message}")
        log_message_on_blockchain(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
