import re
#2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
#x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779

kondisi = r'^[A-Za-z24680]{40}[13579\s]{5}$'

s = input()
hasil1 = re.findall(kondisi, s)
if hasil1:
    print('true')
else:
    print('false')































    # s = input('')

# regex1 =r'[0?2?4?6?8?_?a-z?A-Z?]'
# regex2 =r'[1?3?5?7?9? ?]'

# result1 = re.findall(regex2, s[0:40])   #divariabel ini apabiula di regex 2 diremukan seperri kode akan terinput
# result2 = re.findall(regex1, s[40:45])  #findall menemukan semua kode dalam parameternya
# print(result1, result2)
# if result1:
#     print('false')
#     exit()
# elif result2: 
#     print('false')
#     exit()

# if len(s) == 45:
#     print('true')
# else:
#     print('false')