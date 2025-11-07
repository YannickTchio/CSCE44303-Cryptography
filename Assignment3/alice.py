import hmac
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15 
from Crypto.Hash import SHA256

def part1_alice():
    # Read shared key from file
    with open('shared_key.txt', 'rb') as f:
        key = f.read()
    
    # Get message: needs to be 18 bytes exactly
    while True:
        message = input("Enter 18-byte message: ")
        message_bytes = message.encode()
        if len(message_bytes) == 18:
            break
        print(f"Error: Message must be exactly 18 bytes. Your message is {len(message_bytes)} bytes. Try again.")
    
    # Make HMAC
    mac = hmac.new(key, message_bytes, hashlib.sha256).digest()
    
    # Write to file
    with open('mactext', 'wb') as f:
        f.write(message_bytes)
        f.write(b'\n---HMAC---\n')
        f.write(mac)
    
    print("\nHMAC generated:", mac.hex())
    print("\n")

def part2_alice():
    # Load private key
    with open('alice_private.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())
    
    # Get message from user with validation
    while True:
        message = input("Enter 18-byte message: ")
        message_bytes = message.encode()
        if len(message_bytes) == 18:
            break
        print(f"Error: Message must be exactly 18 bytes. Your message is {len(message_bytes)} bytes. Try again.")
    
    # Sign message 
    h = SHA256.new(message_bytes) 
    signature = pkcs1_15.new(private_key).sign(h) 
    
    # Write to file 
    with open('sigtext', 'wb') as f: 
        f.write(message_bytes)
        f.write(b'\n---SIGNATURE---\n')
        f.write(signature)
    
    print("\nSignature generated:", signature.hex())
    print("\n")

if __name__ == "__main__":
    print("\n")
    print("Choose part:")
    print("1. HMAC (Part 1)")
    print("2. Digital Signature (Part 2)")
    
    while True:
        choice = input("Enter choice (1 or 2): ")
        if choice == "1":
            part1_alice()
            break
        elif choice == "2":
            part2_alice()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
