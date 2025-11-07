import hashlib
import os

def hash_function(message):
    # Get first 8 bits of SHA-256
    full_hash = hashlib.sha256(message).digest()
    first_byte = full_hash[0]
    return first_byte

def find_collision():
    tried_hashes = {}
    num_trials = 0
    
    while True:
        # Generate random message
        message = os.urandom(16)
        num_trials += 1
        
        # Compute hash
        hash_value = hash_function(message)
        
        # Check if we've seen this hash before
        if hash_value in tried_hashes:
            # Found collision
            return num_trials, tried_hashes[hash_value], message, hash_value
        
        # Store this hash
        tried_hashes[hash_value] = message

# Part 4(a) - Find one collision
print("\nPart 4(a): Finding a collision...")
trials, msg1, msg2, hash_val = find_collision()
print(f"Number of trials: {trials}")
print(f"Message 1: {msg1.hex()}")
print(f"Message 2: {msg2.hex()}")
print(f"Hash value: {hash_val:02x}")
print("\n")

# Part 4(b) - Find average over 20 iterations
print("Part 4(b): Running 20 iterations...")
total_trials = 0
for i in range(20):
    trials, _, _, _ = find_collision()
    total_trials += trials

average_trials = total_trials / 20
print(f"Average number of trials needed to find a collision: {average_trials:.2f}")
print("\n")
