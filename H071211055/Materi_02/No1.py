nilai =int(input("nilai =")) 

if nilai >= 90:
    hasil = "A"
elif nilai >= 80:
    hasil = "B"
elif nilai >= 70:   
    hasil = "C"
elif nilai >= 60:
    hasil = "D"
elif nilai >= 40:
    hasil = "E"
else:
    hasil = "F"

print(f"> nilai anda = {hasil}")