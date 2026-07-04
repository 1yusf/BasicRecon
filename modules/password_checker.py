import os
from colorama import Fore
from zxcvbn import zxcvbn


def password_checker():
    while True:
        os.system("clear")

        print(Fore.CYAN + "PASSWORD STRENGTH ANALYZER")
        print(Fore.CYAN + "=" * 40)

        password = input("Enter Password (99 = Back): ")

        if password == "99":
            return

        result = zxcvbn(password)

        score = result['score']
        crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']

        levels = {
            0: "Very Weak",
            1: "Weak",
            2: "Medium",
            3: "Strong",
            4: "Very Strong"
        }

        print(Fore.GREEN + f"\nStrength: {levels[score]}")
        print(Fore.YELLOW + f"Estimated Crack Time: {crack_time}")

        again = input("\nCheck another password? (y/n): ").lower()

        if again != 'y':
            break
