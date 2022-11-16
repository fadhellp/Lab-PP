file1 = input('Nama file pertama (auto .txt): ')
file2 = input('Nama file kedua (auto .txt): ')

try: 
    with open(file1 + '.txt', 'r') as first_file:
        file1_contents = first_file.read()
        
    with open(file2 + '.txt', 'x') as new_file:
        new_file.write(file1_contents)

    print('\nBerhasil')

except:
    print('\nGagal')