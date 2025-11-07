from Crypto.PublicKey import RSA
import os

# Generate 16-byte shared key for HMAC
shared_key = os.urandom(16)
with open('shared_key.txt', 'wb') as f:
    f.write(shared_key)
print("\nGenerated shared_key.txt")

# Generate RSA 2048-bit key pair
key = RSA.generate(2048)

# Save private key
with open('alice_private.pem', 'wb') as f:
    f.write(key.export_key())
print("Generated alice_private.pem done")

# Save public key
with open('alice_public.pem', 'wb') as f:
    f.write(key.publickey().export_key())
print("Generated alice_public.pem done")

# Create 2 empty files
open('mactext', 'wb').close()
print("Created empty mactext")

open('sigtext', 'wb').close()
print("Created empty sigtext")

print("\nAll generate key and files complete!")
print("\n")
