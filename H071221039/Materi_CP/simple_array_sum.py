def plus(n):
    list = []
    total = 0
    input_array = input().split(" ")
    for x in range(n):
        list.append(int(input_array[x]))
    for i in range(len(list)):
        total = total+list[i]
    print(total)

n = int(input())
plus(n)