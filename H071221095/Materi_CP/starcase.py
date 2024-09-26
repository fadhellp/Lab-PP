n = int(input())
spasi = n-1
for i in range(n):
    for j in range(spasi):
        print(' ', end="")
    for j in range(n-spasi):
        print('#', end="")
    print()
    spasi = spasi-1

