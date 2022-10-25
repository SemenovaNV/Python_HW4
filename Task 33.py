# Задана натуральная степень k. Сформировать случайным образом
#  список коэффициентов (значения от 0 до 100) многочлена 
#  и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0


import random

# создать список коэфициентов передавая степень count_elements
def create_list(count_elements):
    coefficientes_lst = [random.randint(0, 100 + 1) for i in range(count_elements + 1)]
    return coefficientes_lst

# заполнение многочлена передавая lst_data
def create_polynomial(lst_data):
    if len(lst_data) < 1:
        return 'x = 0'
    k = len(lst_data) - 1
    result = ""
    for i in range(len(lst_data)):
        if i == len(lst_data) - 1:
            result += f'{lst_data[i]} = 0'
            return result
        else:
            result += f'{lst_data[i]}*x'
            if k != 1:
                result += f'^{k}'
            k -= 1
        result += f' + '
    return result

# степень k
degree_k = int(input("Введите натуральную степень k = "))

# список рандомных коэфициентов
lst = create_list(degree_k)
print(lst)

# создаем файл и записываем многочлен использую список рандомных коэфициентов от степени k
polynomial = create_polynomial(lst)
print(polynomial)
save_to_file(polynomial)

# создать файл передавая polynomial_str
def save_to_file(polynomial_str):
    with open('file.txt', 'w') as data:
        data.write(polynomial_str)