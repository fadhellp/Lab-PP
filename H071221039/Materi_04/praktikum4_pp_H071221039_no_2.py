print(40*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print("Kelompok: C")
print(40*"=")


number = int(input("Enter number :"))
def isPrime(number):
    number = abs(number)
    if number == 1 or number == 0 :
        return "Not Prime"
    for i in range(2,number//2):
        if number % i == 0 :
            return "Not Prime"
    return "Is Prime"

print(isPrime(number))
