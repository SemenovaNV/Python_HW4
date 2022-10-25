# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.


number = int(input('Введите число: '))
multiplier = []
index = 2  # первое простое число

while index <= number:
    if number % index == 0:
        multiplier.append(index)
        number //= index
    else:
        index += 1
print(multiplier)