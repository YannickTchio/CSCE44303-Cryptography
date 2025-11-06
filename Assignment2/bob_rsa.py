from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Needed file name
PRIVKEY, CTEXT = "bob_private.pem", "ctext"

def main():
    # Load private key and read encrypted message
    key = RSA.import_key(open(PRIVKEY, "rb").read())
    cipher = PKCS1_OAEP.new(key)
    ct = open(CTEXT, "rb").read()

    # Decrypt and show result
    print("\nBob: received encrypted message from Alice.")
    print(f"received ciphertext(hex): {ct.hex()}")
    pt = cipher.decrypt(ct)
    print(f"plaintext: {pt.decode(errors='replace')}")
    print("\n")

if __name__ == "__main__":
    main()
