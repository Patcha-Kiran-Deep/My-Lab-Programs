import subprocess
import re

temp = subprocess.Popen(["tail", "-n", "15", "/var/log/syslog"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
bc = temp.communicate()
for eachLog in bc[0].decode().splitlines():
    getPID = re.search(r"\[(\d{4,5})\]", eachLog)
    print(getPID.group(1))