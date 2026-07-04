import os
import hashlib
from colorama import Fore


DEFAULT_WORDLIST = "wordlists/common.txt"


def crack_hash(target_hash, wordlist_path):
    try:
        with open(wordlist_path, "r", encoding="latin-1") as file:
            for word in file:
                word = word.strip()

                if not word:
                    continue

                md5_hash = hashlib.md5(word.encode()).hexdigest()
                if md5_hash == target_hash:
                    return word, "MD5"

                sha1_hash = hashlib.sha1(word.encode()).hexdigest()
                if sha1_hash == target_hash:
                    return word, "SHA1"

                sha256_hash = hashlib.sha256(word.encode()).hexdigest()
                if sha256_hash == target_hash:
                    return word, "SHA256"

        return None, None

    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return None, None


def password_audit():
    while True:
        os.system("clear")

        print(Fore.CYAN + "BRUTEFORCE")
        print(Fore.CYAN + "=" * 40)

        target_hash = input("Enter MD5/SHA1/SHA256 Hash (99 = Back): ")

        if target_hash == "99":
            return

        print("\n1. Use Default Wordlist")
        print("2. Use Custom Wordlist")

        choice = input("\nSelect Option: ")

        if choice == "1":
            wordlist = DEFAULT_WORDLIST

        elif choice == "2":
            wordlist = input("Enter Wordlist Path: ")

        else:
            print(Fore.RED + "Invalid Option")
            input("Press Enter...")
            continue

        print(Fore.YELLOW + "\nCracking...\n")

        result, hash_type = crack_hash(target_hash, wordlist)

        if result:
            print(Fore.GREEN + f"Password Found: {result}")
            print(Fore.CYAN + f"Hash Type: {hash_type}")
        else:
            print(Fore.RED + "Password not found in wordlist")

        again = input("\nBruteForce another password? (y/n): ").lower()

        if again != "y":
            break
