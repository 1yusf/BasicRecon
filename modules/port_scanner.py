import os
import nmap
from colorama import Fore


scanner = nmap.PortScanner()


def port_scanner():
    while True:
        os.system("clear")

        print(Fore.CYAN + "PORT SCANNER")
        print(Fore.CYAN + "=" * 40)

        target = input("Enter Target IP or Domain (99 = Back): ")

        if target == "99":
            return

        try:
            scanner.scan(target, arguments='-sV')

            for host in scanner.all_hosts():
                print(Fore.GREEN + f"\nHost: {host}")
                print(Fore.YELLOW + f"State: {scanner[host].state()}")

                for proto in scanner[host].all_protocols():
                    print(Fore.CYAN + f"\nProtocol: {proto}")

                    ports = scanner[host][proto].keys()

                    for port in ports:
                        service = scanner[host][proto][port]['name']
                        state = scanner[host][proto][port]['state']

                        if state == 'open':
                            print(Fore.WHITE + f"Port: {port} | Service: {service} | State: {state}")

        except Exception as e:
            print(Fore.RED + f"Error: {e}")

        again = input("\nPerform another scan? (y/n): ").lower()

        if again != 'y':
            break
