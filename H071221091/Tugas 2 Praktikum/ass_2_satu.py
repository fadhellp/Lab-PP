
while True:
    ko_nilai = int(input("NILAI :"))

    if ko_nilai >=90 :
        print(">nilai",ko_nilai,"= 'A'")
    elif ko_nilai >=70 and ko_nilai<80 :           #penggunaan and dalam varibel karena input 2x 
        print(">nilai",ko_nilai,"= 'B'")           
    elif ko_nilai >=80 and ko_nilai <90 :
        print(">nilai",ko_nilai,"= 'C'")
    elif ko_nilai >=60 :
        print(">nilai",ko_nilai,"= 'D'")
    elif ko_nilai >=40 :
        print(">nilai",ko_nilai,"= 'E'")
    elif ko_nilai <=40 and ko_nilai >0 :
        print(">nilai",ko_nilai,"= 'F'")    
    else :                                 #penggunaan else tidak berguna ketika penginputan nilai dibatasi dibawah nol
        print("salah salah")               #else berguna pada variabel 15, jika formatnya seperti itu