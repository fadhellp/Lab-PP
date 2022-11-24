try:
    nilai= float(input("nilai= "))

    if nilai >= 90 and nilai <= 100:
        print(f"nilai {nilai} = A ")
    elif nilai >= 80 and nilai < 90:
        print(f"nilai {nilai} = B ")
    elif nilai >= 70 and nilai < 80:
        print(f"nilai {nilai} = C ")
    elif nilai >= 60 and nilai < 70:
        print(f"nilai {nilai} = D ")
    elif nilai >= 40 and nilai < 60:
        print(f"nilai {nilai} = E ")
    elif nilai < 40 and nilai >= 0:
        print(f"nilai {nilai} = F ")
    else:
        print("input salah")
except:
    print("input salah")