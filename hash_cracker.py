import hashlib

def hash_cracker(hash_to_crack, hash_function, wordlist):
    hash_function = getattr(hashlib, hash_function)
    with open(wordlist, 'r') as file:
        for line in file:
            word = line.strip()
            if hash_function(word.encode()).hexdigest() == hash_to_crack:
                print(f"Word found: {word}")
                return word
    print("Word not found.")
    return None