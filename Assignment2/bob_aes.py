
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Same file uses by alice
KEYFILE, CTEXT = "shared_key.txt", "ctext"

def main():
    # Load shared key and read ebcrypted message
    key = open(KEYFILE, "rb").read()
    data = open(CTEXT, "rb").read()
    if len(data) < 16: print("[err] ctext too short"); return 

    # Split message and decrypt
    iv, ct = data[:16], data[16:]
    print("\n Bob: received encrypted message from Alice.")
    print(f"received ciphertext(hex): {data.hex()}")
    pt = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ct), 16) 
    print(f"plaintext: {pt.decode(errors='replace')}")
    print("\n")

if __name__ == "__main__":
    main()
