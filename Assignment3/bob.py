import hmac
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def part1_bob():
    # Read shared key from file
    with open('shared_key.txt', 'rb') as f:
        key = f.read()
    
    # Read message and MAC from file
    with open('mactext', 'rb') as f:
        content = f.read()
        parts = content.split(b'\n---HMAC---\n')
        message = parts[0]
        received_mac = parts[1] 
    
    # Generate HMAC 
    computed_mac = hmac.new(key, message, hashlib.sha256).digest()
    
    # Verify 
    if hmac.compare_digest(computed_mac, received_mac): 
        print("\nVerification succeeded")
        print("\n")
    else:
        print("\nVerification failed")
        print("\n")

def part2_bob(): 
    # Load Alice's public key
    with open('alice_public.pem', 'rb') as f:
        public_key = RSA.import_key(f.read()) 
    
    # Read message and signature from file 
    with open('sigtext', 'rb') as f:
        content = f.read()
        parts = content.split(b'\n---SIGNATURE---\n')
        message = parts[0]
        signature = parts[1]
    
    # Verify signature
    h = SHA256.new(message)
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        print("\nVerification succeeded")
        print("\n")
    except:
        print("\nVerification failed")
        print("\n")

if __name__ == "__main__": 
    print("\n")
    print("Choose part:")
    print("1. HMAC (Part 1)")
    print("2. Digital Signature (Part 2)")
    
    while True:
        choice = input("Enter choice (1 or 2): ")
        if choice == "1":
            part1_bob()
            break
        elif choice == "2":
            part2_bob()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
          
