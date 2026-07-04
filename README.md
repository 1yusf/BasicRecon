# 🔍 Basic Recon

Advanced Cybersecurity Recon & Password Audit Toolkit


---

# ✨ Features

## 🌐 Network Discovery

Discover active devices connected to your local network using Bettercap.

**Capabilities**

* Automatic network interface detection
* Local network host discovery
* Active device enumeration
* Simple Bettercap integration

---

## 🔎 Port Scanner

Perform service enumeration using Nmap.

**Capabilities**

* Scan IP addresses and domain names
* Detect open ports
* Identify running services
* Display host status
* Protocol detection

---

## 🌍 Subdomain Enumeration

Enumerate publicly available subdomains using Certificate Transparency logs from crt.sh.

**Capabilities**

* Retrieve historical subdomains
* Remove duplicate results
* Automatic retry handling
* Quick reconnaissance of an organization's attack surface

---

## 📧 Email Scraper

Extract publicly exposed email addresses from websites.

**Capabilities**

* Website crawling
* Internal link discovery
* Email extraction using Regular Expressions
* Duplicate filtering
* Multi-page scanning

---

## 🔐 Password Hash Cracker

Perform dictionary attacks against password hashes.

**Supported Algorithms**

* MD5
* SHA-1
* SHA-256

**Capabilities**

* Default wordlist support
* Custom wordlist support
* Automatic hash identification after successful cracking

---

## 🛡 Password Strength Analyzer

Evaluate password strength using Dropbox's zxcvbn algorithm.

**Capabilities**

* Password complexity scoring
* Crack time estimation
* Strength classification
* User-friendly output

---

# 🏗 Project Architecture

```text
Basic-Recon
│
├── main.py
│
├── modules
│   ├── port_scanner.py
│   ├── network_discovery.py
│   ├── subdomain_enum.py
│   ├── email_scraper.py
│   ├── password_audit.py
│   └── password_checker.py
│
├── wordlists
│   └── common.txt
│
└── requirements.txt
```

Each module is designed to operate independently while being managed through a centralized CLI menu, making future expansion straightforward.

---

# 🛠 Technologies Used

* Python 3
* Nmap
* Bettercap
* python-nmap
* Requests
* BeautifulSoup4
* Colorama
* zxcvbn
* hashlib
* Regular Expressions (Regex)
* urllib

---

# 📸 Screenshots



---

# ⚡ Installation

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Basic-Recon.git
```

```bash
cd Basic-Recon
```

---

## Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## Install Nmap

### Debian / Ubuntu / Kali

```bash
sudo apt update
sudo apt install nmap
```

---

## Install Bettercap

```bash
sudo apt install bettercap
```

---

# ▶ Running the Project

```bash
python3 main.py
```

Some modules (such as Network Discovery) require elevated privileges.

Run with:

```bash
sudo python3 main.py
```

---

# 📋 Included Modules

| Module                | Description                                       |
| --------------------- | ------------------------------------------------- |
| Port Scanner          | Service and port enumeration using Nmap           |
| Network Discovery     | Local network discovery using Bettercap           |
| Subdomain Enumeration | Certificate Transparency enumeration              |
| Email Scraper         | Website email harvesting                          |
| Hash Cracker          | Dictionary attacks against MD5, SHA-1 and SHA-256 |
| Password Analyzer     | Password strength estimation using zxcvbn         |

---

# 🎯 Purpose

Basic Recon was developed as a practical cybersecurity project to demonstrate the integration of multiple reconnaissance techniques into a modular Python application.

The project emphasizes:

* Modular software design
* Linux command-line development
* Security tool integration
* Network reconnaissance
* Information gathering
* Password auditing
* Automation of common security tasks

It also serves as a foundation for future enhancements, allowing additional modules and functionality to be integrated with minimal changes to the existing architecture.

---

# 🚀 Future Improvements

* Export scan results to JSON, CSV and HTML
* Multi-threaded scanning
* DNS enumeration
* WHOIS lookup
* Banner grabbing
* HTTP header analysis
* SSL certificate inspection
* Vulnerability detection
* OS fingerprinting
* Report generation
* Logging system
* Plugin support

---

# 🤝 Contributing

Contributions, improvements, and feature suggestions are always welcome.

Feel free to fork the repository, submit pull requests, or open issues to discuss ideas and enhancements.

---

# ⚖ License

This project is released under the MIT License.

---

# ⚠ Disclaimer

This software is provided for **educational purposes and authorized security assessments only**.

The author assumes **no responsibility** for misuse, unauthorized access, or any damage caused by this software.

Always obtain explicit permission before performing reconnaissance or security testing against any target system or network.


python3 main.py

## Ethical Notice

This tool is strictly for educational purposes and authorized testing only.
