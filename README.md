# 🔍 Basic Recon

Cybersecurity Recon & Password Audit Toolkit

Basic Recon is an open-source cybersecurity toolkit developed in Python to simplify the reconnaissance phase of security assessments. Rather than relying on multiple standalone tools and switching between different terminal sessions, this project provides a centralized command-line interface that combines several essential reconnaissance and password analysis utilities into one lightweight application.



<img width="391" height="305" alt="Screenshot 2026-07-04 171101" src="https://github.com/user-attachments/assets/a25af923-1d75-4b34-9af7-67471955791c" />

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


# 🏗 Project Architecture

```text
BasicRecon
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

# ⚡ Installation

## Clone the repository

```bash
git clone https://github.com/1yusf/BasicRecon.git
```

```bash
cd BasicRecon
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


# 🤝 Contributing

Contributions, improvements, and feature suggestions are always welcome.

Feel free to fork the repository, submit pull requests, or open issues to discuss ideas and enhancements.

---

# ⚖ License

This project is released under the MIT License.

