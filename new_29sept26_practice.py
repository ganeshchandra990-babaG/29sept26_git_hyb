import subprocess
import webbrowser
import time

subprocess.run("date")
time.sleep(2)
subprocess.run("who")

time.sleep(2)
subprocess.run("whoami")
time.sleep(2)
subprocess.run("uptime")
time.sleep(2)
subprocess.run("df")

print("up")