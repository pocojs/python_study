from def_operator import *

print(f"\nСписок операторов: Билайн, МТС, Теле2, Мегафон;")
operator_caller = str(input("\nВыберите оператора звонящего из выше предложенного списка: "))
operator_receiving = str(input("Выберите оператора принимающего из выше предложенного списка: "))
value_call = int(input("Введите стоимость разговора: "))
operator_caller_value = 0
operator_receiving_value = 0

operator_caller_value = operators(operator_caller, operator_caller_value)
operator_receiving_value = operators(operator_receiving, operator_receiving_value)


if value_call <= 0:
    raise ValueError("Стоимость звонка не может быть отрицательной или равняться нулю")

result = value_call * operator_caller_value / operator_receiving_value

print(result)

