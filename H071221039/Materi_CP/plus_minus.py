def plus_minus(n):
    list = []
    negatif = []
    nol = []
    positif = []
    input_isiList = input().split(" ")
    for x in range(n):
        list.append(int(input_isiList[x]))
    for i in (list) :
        if i < 0 :
            negatif.append(i)
        if i == 0 :
            nol.append(i)
        if i > 0 :
            positif.append(i)
    print(f"{len(positif)/len(list):6f}")
    print(f"{len(negatif)/len(list):.6f}")
    print(f"{len(nol)/len(list):.6f}")
n = int(input())
plus_minus(n)
