def rotated_string (kata) :
    temp = kata + kata 
    size = len (kata) 

    for i in range (size) :
        for j in range  (size) :
            print (temp[i+j+1] , end= "")
      
        print (end="|"  )
        

kata = (input("Masukkan kata :"))
rotated_string(kata)