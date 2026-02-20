#! /usr/bin/env python3
import os
import subprocess

try:
    print(os.path.abspath(__file__))
    with open("inventories/igeomat.yaml", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('ansible_host'):
                ip = line.split(" ")[1]
                result = subprocess.run(["ssh-keyscan", "-H" f"ip", ">>", "~/.ssh/known_hosts"], capture_output=True, text=True)
                print(result.stdout)
            continue
                

except:
    print('Arvhivo no existe')