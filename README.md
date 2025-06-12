# APC UPS SNMP Logger

> A simple and efficient Python script for logging key metrics from an APC Uninterruptible Power Supply (UPS) via the SNMP protocol. The data is saved to a `ups_log.csv` file for easy analysis in a spreadsheet application.
> This script is designed to be run continuously to monitor the health and performance of your UPS over time.

## Features

* **Efficient Polling**: Fetches multiple SNMP data points (OIDs) in a single network request.
* **Data Scaling**: Correctly scales raw SNMP values into human-readable formats (e.g., Volts, Amps, Hertz).
* **CSV Logging**: Logs data with a timestamp to a clean, comma-separated values (`.csv`) file.
* **Clear Console Output**: Provides real-time status updates in the terminal while logging.
* **Cross-Platform**: Works on any operating system with Python installed, but is optimized for a Linux environment.

## Prerequisites

* A Linux-based operating system (e.g., `Pop!_OS`, `Ubuntu`, `Debian`).
* Python 3.10 or newer.
* An APC UPS with a network management card (e.g., `AP9631`) that has SNMPv1/v2c enabled.
* The IP address and SNMP Community String for your UPS.

## Setup and Installation

These steps will guide you through setting up the project in a clean and isolated Python virtual environment.

### 1. Clone or Download

Get the project files (`apc_snmp_logger.py`, `requirements.txt`) into a local directory on your machine.

### 2. Open a Terminal and Navigate to the Project Directory

```bash
cd /path/to/your/apc_logger
