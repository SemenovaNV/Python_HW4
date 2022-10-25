# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

numbers = list(map(int,input('Введите числа через пробел: ').split()))
print(f'Исходный список {numbers}')
new_list = []
[new_list.append(i) for i in numbers if i not in new_list]
print(new_list)

