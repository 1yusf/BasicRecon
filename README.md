# 🔍 Basic Recon

Advanced Cybersecurity Recon & Password Audit Toolkit


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



# 📸 Screenshots



---

# ⚡ Installation

## Clone the repository

```bash
git clone https://github.com/1yusf/BasicRecon.git
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


# 🤝 Contributing

Contributions, improvements, and feature suggestions are always welcome.

Feel free to fork the repository, submit pull requests, or open issues to discuss ideas and enhancements.

---

# ⚖ License

This project is released under the MIT License.

