import os
import subprocess
import socket
import uuid
from colorama import Fore


def get_active_interface():
    """Detect the active network interface (eth0, wlan0, etc.)"""
    try:
        # Try to get default interface using ip command
        result = subprocess.run(['ip', 'route', 'default'], capture_output=True, text=True)
        if 'dev' in result.stdout:
            interface = result.stdout.split('dev')[1].split()[0].strip()
            return interface
    except:
        pass
    
    # Fallback: check common interfaces
    for iface in ['wlan0', 'eth0', 'ens33', 'enp0s3']:
        try:
            result = subprocess.run(['ip', 'link', 'show', iface], capture_output=True)
            if result.returncode == 0:
                return iface
        except:
            continue
    
    return 'eth0'


def network_discovery():
    while True:
        os.system("clear")

        print(Fore.CYAN + "NETWORK DISCOVERY")
        print(Fore.CYAN + "=" * 40)
        
        choice = input("Press Enter to start or type 99 to go back: ")

        if choice == "99":
            return

        interface = get_active_interface()
        print(Fore.YELLOW + f"Using interface: {interface}\n")

        try:
            command = [
                "sudo",
                "bettercap",
                "-iface", interface,
                "-eval",
                "net.probe on; net.recon on; net.show; sleep 20; quit"
            ]

            result = subprocess.run(command, capture_output=True, text=True, errors='ignore')

            print(Fore.GREEN + result.stdout)

        except Exception as e:
            print(Fore.RED + f"Error: {e}")
            print(Fore.YELLOW + "Make sure bettercap is installed: sudo apt install bettercap")

        again = input("\nRun network discovery again? (y/n): ").lower()

        if again != 'y':
            break
