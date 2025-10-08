import subprocess
import os
import logging
import time
from datetime import datetime
import psutil
import sys

# Configure logging
log_filename = f"memory_capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_latest_dump_file():
    """Return path to the latest .dmp or .raw file in current dir."""
    files = [f for f in os.listdir() if f.lower().endswith((".raw", ".dmp"))]
    if not files:
        return None
    return max(files, key=os.path.getctime)

def wait_for_dump_completion(dump_path, stable_duration=10):
    """Waits until the file size of the dump stops changing (DumpIt completed)."""
    print("\n📡 Monitoring dump progress...")
    last_size = 0
    stable_time = 0

    while True:
        if not os.path.exists(dump_path):
            time.sleep(1)
            continue

        current_size = os.path.getsize(dump_path)
        if current_size != last_size:
            last_size = current_size
            stable_time = 0
        else:
            stable_time += 1

        # Show progress
        sys.stdout.write(f"\r📊 Dump size: {current_size / (1024 * 1024):.2f} MB")
        sys.stdout.flush()

        if stable_time >= stable_duration:
            print("\n✅ Dump appears to be complete.")
            return True

        time.sleep(1)

def capture_memory_dump(tool_path="C:\\RootkitScannerProject\\Tools\\DumpIt.exe"):
    try:
        if not os.path.exists(tool_path):
            print(f"❌ Error: Tool not found at {tool_path}")
            logging.error(f"Tool not found at {tool_path}")
            return False

        print("🧠 Launching DumpIt with admin privileges...")
        powershell_command = f'Start-Process -FilePath "{tool_path}" -Verb RunAs'
        subprocess.Popen(["powershell", "-Command", powershell_command])

        # Wait for a new dump file to appear
        print("⏳ Waiting for dump file to appear...")
        dump_file = None
        timeout = time.time() + 300  # 5 minutes max
        while time.time() < timeout:
            dump_file = get_latest_dump_file()
            if dump_file:
                break
            time.sleep(1)

        if not dump_file:
            print("❌ Dump file was not created.")
            return False

        wait_for_dump_completion(dump_file)
        logging.info(f"Dump completed: {dump_file}")
        return True

    except Exception as e:
        print(f"⚠️ Error: {str(e)}")
        logging.error(f"Exception: {str(e)}")
        return False

if __name__ == "__main__":
    capture_memory_dump()
