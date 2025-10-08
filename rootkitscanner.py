import psutil
import os

def is_suspicious(proc):
    """
    Check if a process is suspicious based on missing parent or unusual executable path.
    """
    try:
        # Check for missing parent
        if proc.ppid() == 0:
            return True

        # Check if the executable path is in a suspicious location
        exe_path = proc.exe()
        if "System32" not in exe_path and "SysWOW64" not in exe_path and "Program Files" not in exe_path:
            return True

    except (psutil.AccessDenied, psutil.NoSuchProcess):
        return False
    return False

def list_processes():
    """
    List all running processes and flag suspicious ones.
    """
    print("\nScanning for suspicious processes...\n")
    print(f"{'PID':<8}{'Process Name':<30}{'Suspicious'}")
    print("=" * 50)

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            suspicious = is_suspicious(proc)
            print(f"{proc.pid:<8}{proc.name():<30}{'Yes' if suspicious else 'No'}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == "__main__":
    list_processes()
