def sales(manager):
    if manager <= 500:
        manager = manager / 100 * 3
    elif manager > 500 and manager < 1000:
        manager = manager/ 100 * 5
    elif manager >= 1000:
        manager = manager / 100 * 8
    return manager

def salarys(manager_1_sales, manager_1_name, manager_2_name, manager_3_name, manager_1_salary, manager_2_salary, manager_3_salary):
    print(f"\nУ менеджера {manager_1_name} самые большие продажи: {manager_1_sales}")
    print(f"Зарплата менеджера {manager_1_name} с учётом премии: {manager_1_salary},\nЗарплата менеджера {manager_2_name}: {manager_2_salary},\nЗарплата менеджера {manager_3_name}: {manager_3_salary}")
