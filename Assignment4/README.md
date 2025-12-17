Assignment 4 – Password Cracker (CSCE 44303)

This project implements a Python based dictionary attack tool for cracking unsalted and salted SHA-256 password hashes, as required for Assignments 4 in CSCE 44303 (Cryptography). The goal of this assignment was to demonstrate how salting passwords increases resistance to dictionary attacks by comparing attack behavior and execution time.

The program supports two modes:

Part 1 (Unsalted): Cracks passwords stored as SHA256(password)

Part 2 (Salted): Cracks passwords stored as SHA256(password || salt), where the salt is a 32-bit random value

The program generates all possible passwords of length N using the allowed character set and compares their SHA-256 hashes against those in the input file. When a match is found, the plaintext password is recovered and displayed. The total execution time is measured and printed.

How I Tested My Work
Part 1 – Unsalted Passwords

The program was executed using the provided test file part1_test.txt with password length N = 3.

python3 password_cracker.py
Choose option 1 or 2: 1
Enter file name: part1_test.txt
Enter password length N: 3


Result:

All five passwords were successfully recovered

Total password space tested: 314,432

Execution time: 0.344 seconds

Recovered passwords:

user1 → fZ0

user2 → #Hr

user3 → mpj

user4 → Y&m

user5 → ulX

Part 2 – Salted Passwords

The program was then tested using the salted password file part2_test.txt with the same password length N = 3.

python3 password_cracker.py
Choose option 1 or 2: 2
Enter file name: part2_test.txt
Enter password length N: 3


Result:

All salted passwords were successfully recovered

Each password was cracked using its corresponding salt

Total execution time: 0.262 seconds

Recovered passwords:

user1 (salt = 2d94f04d) → j$D

user2 (salt = eefa0a75) → 2zP

user3 (salt = 56edf6f9) → uEL

user4 (salt = ad9a7b1e) → dWa

user5 (salt = dc3180e9) → RIV

Summary

This project successfully demonstrates the effectiveness of dictionary attacks against unsalted password hashes and shows how salting alters the attack process. The program correctly recovers all passwords in both test cases and reports accurate execution times, meeting all assignment requirements.
