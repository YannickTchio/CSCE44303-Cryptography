# Assignment 2: Encrypted Communication & Cryptographic Performance Analysis

## Project Overview

This project implements encrypted communications between two parties (Alice and Bob) using both **AES** and **RSA** encryption algorithms. It also includes performance benchmarking to analyze how key sizes affect computational costs.

Alice encrypts messages and writes them to a file (`ctext`), while Bob reads and decrypts those messages. 


The simulation runs two programs on the same computer where:
- **Alice** encrypts messages and writes them to a file
- **Bob** reads and decrypts the messages from the file

## Features

### Part 1: AES Encryption (128-bit)
- Implements AES-128 encryption in **CBC mode**
- Uses a shared secret key between Alice and Bob
- Encrypts messages of 18+ bytes
- Demonstrates symmetric encryption workflow

### Part 2: RSA Encryption (2048-bit)
- Implements RSA-2048 asymmetric encryption
- Uses public/private key pairs
- Encrypts messages of 18+ bytes using PKCS1 OAEP padding
- Demonstrates public key cryptography

### Part 3: Performance Benchmarking
- Compares encryption/decryption speeds across different key sizes
- **AES:** 128-bit, 192-bit, 256-bit keys
- **RSA:** 1024-bit, 2048-bit, 4096-bit keys
- Runs 100 iterations for statistical accuracy
- Measures and reports average execution times



## Technologies Used

- **Language:** Python 3
- **Libraries:** 
  - `pycryptodome` - Cryptographic operations (AES, RSA)
  - `time` - Performance measurements
  - `statistics` - Average calculations


##  Project Structure
```
Assignment2/
├── alice_aes.py         # Alice's AES encryption program
├── bob_aes.py           # Bob's AES decryption program
├── alice_rsa.py         # Alice's RSA encryption program
├── bob_rsa.py           # Bob's RSA decryption program
├── keygen.py            # Generate all cryptographic keys ( Needs to be run first)
├── perf_test.py         # Performance benchmarking script
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # This file

Generated files (not in repo) by running keygen.py:
├── ctext               # Encrypted message file
├── shared_key.txt      # AES shared secret key
├── bob_private.pem     # RSA private key
└── bob_public.pem      # RSA public key
```

## Installation

### Install Dependencies
 directly:
```bash
pip install pycryptodome
```

## Usage

### Step 1: Generate Cryptographic Keys
Run this **first** to generate all necessary keys:

```bash
python3 keygen.py
```

This creates:
- `shared_key.txt` - 128-bit AES key
- `bob_private.pem` - RSA private key
- `bob_public.pem` - RSA public key
- `ctext` - Empty file for encrypted messages

### Step 2: Test AES Encryption (Part 1)

**Terminal 1 - Alice encrypts:**
```bash
python3 alice_aes.py
```
Enter a message with at least 18 bytes when prompted.

**Terminal 2 - Bob decrypts:**
```bash
python3 bob_aes.py
```
Bob will display the decrypted message.

### Step 3: Test RSA Encryption (Part 2)

**Terminal 1 - Alice encrypts:**
```bash
python3 alice_rsa.py
```
Enter a message with at least 18 bytes when prompted.

**Terminal 2 - Bob decrypts:**
```bash
python3 bob_rsa.py
```
Bob will display the decrypted message.

### Step 4: Run Performance Tests (Part 3)
```bash
python3 perf_test.py
```
Enter exactly 7 bytes when prompted. The script will:
- Test AES with 128, 192, and 256-bit keys
- Test RSA with 1024, 2048, and 4096-bit keys
- Run 100 iterations for each configuration
- Display average encryption and decryption times

##  Example Output

### AES Encryption Example
```
Enter message (>=18 bytes): Hello from Alice!!
ciphertext(hex): a3f2b1c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2
Alice sent encrypted message to ctext. Bob, can now check it.
```

### Performance Test Example
```
=== AES avg times (sec) ===
AES-128: enc=0.000012, dec=0.000011
AES-192: enc=0.000014, dec=0.000013
AES-256: enc=0.000016, dec=0.000015

=== RSA avg times (sec) ===
RSA-1024: enc=0.001234, dec=0.003456
RSA-2048: enc=0.004567, dec=0.012345
RSA-4096: enc=0.018901, dec=0.089012
```
## Assignment Requirements Met

✅ **Part 1:** AES-128 CBC encryption with shared key (18+ byte messages)  
✅ **Part 2:** RSA-2048 encryption with public/private keys (18+ byte messages)  
✅ **Part 3:** Performance analysis with multiple key sizes (7-byte messages)  
✅ Command-line input/output  
✅ File-based message passing  
✅ Proper error handling  
✅ Clean, documented code  


## Testing

The program has been tested with:
- Various message lengths (18+ bytes for Parts 1&2, exactly 7 bytes for Part 3)
- Different character encodings (ASCII, Unicode)
- Edge cases (minimum length messages)
- All specified key sizes


## Performance Insights

From benchmarking results:
1. **AES** is significantly faster than **RSA** (100-1000x)
2. Larger key sizes increase computation time for both algorithms
3. RSA decryption is slower than encryption due to private key operations
4. AES performance scales linearly with key size
5. RSA performance scales exponentially with key size

## References

- [PyCryptodome Documentation](https://pycryptodome.readthedocs.io/)
- [AES (Advanced Encryption Standard)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [RSA (Rivest–Shamir–Adleman)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [PKCS#1 OAEP Padding](https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding)

