while True:
    nilai = int(input("MASUKKAN NILAI :"))

    if nilai >=90 and nilai<=100 :
        print(">nilai",nilai,"= 'A'")
    elif nilai >=80 and nilai<90 :           
        print(">nilai",nilai,"= 'B'")           
    elif nilai >=70 and nilai <80 :
        print(">nilai",nilai,"= 'C'")
    elif nilai >=60 and nilai <70 :
        print(">nila",nilai,"= 'D'")
    elif nilai >=40 and nilai <50 :
        print(">nilai",nilai,"= 'E'")
    elif nilai <=40 and nilai >0 :
        print(">nilai",nilai,"= 'F'")    
    else :                                 
        print("tidak ada")               