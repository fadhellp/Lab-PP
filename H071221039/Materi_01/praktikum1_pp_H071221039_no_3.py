print(53*"=")
print("NAMA\t: Muhammad Khaekal\nNIM\t: H071221039\nKelompok: C")
print(53*"=")
print("\tMENGHITUNG TAGIHAN LISTRIK BULANAN")
print(53*"-")

Nilai = input("Pemakaian listrik harian dalam satuan watt jam :")

print("Tarif listrik : Rp. 1325/Kwh")
print(53*"-")

wh = float(Nilai)
Tarif = 1352  # DALAM HARIAN
Kwh = wh/1000
Bulanan = Kwh*30
TarifBulanan = int(Bulanan*Tarif)

print ("Tagihan listrik perbulannya adalah : Rp.", TarifBulanan)
print(53*"=")
print("\t\t  Terima Kasih")
print(53*"=")