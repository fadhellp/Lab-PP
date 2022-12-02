def isiFPB(a,b): 
    if (b==0):
        return a
    else:
        return isiFPB(b,a%b) 

input_a = int(input())
input_b = int(input())

print('FPB( %s,%s)='%(input_a,input_b),isiFPB(input_a,input_b))

if input_a == 0 or input_b == 0:
    print('salah')

isiFPB (4,8)

