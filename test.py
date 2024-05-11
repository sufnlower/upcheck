import re

line = "443/tcp open  https   syn-ack"
port = re.search(r'\d+', line)
print(port.group())