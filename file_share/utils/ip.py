from re import findall, match
from subprocess import getoutput


def getIPAddress() -> str:
    data = getoutput("ifconfig")
    allIp = findall(r"inet [.\d]+", data)

    if allIp:
        address = match(r"inet ([.\d]+)", allIp[0])

        if address:
            return address.group(1)

    return "127.0.0.1"
