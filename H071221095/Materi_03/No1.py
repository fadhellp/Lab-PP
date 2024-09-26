try: 
    x = int(input("Nilai X: "))
    y = int(input("Nilai Y: "))

    if x<y:
        for i in range(1, y+1):
            print(i, end=" ")
            if i % x == 0:
                print("")

    else:
        print("salah")
except:
    print("salah")