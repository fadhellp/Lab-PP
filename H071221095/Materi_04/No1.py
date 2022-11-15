list = [7,4,2,1,3,2]

def bilangan (list) :
    for i in range (len(list)) :
        for j in range (i +1,len (list)) :
            if list [i] >= list [j] :
                list [i] , list [j] = list [j] , list [i]

    return list 
print (bilangan(list))