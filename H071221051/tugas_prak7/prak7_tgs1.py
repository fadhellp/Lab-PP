import re
kondisi = r'^[A-Za-z24680]{40}[13579\s]{5}$'

s = input()
hasil1 = re.findall(kondisi, s)
if hasil1:
    print('true')
else:
    print('false')