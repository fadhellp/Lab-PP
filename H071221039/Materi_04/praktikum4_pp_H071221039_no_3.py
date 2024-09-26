print(40*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print("Kelompok: C")
print(40*"=")

number = int(input("Enter number :"))
def factorial(number):
    if number == 0 :
        return 1
    else :
        return number * factorial(number-1)

print(factorial(number))