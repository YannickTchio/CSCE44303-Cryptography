from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# File name we are using
KEYFILE, CTEXT = "shared_key.txt", "ctext"

def get_msg_min18():
    # The user should enter at least 18 bytes 
    while True:
        b = input("Enter message (>=18 bytes): ").encode()
        #if len(b) == 18; return b
        #print(f"[err] You entered {len(b)} bytes. Please enter 18)  I decided to change ==18 to >=18 below
        if len(b) >= 18: return b
        print(f"[err] You entered {len(b)} bytes. Please enter 18 or more.")

def main():
    # Load shared key and generate IV
    key = open(KEYFILE, "rb").read()
    iv  = get_random_bytes(16)
    pt  = get_msg_min18()
    #pt = get_msg_exact18()

    # Encrypt message using AES_CBC 
    ct  = AES.new(key, AES.MODE_CBC, iv).encrypt(pad(pt, 16))
    payload = iv + ct 

    # Save encrypted message and show result
    open(CTEXT, "wb").write(payload)
    print(f"ciphertext(hex): {payload.hex()}")
    print("Alice sent encrypted message to ctext. Bob, can now check it.")
    print("\n")

if __name__ == "__main__":
    main()
