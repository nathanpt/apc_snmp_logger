Here is your reformatted content in **Markdown**:

---

# APC UPS SNMP Logger

A simple and efficient Python script for logging key metrics from an APC Uninterruptible Power Supply (UPS) via the SNMP protocol. The data is saved to a `ups_log.csv` file for easy analysis in a spreadsheet application.

This script is designed to be run continuously to monitor the health and performance of your UPS over time.

---

## Features

* **Efficient Polling**: Fetches multiple SNMP data points (OIDs) in a single network request.
* **Data Scaling**: Correctly scales raw SNMP values into human-readable formats (e.g., Volts, Amps, Hertz).
* **CSV Logging**: Logs data with a timestamp to a clean, comma-separated values (`.csv`) file.
* **Clear Console Output**: Provides real-time status updates in the terminal while logging.
* **Cross-Platform**: Works on any OS with Python installed, optimized for Linux environments.

---

## Prerequisites

* A Linux-based operating system (e.g., Pop!\_OS, Ubuntu, Debian)
* Python 3.10 or newer
* An APC UPS with a network management card (e.g., AP9631) that has SNMPv1/v2c enabled
* The IP address and SNMP Community String for your UPS

---

## Setup and Installation

These steps will guide you through setting up the project in a clean and isolated Python virtual environment.

### 1. Clone or Download

Get the project files (`apc_snmp_logger.py`, `requirements.txt`) into a local directory.

### 2. Open a Terminal and Navigate to the Project Directory

```bash
cd /path/to/your/apc_logger
```

### 3. Create and Activate a Python Virtual Environment

This creates an isolated environment named `venv` for the project.

```bash
# Create the environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate
```

Your terminal prompt should now start with `(venv)`.

### 4. Install Required Packages

Install dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Configuration

Before running the script, edit `apc_snmp_logger.py` to match your network settings.

Open the script in a text editor and modify the following lines:

```python
# SNMP config
UPS_IP = '192.168.0.6'         # <-- Replace with your UPS's IP address
COMMUNITY_STRING = 'public'    # <-- Replace with your SNMP community string
INTERVAL_SECONDS = 5           # <-- Adjust the logging frequency (in seconds)
```

---

## Usage

With your virtual environment activated, run the script:

```bash
python3 apc_snmp_logger.py
```

The script will begin logging data and printing real-time status updates.
To stop the script, press `Ctrl+C`.

---

## Output

The script generates a file named `ups_log.csv` in the same directory. This file contains the logged data with the following columns:

* Timestamp
* Battery Voltage
* Estimated Runtime
* Output Load Percent
* Input Voltage
* Output Voltage
* Battery Temperature
* Battery Current
* Line Frequency
* Output Wattage
* Battery Capacity

You can open this file with any spreadsheet application like:

* Microsoft Excel
* LibreOffice Calc
* Google Sheets

to analyze the data and create graphs.

---
