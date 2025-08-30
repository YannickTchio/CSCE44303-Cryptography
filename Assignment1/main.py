from caesar_cipher import encrypt_text, decrypt_text, brute_force_attack

def get_valid_key(prompt):
    #Keep asking for a valid key until we get one
    while True:
        key_input = input(prompt).strip()
        try:
            key = int(key_input)
            if 1 <= key <= 25:
                return key
            else:
                print("The Key must be a positive integer number between 1 and 25!")
        except ValueError:
            print("That is not a valid number! Please enter a number between 1 and 25!")

def main():
   
    print("\n\n")
    print ("Welcome to my Caesar Cipher Program!" .center(80))
    print("I made this for my first homework assignment for CSCE 44303 Cryptography" .center(80))
    
    
    while True:
    
        print("")
        print("What would you like to do?: ")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Try to crack a cipher (Brute-force attack)")
        print("4. Quit or Exit")
        
        choice = input("\nPlease enter your choice number (1-4): ").strip()
        
        
        if choice == '1':
            # Encryption from Part 1
            plaintext = input("Please write the message that you want to encrypt: ").strip()
            
            if not plaintext:
                print("Please you need to enter a message to encrypt!")
                continue

            # Keep asking until we get a valid key
            key = get_valid_key("What key do you want to use? (1-25): ")
            
            # Message encryption
            ciphertext = encrypt_text(plaintext, key)
            print("Your Ciphertext(encrypted message) is:", ciphertext)
        
        elif choice == '2':
            # Decryption from Part 1
            ciphertext = input("Enter ciphertext(encrypted) message: ").strip()
            
            if not ciphertext:
                print("Please enter a message to decrypt!")
                continue
            
            # Keep asking until we get a valid key
            key = get_valid_key("What key do you want to use? (1-25): ")
            
            # Message decryption
            plaintext = decrypt_text(ciphertext, key)
            print("Your Plaintext(decrypted message) is:", plaintext)
        
        elif choice == '3':
            # Brute-force attack from part 2
            ciphertext = input("Enter the ciphertext message that you want to crack: ").strip()
            
            if not ciphertext:
                print("Please you need to enter an encrypted message to crack!")
                continue
                
            vocab_file = input("Enter vocabulary file name (like sample.txt): ").strip()
            
            if not vocab_file:
                print("Please enter a vocabulary file name!")
                continue
                
            print("I am trying to crack the cipher and this might take a few seconds")
            key, plaintext = brute_force_attack(ciphertext, vocab_file)
            
            if key is not None:
                print("Successsssssss! I cracked it!")
                print("The secret Key is:", key)
                print("The Original Plaintext Message is:", plaintext)
            else:
                print("Sorry, I could not crack the cipher. No valid key found or maybe the words aren't in the file.")
        
        elif choice == '4':
            print("Thank you for trying my first Caesar Cipher program! I hope you enjoyed it.  I plan to keep learning and improving it. Goodbye!")
            break
        
        else:
            print("Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

    