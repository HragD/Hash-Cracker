import hashlib

def hash_crack(hash_to_crack, hash_type, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                if hash_type == 'md5':
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == 'sha1':
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == 'sha256':
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print("❌ Unsupported hash type.")
                    return

                if hashed_word == hash_to_crack:
                    print(f'✅ Password found: {word}')
                    return

        print("❌ Password not found in the wordlist.")
    except FileNotFoundError:
        print("❌ Wordlist file not found.")

if __name__ == "__main__":
    print("🔓 HASH CRACKER 🔓")
    hash_to_crack = input("Enter the hash to crack: ").strip()
    hash_type = input("Enter the hash type (md5/sha1/sha256): ").strip().lower()
    wordlist_path = input("Enter path to wordlist (e.g., rockyou.txt): ").strip()

    hash_crack(hash_to_crack, hash_type, wordlist_path)
