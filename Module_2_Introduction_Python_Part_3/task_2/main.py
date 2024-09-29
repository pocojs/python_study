num = int(input("Введите число: "))
degree = int(input("Введите степень от 0 до 7: "))

if degree < 0 or degree > 7:
    raise ValueError ("Введите степень не меньше 0 или не больше 7")
result = num ** degree

print(f"Результат возведения числа {num} в степень {degree}: {result}")