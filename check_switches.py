import os
import platform

def ping(host):
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    command = f"ping {param} {host} > nul" if platform.system().lower() == "windows" else f"ping {param} {host} > /dev/null 2>&1"
    return os.system(command) == 0

def check_switches(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    print("Switch Name | IP | Status")
    print("-" * 40)

    for line in lines:
        name, ip = line.strip().split(",")
        status = "UP" if ping(ip) else "DOWN"
        print(f"{name} | {ip} | {status}")

if __name__ == "__main__":
    check_switches("switches.txt")