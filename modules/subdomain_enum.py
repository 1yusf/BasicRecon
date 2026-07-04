import os
import requests
from colorama import Fore


def subdomain_enum():
    while True:
        os.system("clear")

        print(Fore.CYAN + "SUBDOMAINS CHECKER")
        print(Fore.CYAN + "=" * 40)

        domain = input("Enter Domain (99 = Back): ")

        if domain == "99":
            return

        print(Fore.YELLOW + "\nScanning... (may take time)\n")

        url = f"https://crt.sh/?q=%25.{domain}&output=json"

        found = set()
        success = False

        for attempt in range(3):
            try:
                response = requests.get(url, timeout=120)

                if response.status_code == 200:
                    data = response.json()

                    for entry in data:
                        name = entry['name_value']

                        for sub in name.split('\n'):
                            sub = sub.strip()

                            if domain in sub and '*' not in sub and ' ' not in sub:
                                found.add(sub)

                    success = True
                    break

                else:
                    print(Fore.YELLOW + f"Attempt {attempt+1}/3: Server busy ({response.status_code}), retrying...")

            except requests.exceptions.Timeout:
                print(Fore.YELLOW + f"Attempt {attempt+1}/3: Timeout, retrying...")

            except Exception:
                print(Fore.YELLOW + f"Attempt {attempt+1}/3: Error, retrying...")

        if success:
            print(Fore.GREEN + "\nDiscovered Subdomains:\n")

            for subdomain in sorted(found):
                print(Fore.WHITE + subdomain)

            print(Fore.YELLOW + f"\nTotal found: {len(found)}")

        else:
            print(Fore.RED + "\nFailed to fetch data from crt.sh")
            print(Fore.YELLOW + "Try:")
            print("- Checking your internet connection")
            print("- Trying again in a few minutes")
            print("- The domain may not have subdomains")

        again = input("\nScan another domain? (y/n): ").lower()

        if again != "y":
            break
