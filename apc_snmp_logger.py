# Filename: apc_snmp_logger.py
import time
import csv
from datetime import datetime
from pysnmp.hlapi import (
    SnmpEngine,
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity,
    getCmd
)

# SNMP config
UPS_IP = ''  # <-- Replace with your UPS's IP address
COMMUNITY_STRING = 'public'
INTERVAL_SECONDS = 5

# --- Corrected OIDs for APC SMT1500RM2U w/ AP9631 ---
# A mix of standard UPS-MIB and APC's PowerNet-MIB
OIDS = {
    # Name: (OID, Scaling Function)
    'battery_voltage': ('1.3.6.1.2.1.33.1.2.5.0', lambda x: x / 10.0), # Tenths of Volts -> Volts
    'estimated_runtime': ('1.3.6.1.2.1.33.1.2.3.0', lambda x: x), # Already in Minutes
    'output_load_percent': ('1.3.6.1.2.1.33.1.4.4.1.5.1', lambda x: x), # Percentage
    'input_voltage': ('1.3.6.1.4.1.318.1.1.1.3.2.1.0', lambda x: x), # Volts
    'output_voltage': ('1.3.6.1.2.1.33.1.4.4.1.2.1', lambda x: x), # Volts
    'battery_temperature': ('1.3.6.1.4.1.318.1.1.1.2.2.2.0', lambda x: x), # Celsius
    'battery_current': ('1.3.6.1.4.1.318.1.1.1.2.2.4.0', lambda x: x / 10.0), # Tenths of Amps -> Amps
    'line_frequency': ('1.3.6.1.2.1.33.1.3.2.0', lambda x: x / 10.0), # Tenths of Hertz -> Hertz
    'output_wattage': ('1.3.6.1.4.1.318.1.1.1.4.2.3.0', lambda x: x), # Watts
    'battery_capacity': ('1.3.6.1.2.1.33.1.2.4.0', lambda x: x) # Percentage
}

def get_snmp_data(oid_map):
    """
    Fetches and processes multiple SNMP OIDs in a single request.
    """
    oids_to_fetch = [ObjectType(ObjectIdentity(v[0])) for v in oid_map.values()]

    error_indication, error_status, error_index, var_binds = next(
        getCmd(SnmpEngine(),
               CommunityData(COMMUNITY_STRING, mpModel=1),
               UdpTransportTarget((UPS_IP, 161)),
               ContextData(),
               *oids_to_fetch)
    )

    if error_indication:
        print(f"SNMP error: {error_indication}")
        return None
    elif error_status:
        print(f"SNMP error status: {error_status.prettyPrint()} at {error_index}")
        return None

    results = {}
    oid_keys = list(oid_map.keys())
    for i, var_bind in enumerate(var_binds):
        key = oid_keys[i]
        _, value = var_bind
        try:
            scaling_func = oid_map[key][1]
            results[key] = scaling_func(float(value))
        except ValueError:
            print(f"Could not convert value for {key}: {value}")
            results[key] = None
    return results

# --- Main Logging Loop ---
try:
    with open('ups_log.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        header = ['Timestamp'] + [key.replace('_', ' ').title() for key in OIDS.keys()]
        writer.writerow(header)

        print("Starting UPS SNMP logging... Press Ctrl+C to stop.")
        
        while True:
            data = get_snmp_data(OIDS)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if data and all(v is not None for v in data.values()):
                row_data = [timestamp] + [f"{data[key]:.2f}" for key in OIDS.keys()]
                writer.writerow(row_data)
                file.flush()

                print(f"[{timestamp}] Logged | "
                      f"Load: {data['output_load_percent']:.1f}% | "
                      f"Runtime: {data['estimated_runtime']:.0f} min | "
                      f"Input: {data['input_voltage']:.1f}V")
            else:
                print(f"[{timestamp}] Failed to read one or more SNMP values. Retrying...")

            time.sleep(INTERVAL_SECONDS)

except KeyboardInterrupt:
    print("\nLogging stopped by user.")
except Exception as e:
    print(f"\nAn error occurred: {e}")
