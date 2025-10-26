# Assignement 1 - Enhanced Caesar Cipher


# Description: 
This python project demonstrates an implementation of the **Enhanced Caesar Cipher** algorithm supporting **encryption, decryption, and brute-force attack** using a sample vocabulary. This project shows how encryption can be implemented, analyzed and broken using simple cryptographic principles. 

# Features 
- **Encryption**: Encrypt plaintext using Caesar Cipher with an user defined key
- **Decryption**: Decrypt ciphertext using the known key
- **Brute-force attack**: Automatically guess the correct key by matching against a vocabulary list('sample.txt') 


# Files
It includes: 
'main.py' - user interface
'caesar_cipher.py' - cipher logic and brute-force attack implementation
'sample.txt' - vocabulary list used for brute-force analysis


# How to run
The program can be run in the terminal or vscode with: 

**python3 main.py**

Example: After Running, 
**Encript (key=3)**
                   . Input: Hello, World!
                   . Output: Khoor, Zruog!

**Decrypt (key=3)**
                  . Input: Khoor, Zroug!
                  . Output: Hello, World!
