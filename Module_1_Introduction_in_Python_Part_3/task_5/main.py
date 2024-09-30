num = int(input("Введите число длиной в 4 цифры: "))
if len(str(num)) != 4:
    raise ValueError ("Длина числа больше или меньше 4 цифр")
b = int(num) % 10
c = ((num - b) % 100) // 10
d = ((num - c - b) % 1000) // 100
e = (num - d - c - b) // 1000
result = str(b + c + d + e)
print(f"{b}{c}{d}{e}")