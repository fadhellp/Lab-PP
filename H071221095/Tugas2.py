second = input("detik=")

second = int(second)

hours = second//3600

second = second-(hours*3600)
minute = second//60
second = second-(minute*60)
print(f"{hours:02d}:{minute:02d}:{second:02d}")
