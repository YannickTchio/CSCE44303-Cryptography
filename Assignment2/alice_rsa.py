
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Needeed file name
PUBKEY, CTEXT = "bob_public.pem", "ctext"
RSA2048_OAEP_MAX = 214  # max plaintext bytes for 2048-bit RSA OAEP (SHA-1)

def get_msg_min18():
    while True:
        b = input("Enter message (>=18 bytes): ").encode()
        #if len(b) == 18: return b
        #print(f"[err] You entered {len(b)} bytes. Please enter 18)
        if len(b) >= 18: return b
        print(f"[err] You entered {len(b)} bytes. Please enter 18 or more.")

def main():
    # Load Bob's public key and get message
    key = RSA.import_key(open(PUBKEY, "rb").read())
    cipher = PKCS1_OAEP.new(key)
    pt = get_msg_min18() 
    #pt = get_msg_exact18()

    # Check message length 
    if len(pt) > RSA2048_OAEP_MAX:
        print(f"Error: message too long for RSA-2048 OAEP (max {RSA2048_OAEP_MAX} bytes).")
        return 
    
    # Encrypt and save result
    ct = cipher.encrypt(pt)
    open(CTEXT, "wb").write(ct)
    print(f"ciphertext(hex): {ct.hex()}")
    print("Alice sent encrypted message to ctext. Bob, please check it.")
    print("\n")

if __name__ == "__main__":
    main()
