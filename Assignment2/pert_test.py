
import time
from statistics import mean
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad

def get_msg_7():
    while True:
        b = input("Enter 7-byte message for performance test: ").encode()
        if len(b) == 7: return b
        print(f"[err] {len(b)} bytes. Please enter exactly 7 bytes.")

def bench_aes(msg, bits):
    key, iv = get_random_bytes(bits//8), get_random_bytes(16)
    enc_t, dec_t = [], [] 

    # Run 100 encryption/decryption cycles and time each
    for _ in range(100):
        c = AES.new(key, AES.MODE_CBC, iv)
        t0 = time.perf_counter(); ct = c.encrypt(pad(msg, 16)); t1 = time.perf_counter()
        d = AES.new(key, AES.MODE_CBC, iv)
        t2 = time.perf_counter(); _ = unpad(d.decrypt(ct), 16); t3 = time.perf_counter()
        enc_t.append(t1-t0); dec_t.append(t3-t2)
    return mean(enc_t), mean(dec_t)

def bench_rsa(msg, bits):
    # Generate RSA key pair for testing
    #print(f"Generating RSA-{bits} key...(this may take a moment for larger sizes)")
    k = RSA.generate(bits)
    enc, dec = PKCS1_OAEP.new(k.publickey()), PKCS1_OAEP.new(k)
    enc_t, dec_t = [], []

    # Run 100 encryption/decryption cycles and time each
    for _ in range(100):
        t0 = time.perf_counter(); ct = enc.encrypt(msg); t1 = time.perf_counter()
        t2 = time.perf_counter(); _  = dec.decrypt(ct);  t3 = time.perf_counter()
        enc_t.append(t1-t0); dec_t.append(t3-t2)
    return mean(enc_t), mean(dec_t)

def main():
    msg = get_msg_7()
    print(f"Using message: {msg!r}")

    # Tes AES with different key sizes (128, 192, 256-bit)
    print("\n === AES avg times (sec) ===")
    for bits in (128, 192, 256):
        e,d = bench_aes(msg, bits)
        print(f"AES-{bits}: enc={e:.6f}, dec={d:.6f}")

        # Test RSA with different key sizes (1024, 2048, 4096-bit)
    print("\n === RSA avg times (sec) ===")
    print("This may talkes a moment for larger sizes!")
    for bits in (1024, 2048, 4096):
        e,d = bench_rsa(msg, bits)
        print(f"RSA-{bits}: enc={e:.6f}, dec={d:.6f}") 

if __name__ == "__main__":
    main()
