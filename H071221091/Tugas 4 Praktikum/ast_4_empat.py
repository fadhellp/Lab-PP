
isian = int(input())
def nilai_f(isian):
    if isian > 1:
        return isian*nilai_f(isian-1)
    elif isian < 0:
        return None

    return 1 # diluar dari kondisi if else akan keluar 1
    
print(nilai_f(isian))