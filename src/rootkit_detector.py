import psutil
import logging
import os
import sys
from datetime import datetime

# Setup logging
log_filename = f"rootkit_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_suspicious_process(proc):
    """
    Checks if a process is suspicious based on name, path or parent status.
    """
    suspicious_keywords = ["rootkit", "malware", "hidden", "test", "turla", "duqu", "zeus", "backdoor"]
    try:
        name = proc.name().lower()
        exe = proc.exe().lower()
        ppid = proc.ppid()

        # Check for suspicious names
        if any(keyword in name for keyword in suspicious_keywords):
            return True, "Name match"

        # Check for suspicious paths
        if "system32" not in exe and "program files" not in exe:
            return True, "Unusual path"

        # Check if it has no parent (might be hidden)
        if ppid == 0:
            return True, "No parent"

    except (psutil.AccessDenied, psutil.NoSuchProcess):
        return False, None

    return False, None

def detect_rootkits():
    """
    Scans live system processes for suspicious indicators.
    """
    print("\nScanning live system for suspicious processes...\n")
    logging.info("Starting live rootkit scan")

    suspicious_found = False
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            suspicious, reason = is_suspicious_process(proc)
            if suspicious:
                print(f"ALERT: Suspicious process - PID {proc.pid} - {proc.name()} ({reason})")
                logging.warning(f"Suspicious: PID {proc.pid} - {proc.name()} - Reason: {reason}")
                suspicious_found = True
            else:
                print(f"Clean: PID {proc.pid} - {proc.name()}")
        except Exception as e:
            logging.error(f"Error reading process: {e}")

    if suspicious_found:
        print(f"\nPotential rootkit activity detected! Check log file: {log_filename}")
    else:
        print("\nNo suspicious activity detected.")

if __name__ == "__main__":
    detect_rootkits()
