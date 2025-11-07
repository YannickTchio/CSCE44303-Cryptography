# Assignment 3: HMAC and RSA Authentication

Implementation of authenticated communications using HMAC-SHA256 and RSA-2048 digital signatures.

## Setup

Install dependencies:
```bash
pip install pycryptodome
```

Generate cryptographic keys:
```bash
python generate_keys.py
```

This creates:
- `shared_key.txt` - 16-byte HMAC shared secret
- `alice_private.pem` - RSA private key
- `alice_public.pem` - RSA public key
- `mactext` - Empty file for HMAC messages
- `sigtext` - Empty file for signed messages

## Usage

### Part 1: HMAC Authentication open 2 terminals one for alice and the second for bob verification
```bash
python alice.py  # Choose 1, enter 18-byte message
python bob.py    # Choose 1, verify message
```

### Part 2: RSA Digital Signature use the 2 terminals used  for part 1
```bash
python alice.py  # Choose 2, enter 18-byte message
python bob.py    # Choose 2, verify signature
```

### Part 3: Performance Testing either one of the both terminal
```bash
python Performance_Test.py  # Enter 7-byte message
```

### Part 4: Hash Collision either one of the both terminal
```bash
python hash_collision.py
```

## Files

- `generate_keys.py` - Generates all cryptographic keys
- `alice.py` - Sender (HMAC & RSA)
- `bob.py` - Verifier
- `Performance_Test.py` - Performance benchmarking
- `hash_collision.py` - Hash collision demonstration
