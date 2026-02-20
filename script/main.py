import subprocess

try:
    with open("inventories/igeomat.yaml", "r") as f:
        lines = f.readlines()
        for line in lines:
            line_strip = line.strip()
            if line_strip.startswith("ansible_host"):
                ip = line_strip.split(" ")[1]
                result = subprocess.run(["ssh-keyscan", "-H" f"{ip}", ">>", "~/.ssh/known_hosts"], capture_output=True, text=True)
            continue
except:
    print("Arvhivo no existe")
