## Todo: Get from list of IPs
# Print all list of IPs and defang them

text = "97.255.255.255, 545.255.255.255"


def ip(ip):
    return ip.replace(".", "[.]")


# input = input("Enter your IP address: ")

print(ip(text))
