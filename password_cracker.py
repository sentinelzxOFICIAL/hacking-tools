import itertools
import hashlib

def password_cracker(hash_to_crack, hash_function, charset, max_length):
    hash_function = getattr(hashlib, hash_function)
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            if hash_function(guess.encode()).hexdigest() == hash_to_crack:
                print(f"Password found: {guess}")
                return guess
    print("Password not found.")
    return None