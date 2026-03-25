from collections import defaultdict
import re

log_file = "windows_logs.txt"
failed_logins = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "EventID:4625" in line:
            ip_match = re.search(r'IP:(\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip = ip_match.group(1)
                failed_logins[ip] += 1

print("=== Failed Login Attempts ===")

for ip, count in failed_logins.items():
    print(f"{ip} → {count}")

print("\n=== Suspicious IPs ===")

for ip, count in failed_logins.items():
    if count >= 3:
        print(f"⚠️ {ip} → Brute Force Attack")
