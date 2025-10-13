# 🧠 Rootkit Detection and Memory Forensics Project

## 1. Introduction
This project focuses on detecting hidden rootkits and analyzing memory dumps using advanced memory forensics techniques.  
Rootkits are stealthy types of malicious software designed to hide the existence of certain processes or programs from normal detection.  
Traditional antivirus tools often fail to find them — therefore, this project leverages **direct memory analysis** with **DumpIt** and **Volatility 3** to identify hidden processes and SSDT hooks.

**Goal:** Automate memory acquisition and analysis using Python scripts and industry-standard tools like DumpIt and Volatility.

---

## 2. Objectives
- Capture system memory in a secure and automated way  
- Scan memory for rootkits and malicious traces using Volatility 3  
- Detect and log suspicious processes or kernel modifications  
- Present results in a structured report format  

---

## 3. Required Tools and Packages

### Tools
- **Python 3.10+** (Python 3.11 preferred)  
- **Volatility 3 Framework**  
- **DumpIt.exe** by Comae Technologies  
- **PowerShell** for script automation and elevation

### Python Packages
- `psutil`
- `logging` and `datetime` (built-in)

### Installation Steps

**Step 1:** Install Python  
Download from [python.org/downloads](https://www.python.org/downloads/)  
✅ Ensure “Add Python to PATH” is checked.

---

**Step 2:** Install Required Packages  
bash :
pip install psutil

---

**Step 3:** Install Volatality 3
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
python3 vol.py -h

---

Step 3.1: Download DumpIt
Get it from Comae Technologies.
Place it in the following path:
RootkitScannerProject/Tools/DumpIt.exe

---

**Step 4:** Folder Structure
Memory-Forensic-Rootkit-Scanner/
│
├── src/
│   ├── memory_capture.py           # Memory dump acquisition
│   ├── rootkitscanner.py           # Volatility-based scanning
│   └── rootkit_detector.py         # Rootkit signature detection
│
├── Tools/
│   └── DumpIt.exe                  # Memory acquisition tool (not uploaded)
│
├── docs/
│   └── Rootkit_Detection_Report.md # Full technical documentation
│
├── analysis/
│   ├── pslist_output.txt           # Sample sanitized outputs
│   └── ssdt_hooks.txt
│
├── .gitignore                      # Excludes dump and temp files
└── README.md                       # Project overview


---

**Step 5:** Project Modules

5.1 Memory Capture — memory_capture.py

Captures a full physical memory dump using DumpIt.
Functionality : 
Checks for DumpIt executable
Launches it with elevated privileges
Monitors dump progress
Logs actions and completion status

Code :
python memory_capture.py

Outputs : 
memory_dump_YYYYMMDD_HHMMSS.dmp
memory_capture_YYYYMMDD_HHMMSS.log

5.2 Memory Scanner — rootkitscanner.py

Uses Volatility 3 to analyze memory dumps.
Functionality :
Executes Volatility plugins (windows.pslist, windows.ssdt, etc.)
Logs all scan results
Filters for suspicious process patterns (rootkit, malware, etc.)

Code :
python rootkitscanner.py memory_dump_xxxxx.dmp

Outputs :
scan_log_YYYYMMDD_HHMMSS.log
Identifies :
Suspicious or hidden processes
SSDT modifications
Unlinked drivers

5.3 Memory Detector — rootkit_detector.py

Performs automated detection of suspicious processes and SSDT hooks.
Functionality :
Keyword-based scanning (rootkit, malware, zeus, turla, etc.)
Detects SSDT hooks and unusual process paths
Reports findings and logs results


Code :
python rootkit_detector.py memory_dump_xxxxx.dmp

Outputs :
Terminal alerts for suspicious processes
rootkit_scan_YYYYMMDD_HHMMSS.log

**Step 6:** Process Workflow

Run memory_capture.py
→ Generates memory dump file
Run rootkitscanner.py
→ Analyzes dump and logs suspicious findings
Run rootkit_detector.py
→ Provides visual alerts and rootkit identification

**Step 7:** Comparative Advantages


| Feature / Capability             | This Project                   | Windows Defender | GMER            | Malwarebytes ARK | Sophos      |
| -------------------------------- | ------------------------------ | ---------------- | --------------- | ---------------- | ----------- |
| **Deep Memory Forensics**        | ✅ Yes                          | ❌ No             | ⚠️ Partial      | ❌ No             | ❌ No        |
| **Rootkit Detection Accuracy**   | ✅ High                         | ⚠️ Basic         | ✅ Good          | ⚠️ Basic         | ⚠️ Moderate |
| **Offline Analysis**             | ✅ Yes                          | ❌ No             | ❌ No            | ❌ No             | ❌ No        |
| **Customizable & Extendable**    | ✅ Fully extensible in Python   | ❌                | ❌               | ❌                | ❌           |
| **Transparency of Results**      | ✅ Full logs & traceability     | ⚠️ Limited       | ⚠️ Logs only    | ❌                | ⚠️ Limited  |
| **SSDT Hook Detection**          | ✅ Yes                          | ❌                | ✅ Yes           | ❌                | ⚠️ Limited  |
| **Integration with DumpIt**      | ✅ Integrated                   | ❌                | ❌               | ❌                | ❌           |
| **Logging & Progress Tracking**  | ✅ Detailed                     | ❌                | ❌               | ❌                | ❌           |
| **Cross-platform Dump Analysis** | ✅ Supports Volatility profiles | ❌                | ⚠️ Windows-only | ❌                | ❌           |



**Step 8:** Conclusion

This project demonstrates how memory forensics can be used to detect rootkits that evade conventional antivirus tools.
By automating memory capture with DumpIt, analysis with Volatility 3, and detection with Python scripts, this toolkit offers a transparent, customizable, and accurate approach to system compromise analysis.


**Step 9:** Process Workflow

Volatility Foundation
Comae Technologies
Volatility 3 GitHub
Python Official Documentation


Privacy and Ethics :

All testing was performed in an isolated lab environment.

👨‍💻 Author

Anish Bonda
Information Security Project — B.Tech Level
Rootkit Detection and Memory Forensics
No real or sensitive memory dumps are uploaded to this repository.
