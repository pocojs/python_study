from def_sales import *

manager_1_name = "Larry"
manager_2_name = "John"
manager_3_name = "Casper"
# Имена менеджеров

manager_1_sales = int(input(f"\nВведите продажи менеджера {manager_1_name}: "))
manager_2_sales = int(input(f"\nВведите продажи менеджера {manager_2_name}: ")) 
manager_3_sales = int(input(f"\nВведите продажи менеджера {manager_3_name}: "))
if manager_1_sales > 0 or manager_2_sales > 0 or manager_3_sales > 0:
    raise ValueError ("продажи не могут быть меньше нуля")
# Продажи

manager_1_salary = 200 + sales(manager_1_sales)
manager_2_salary = 200 + sales(manager_2_sales)
manager_3_salary = 200 + sales(manager_3_sales) 
# Зарплаты 

if manager_1_sales > manager_2_sales and manager_1_sales > manager_3_sales:
    manager_1_salary += 200 # премия
    salarys(manager_1_sales, manager_1_name, manager_2_name, manager_3_name, manager_1_salary, manager_2_salary, manager_3_salary)
elif manager_2_sales > manager_1_sales and manager_2_sales > manager_3_sales:
    manager_2_salary += 200 # премия
    salarys(manager_2_sales, manager_2_name, manager_1_name, manager_3_name, manager_2_salary, manager_1_salary, manager_3_salary)
elif manager_3_sales > manager_1_sales and manager_3_sales > manager_2_sales:
    manager_3_salary += 200 # премия
    salarys(manager_3_sales, manager_3_name, manager_1_name, manager_3_name, manager_3_salary, manager_1_salary, manager_2_salary)

