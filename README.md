
# Wi-Fi Password Retriever (Windows)

This Python script retrieves saved Wi-Fi passwords from a Windows machine. It uses the `os` module to run system commands that access stored wireless network profiles and extract their corresponding passwords in clear text.

---

## What It Does

The script automates the following steps:

1. Runs `netsh wlan show profiles` to list all saved Wi-Fi profiles.
2. Extracts the names of these profiles from the command output.
3. Runs `netsh wlan show profile name="PROFILE" key=clear` for each profile.
4. Extracts and prints the Wi-Fi password if available.

---

## Example Output

```
Wi-Fi: HomeNetwork, Password: mysecret123
Wi-Fi: CoffeeShopWiFi, Password: freewifi456
```

---

## Requirements

- Python 3  
- Windows OS  
- The script must be run with appropriate permissions (some networks may require admin access to view password data)

---

## Installation

1. Save the script as `wifi_passwords.py`  
2. No additional packages are needed — it uses built-in modules.

---

## Running the Script

Open Command Prompt or a terminal and run:

```bash
python wifi_passwords.py
```

The script will display a list of saved Wi-Fi networks and their associated passwords, if available.

---
