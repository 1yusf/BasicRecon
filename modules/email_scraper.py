import os
import re
import requests
from bs4 import BeautifulSoup
from colorama import Fore
from urllib.parse import urljoin, urlparse


EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


def email_scraper():
    while True:
        os.system("clear")

        print(Fore.CYAN + "EMAIL SCRAPER")
        print(Fore.CYAN + "=" * 40)

        url = input("Enter Website URL (99 = Back): ")

        if url == "99":
            return

        if not url.startswith("http"):
            url = "https://" + url

        domain = urlparse(url).netloc

        try:
            print(Fore.YELLOW + f"\nScanning {domain}...\n")

            emails = set()
            queue = [url]
            visited = set()
            max_pages = 20
            page_count = 0

            while queue and page_count < max_pages:
                current_url = queue.pop(0)

                if current_url in visited:
                    continue

                visited.add(current_url)
                page_count += 1
                print(Fore.CYAN + f"Page {page_count}/{max_pages}: {current_url}")

                try:
                    response = requests.get(current_url, timeout=5)
                    soup = BeautifulSoup(response.text, "html.parser")

                    found = re.findall(EMAIL_REGEX, soup.text)

                    for email in found:
                        if not any(ext in email.lower() for ext in [".png", ".jpg", ".gif", ".bmp"]):
                            emails.add(email)

                    for tag in soup.find_all("a", href=True):
                        href = tag["href"]
                        full_url = urljoin(current_url, href)
                        parsed = urlparse(full_url)

                        if parsed.netloc == domain and full_url not in visited:
                            queue.append(full_url)

                except:
                    continue

            print(Fore.GREEN + "\nEmails Found:\n")

            if emails:
                for email in sorted(emails):
                    print(Fore.WHITE + email)

                print(Fore.YELLOW + f"\nTotal: {len(emails)}")

            else:
                print(Fore.RED + "No emails found")

        except Exception as e:
            print(Fore.RED + f"Error: {e}")

        again = input("\nScrape another website? (y/n): ").lower()

        if again != "y":
            break
