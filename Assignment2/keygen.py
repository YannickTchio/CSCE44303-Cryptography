from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA

# Generate AES-128 key for symmetric encryption (part1)
aes_key = get_random_bytes(16)
with open("shared_key.txt", "wb") as f: 
    f.write(aes_key)

# Generate RSA-2048 key pair for asymmetric encryption (part2)
rsa = RSA.generate(2048)
with open("bob_private.pem", "wb") as f: 
    f.write(rsa.export_key())
with open("bob_public.pem", "wb")  as f: 
    f.write(rsa.publickey().export_key())


# Create the empty ctext for both part 1 & 2 communication
open("ctext", "wb").close()

print("\n")
print("Making keys for the crypto homework 3!" .center (80))
print("Made AES key and saved to shared_key.txt (shared key for Alice & Bob).")
print("Made RSA keys:")
print("  bob_private.pem - Bob's secret key")
print("  bob_public.pem  - Alice uses this")
print("\nWell done, All key create! Now you can run alice_aes.py / bob_aes.py or alice_rsa.py / bob_rsa.py.")
print("\n")
