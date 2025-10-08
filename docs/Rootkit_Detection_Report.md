Rootkit Detection and Memory Forensics Project
1. Introduction

This project focuses on detecting hidden rootkits and analyzing memory dumps using advanced memory forensics techniques.
Rootkits are stealthy types of malicious software designed to hide processes or programs from detection.
Traditional antivirus tools often fail to identify them, so this project leverages direct memory analysis with DumpIt and Volatility 3 to detect hidden processes and SSDT hooks.

Goal: Automate memory acquisition and analysis using Python scripts and industry-standard tools.

2. Objectives

Capture system memory in a secure and automated way

Scan memory dumps for rootkits using Volatility 3

Detect and log suspicious processes or kernel modifications

Generate structured forensic reports

3. Required Tools and Packages

Tools:

Python 3.10+ (Python 3.11 recommended)

Volatility 3 Framework

DumpIt.exe by Comae Technologies

PowerShell (for integration)

Python Packages:

psutil

logging, datetime (built-in)

Installation
pip install psutil
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
python3 vol.py -h

Folder Structure
RootkitScannerProject/
├── Tools/
│   └── DumpIt.exe
├── memory_capture.py
├── rootkitscanner.py
├── rootkit_detector.py
└── memory_dump_xxxxx.dmp

4. Project Modules
4.1 memory_capture.py — Memory Capture

Automates DumpIt.exe to capture full system memory.

Features:

Verifies DumpIt path

Launches DumpIt with elevated privileges

Tracks dump progress

Logs events and completion status

Command:

python memory_capture.py


Outputs:

memory_dump_YYYYMMDD_HHMMSS.dmp

memory_capture_YYYYMMDD_HHMMSS.log

4.2 rootkitscanner.py — Memory Scanner

Runs Volatility 3 scans on captured dumps to detect anomalies.

Functions:

Executes plugins like windows.pslist, windows.modules, windows.ssdt

Filters suspicious process names or paths

Logs all results

Command:

python rootkitscanner.py memory_dump_xxxxx.dmp


Output:
scan_log_YYYYMMDD_HHMMSS.log
Highlights hidden processes, SSDT modifications, and anomalous modules.

4.3 rootkit_detector.py — Rootkit Detection

Analyzes Volatility results to identify potential rootkit traces.

Functionality:

Keyword-based detection (rootkit, malware, backdoor, etc.)

Detects SSDT hooks

Flags processes with missing parents or unusual paths

Command:

python rootkit_detector.py memory_dump_xxxxx.dmp


Output:

Terminal alerts for suspicious processes

Log: rootkit_scan_YYYYMMDD_HHMMSS.log

5. Process Workflow

Run memory_capture.py → creates memory dump

Run rootkitscanner.py → performs analysis

Run rootkit_detector.py → alerts and logs results

6. Advantages
Feature	This Project	Windows Defender	GMER	Malwarebytes ARK	Sophos
Deep Memory Forensics	✅ Yes	❌ No	⚠️ Partial	❌ No	❌ No
SSDT Hook Detection	✅ Yes	❌ No	✅ Yes	❌ No	⚠️ Limited
Customizable	✅ Fully extensible in Python	❌	❌	❌	❌
Offline Analysis	✅ Yes	❌	❌	❌	❌
Logging & Progress	✅ Detailed	❌	❌	❌	❌
7. Conclusion

This project demonstrates automated rootkit detection through memory forensics.
By integrating DumpIt, Volatility 3, and Python, it delivers a reliable system for detecting hidden processes and malicious kernel modifications.

8. References

Volatility Foundation

Comae Technologies – DumpIt

Volatility 3 GitHub

Python Docs

🔐 Privacy Note

All tests were performed on isolated lab systems.
No live or sensitive memory dumps are uploaded to this repository.

🧑‍💻 Author

Anish Bonda
Information Security Project — B.Tech Level
Rootkit Detection and Memory Forensics
