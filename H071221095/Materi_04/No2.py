x = int(input("Masukkan bilangan pertama : "))
y = int(input("Masukkan bilangan kedua : "))

def getFPB (x,y) :
    if x > y :
        bilangan_terkecil = y 
    else :
        bilangan_terkecil = x 

    # fpb=0
    for i in range (1, bilangan_terkecil +1) :
        if (x % i == 0) and (y % i == 0 ) :
            fpb = i 
            
    return fpb 

print ("FPB" , (x,  y) , "=", getFPB(x,y)) 