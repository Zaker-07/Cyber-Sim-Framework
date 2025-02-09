import time
import os

log_file_path = "/var/log/snort/snort.alert.fast"

def monitor_snort_logs(log_file):
    print(f"Monitoring Snort log at {log_file}")
    with open(log_file, "r") as file:
        file.seek(0, os.SEEK_END)
        while True:
            line = file.readline()
            if line:
                print(f"[ALERT] {line.strip()}")
            time.sleep(1)

monitor_snort_logs(log_file_path)
