import re
inputan = input("Masukkan Inputan : ")
match = re.search("[2468a-zA-Z]{40}[13579\s]{5}", inputan)
if match :
    print("True")
else :
    print("False")
