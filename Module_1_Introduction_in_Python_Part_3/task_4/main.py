height = int(input("Введите высоту треугольника: "))
foundation = int(input("Введите длину основания треугольника: "))
if height <= 0 or foundation <= 0:
    raise ValueError ("Длина основания и высота не могут быть равны нулю или быть меньше его")
result = height / 2 * foundation5
print(result)