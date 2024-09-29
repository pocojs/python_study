num = int(input("Введите число от 1 до 100: "))

if num < 1 or num > 100:
    print("Введите число не меньше 1 или не больше 100")
elif num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)