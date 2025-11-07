import hmac
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import time

# Get message from user with validation loop
while True:
    message = input("\nEnter 7-byte message: ")
    message_bytes = message.encode()
    if len(message_bytes) == 7:
        break
    print(f"Error: Message must be exactly 7 bytes. Your message is {len(message_bytes)} bytes. Try again.")

# Load key for HMAC
with open('shared_key.txt', 'rb') as f:
    key = f.read()

# Load RSA keys
with open('alice_private.pem', 'rb') as f:
    private_key = RSA.import_key(f.read())

with open('alice_public.pem', 'rb') as f:
    public_key = RSA.import_key(f.read())

# Test HMAC generation
start_time = time.time()
for i in range(100):
    mac = hmac.new(key, message_bytes, hashlib.sha256).digest()
end_time = time.time()
hmac_time = (end_time - start_time) / 100


# Generate signature for verification just for my own veriffication not required 
#test_signature = pkcs1_15.new(private_key).sign(SHA256.new(message_bytes))

# Test signature generation
start_time = time.time()
for i in range(100):
    h = SHA256.new(message_bytes)
    signature = pkcs1_15.new(private_key).sign(h)
end_time = time.time()
sign_time = (end_time - start_time) / 100

# Test signature verification
start_time = time.time()
for i in range(100):
    h = SHA256.new(message_bytes)
    try:
        pkcs1_15.new(public_key).verify(h, signature)
    except:
        pass
end_time = time.time()
verify_time = (end_time - start_time) / 100

print(f"Average HMAC generation time: {hmac_time:.6f} seconds")
print(f"Average signature generation time: {sign_time:.6f} seconds")
print(f"Average signature verification time: {verify_time:.6f} seconds")
print("\n")
