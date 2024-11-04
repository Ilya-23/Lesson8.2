def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data

def calculate_average(numbers):
    mean = None
    number = 0

    try:
        sum = personal_sum(numbers)[0]
        for i in numbers:
            if type(i) is int or type(i) is float:
                number += 1
            else:
                continue
        try:
            mean = sum / number
        except ZeroDivisionError:
            mean = 0
            print('Деление на 0!')
    except TypeError:
        print('В numbers записан некорректный тип данных')
    return mean


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать