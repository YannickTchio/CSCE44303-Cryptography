import hashlib
import itertools
import time

# All possible and allowed characters
CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%^&*"

# PART 1: UNSALTED
def part1_attack(filename, N):
    print("\n PART 1: UNSALTED ".center(80))
    users = []

    # part1 Read file
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            line = line[1:-1]        
            name, h = line.split(",")
            users.append((name.strip(), h.strip())) 
    
    total = len(CHARS) ** N
    print(f"Total passwords to try: {total}") 
    print(f"Password length N = {N}\n")

    start_time = time.time()

    # Try all passwords posssible for users
    for name, target_hash in users:
        print(f"\nCracking {name} ...")
        found = None

        for pwd_tuple in itertools.product(CHARS, repeat=N):
            pwd = "".join(pwd_tuple)
            h = hashlib.sha256(pwd.encode()).hexdigest()
            if h == target_hash:
                found = pwd
                break

        if found:
            print(f"   the Password = {found}")
        else:
            print("   Not found")

    end_time = time.time()
    print(f"\nTime used: {end_time - start_time:.3f} seconds\n")


#  PART 2: SALTED 
def part2_attack(filename, N):
    print("\n PART 2: SALTED ".center(70))
    users = []

    # Part2 Read file
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()[1:-1]     
            name, salt_hex, h = [x.strip() for x in line.split(",")]
            users.append((name, salt_hex, h)) 

    total = len(CHARS) ** N
    print(f"Total passwords to try: {total}")
    print(f"Password length N = {N}\n")

    start_all = time.time()

    # Try passwords for each user
    for name, salt_hex, target_hash in users:
        print(f"\nCracking {name} (salt = {salt_hex}) ...")
        salt_bytes = bytes.fromhex(salt_hex)
        found = None
        start_user = time.time()

        
        for pwd_tuple in itertools.product(CHARS, repeat=N):
            pwd = "".join(pwd_tuple)
            h = hashlib.sha256(pwd.encode() + salt_bytes).hexdigest()
            if h == target_hash:
                found = pwd
                break

        if found:
            print(f"   The Password = {found} \n")
        else:
            print("   Not found")

        print(f"  Time: {time.time() - start_user:.3f} seconds")

    print(f"\nTotal time: {time.time() - start_all:.3f} seconds\n")



#  The main menu
def main():
    print("\n  Welcome to my HW7 Password Cracker ".center(100))
    print("\n 1 - Part 1 (unsalted)")
    print(" 2 - Part 2 (salted)")

    choice = input("\nChoose option 1 or 2: ").strip()
    filename = input("Enter file name: ").strip()
    try:
        N = int(input("Enter password length N: ").strip()) 
    except ValueError:
        print("Invalid input for password length. Please enter a valid integer. \n")
        return

    if choice == "1":
        part1_attack(filename, N)
    elif choice == "2":
        part2_attack(filename, N)
    else:
        print("Invalid choice option. Please try again between 1 and 2.")

main()
