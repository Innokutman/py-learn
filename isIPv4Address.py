# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso
import re
def isIPv4Address(inputString):
    ipv4_address = re.compile('^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
    if ipv4_address.match(inputString):
        return True
    else: 
        return False
print(isIPv4Address("172.16.254.1"))