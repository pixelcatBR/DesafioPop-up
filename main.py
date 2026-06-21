import subprocess
import time

while True:
    time.sleep(5)
    subprocess.Popen("python3 ui.py", shell=True)
