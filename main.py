import os
import time
from colorama import Fore, init

from modules.port_scanner import port_scanner
from modules.network_discovery import network_discovery
from modules.password_checker import password_checker
from modules.subdomain_enum import subdomain_enum
from modules.email_scraper import email_scraper
from modules.password_audit import password_audit

init(autoreset=True)


def clear_screen():
    os.system("clear")


def banner():
    print(Fore.CYAN + """
╔═══════════════════════════════════════════════════╗
║                                                   ║
║   ██████╗  █████╗ ███████╗██╗ ██████╗             ║
║   ██╔══██╗██╔══██╗██╔════╝██║██╔════╝             ║
║   ██████╔╝███████║███████╗██║██║                  ║
║   ██╔══██╗██╔══██║╚════██║██║██║                  ║
║   ██████╔╝██║  ██║███████║██║╚██████╗             ║
║   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝             ║
║                                                   ║
║   ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗     ║
║   ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║     ║
║   ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║     ║
║   ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║     ║
║   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║     ║
║   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝     ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
""" + Fore.LIGHTYELLOW_EX + "                                        by 1yusf\n")


def loading(message):
    """Simple loading animation"""
    print(Fore.CYAN + message, end='', flush=True)

    for _ in range(3):
        time.sleep(0.5)
        print(Fore.CYAN + ".", end='', flush=True)

    print()


def menu():
    print(Fore.GREEN + "─ Menu ──────────────────────────────")
    print(Fore.GREEN + " 1. Port Scanner")
    print(Fore.GREEN + " 2. Network Scanner")
    print(Fore.GREEN + " 3. Subdomain Scanner")
    print(Fore.GREEN + " 4. Email Scraper")
    print(Fore.GREEN + " 5. Hash Cracker (MD5/SHA1/SHA256)")
    print(Fore.GREEN + " 6. Password Checker")
    print(Fore.GREEN + " 7. Exit")
    print(Fore.GREEN + "─────────────────────────────────────")


def main():
    while True:
        clear_screen()
        banner()
        menu()

        choice = input(Fore.CYAN + "\nSelect Option: ")

        if choice == "1":
            port_scanner()

        elif choice == "2":
            network_discovery()

        elif choice == "3":
            subdomain_enum()

        elif choice == "4":
            email_scraper()

        elif choice == "5":
            password_audit()

        elif choice == "6":
            password_checker()

        elif choice == "7":
            print(Fore.RED + "\nGoodbye!")
            break

        else:
            input(Fore.RED + "Invalid Option. Press Enter...")


if __name__ == "__main__":
    main()
