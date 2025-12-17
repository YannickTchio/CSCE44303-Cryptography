                    <b>Assignment 4: Password Cracking & Salted Hash Analysis</b>
Project Overview

This project implements a dictionary-based password cracking tool to analyze the security differences between unsalted and salted password hashing. The program simulates real-world password storage systems using SHA-256 and demonstrates how the use of salts impacts the effectiveness and performance of dictionary attacks.

The program supports two attack modes:

Unsalted password cracking

Salted password cracking

For each mode, the program attempts to recover plaintext passwords and reports the total execution time required to complete the attack.

Features
Part 1: Unsalted Password Cracking

Cracks passwords stored as SHA256(password)

Performs a dictionary attack using all possible passwords of length N

Uses SHA-256 hashing

Recovers and prints all plaintext passwords

Measures total attack time

Part 2: Salted Password Cracking

Cracks passwords stored as SHA256(password || salt)

Uses a 32-bit random salt for each user

Demonstrates resistance to precomputed dictionary attacks

Recovers and prints all plaintext passwords

Measures total attack time

Technologies Used

Language: Python 3

Libraries:

hashlib — SHA-256 hashing

time — execution time measurement

itertools — password generation

Project Structure
Assignment_4/
├── password_cracker.py     # Main password cracking program
├── part1_test.txt          # Unsalted password test file
├── part2_test.txt          # Salted password test file
├── Plaintext_passwords.txt # Password dictionary
└── README.md               # This file

Usage
Run the Program
python3 password_cracker.py


The program will prompt the user to select an attack mode:

1 - Part 1 (unsalted)
2 - Part 2 (salted)


The user then provides:

Input filename

Password length N

Testing
Part 1 – Unsalted Passwords

The program was tested using part1_test.txt with password length N = 3.

Total passwords tested: 314,432

All passwords successfully recovered

Total execution time: 0.344 seconds

Recovered passwords:

user1 → fZ0

user2 → #Hr

user3 → mpj

user4 → Y&m

user5 → ulX

Part 2 – Salted Passwords

The program was tested using part2_test.txt with password length N = 3.

Total passwords tested: 314,432

All salted passwords successfully recovered

Total execution time: 0.262 seconds

Recovered passwords:

user1 → j$D

user2 → 2zP

user3 → uEL

user4 → dWa

user5 → RIV

Example Output
PART 1: UNSALTED
Total passwords to try: 314432
Time used: 0.344 seconds

PART 2: SALTED
Total passwords to try: 314432
Total time: 0.262 seconds

Assignment Requirements Met

✅ Dictionary attack implementation

✅ SHA-256 hashing

✅ Unsalted and salted password cracking

✅ Execution time measurement

✅ Command-line interaction

✅ Grader-provided file support

Security Insights

Unsalted password hashes are vulnerable to fast dictionary attacks

Salting passwords prevents precomputed attacks and increases attack complexity

Even small password lengths result in large search spaces

Salting improves security without significant system overhead

References

Python hashlib Documentation

CSCE 44303 Cryptography Course Materials
