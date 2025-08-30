def encrypt_text(text, key): 
    result = ""
    
    # I'm going through each letter one by one
    for i in range(len(text)):  
        char = text[i]
        if char.isalpha():
            if char.isupper():
                # This math took me a while to figure out
                position = ord(char) - ord('A')
                new_position = (position + key) % 26  
                new_char = chr(new_position + ord('A'))
            else:
                position = ord(char) - ord('a')
                new_position = (position + key) % 26  
                new_char = chr(new_position + ord('a'))
            result += new_char
        else:
            result += char
    
    return result

def decrypt_text(text, key):
    # For decryption I just use negative key, this should work I think
    return encrypt_text(text, -key)

def load_vocabulary(filename):
    words = set()  
    
    try:
        f = open(filename, 'r')  
        content = f.read()
        f.close()
        
        # I'll convert everything to lowercase first
        content = content.lower()
        
        # Now I need to get all the words
        current_word = ""
        for char in content:
            if char.isalpha():
                current_word = current_word + char
            else:
                if len(current_word) > 0:  
                    words.add(current_word)  
                    current_word = ""
        
        # Don't forget the last word!
        if len(current_word) > 0:
            words.add(current_word)
        
        return words
    
    except:
        print("Oops! I can't find that file")  
        return set()  

def brute_force_attack(ciphertext, vocab_file):
    vocab_words = load_vocabulary(vocab_file)
    if len(vocab_words) == 0:  
        return None, None
    
    print("I found", len(vocab_words), "words in the file")
    
    # Let me try every possible key from 1 to 25
    for key in range(1, 26):
        decrypted_message = decrypt_text(ciphertext, key)
        
        # Now I need to split this into individual words like i did in load vocabulary
        words_list = []
        current_word = ""

        # Go through each character in the decrypted message 
        for char in decrypted_message.lower():  
            if char.isalpha():  
                current_word = current_word + char
            else:  
                if len(current_word) > 0:
                    words_list.append(current_word)
                    current_word = ""
        
        # Don't forget the last word if theere is one
        if len(current_word) > 0:
            words_list.append(current_word)
        
        # Check if all words are in vocabulary
        found_all = True
        for word in words_list:
            if word not in vocab_words:  
                found_all = False
                break
        
        # If we found all words and there's at least one word, we successed!
        if len(words_list) > 0 and found_all:
            return key, decrypted_message

    return None, None


