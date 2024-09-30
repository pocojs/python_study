metres = int(input("Введите число метров: "))
if metres <= 0:
    raise ValueError ("Число метров не может быть меньше нуля")
centi = metres * 100
deci = metres * 10
milli = metres * 1000
print(f"\nСантиметры: {centi} \nДециметры: {deci} \nМиллиметры: {milli}")