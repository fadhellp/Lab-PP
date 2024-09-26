import re

regex_ipv4 = r'(([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])\.){3}([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])$'
regex_ipv6 = r'(([\d,A-F,a-f]{1,4}?\:){7})([\d,A-F,a-f]{1,4})$'

n = int(input(''))
list_address = []

for i in range(n):
    address = input('')
    list_address.append(address)

print() 

for x in list_address:
    ipv4 = re.search(regex_ipv4, x)     #ipv4 0-255         terdiri dari 4grup(.)
    if ipv4:
        print('IPv4')
    else:
        ipv6 = re.search(regex_ipv6, x) #ipv6 hexadesimal       terdiri dari 8 grup(:)
        if ipv6:
            print('IPv6')
        else:
            print('Bukan IP Address')

# 3
# This line has trailing whitespace
# 121.203.197.20
# 2001:0db8:0000:0000:0000:ff00:0042:8329