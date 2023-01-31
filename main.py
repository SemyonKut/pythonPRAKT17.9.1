"""Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.
В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
Далее программа работает по следующему алгоритму:
Преобразование введённой последовательности в список
Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)

Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.

Помните, что у вас есть числа, которые могут не соответствовать заданному условию. В этом случае необходимо вывести соответствующее сообщение"""

def Sort(list_sequence):                             #функция coртировка вставками
    for i in range(1, len(list_sequence)):
        x = list_sequence[i]
        idx = i
        while idx > 0 and list_sequence[idx - 1] > x:
            list_sequence[idx] = list_sequence[idx - 1]
            idx -= 1
        list_sequence[idx] = x

def binary_search(list_sequence, element, left, right):       #функция алгоритм двоичного поиска
    if left > right:
        return False
    middle = (right + left) // 2
    if list_sequence[middle] == element:
        return middle
    elif element < list_sequence[middle]:
        return binary_search(list_sequence, element, left, middle - 1)
    else:
        return binary_search(list_sequence, element, middle + 1, right)

while True:
    try:
        sequence = input('Введите последовательность чисел через пробел:\n').split()
        list_sequence = [float(x) for x in sequence]
        break
    except ValueError:
        print(' ***Неверный формат ввода (введите последовательность чисел через пробел)*** ')
print('Последовательность чисел:', sequence)

while True:
    try:
        element = float(input('Введите любое число:\n'))
        break
    except ValueError:
        print(' ***Неверный формат ввода (введите число)*** ')

print("*" * 225)
print('Последовательность чисел (список):', list_sequence, type(list_sequence))
print('Число пользователя:', element)
print("*" * 225)

Sort(list_sequence)
print('Отсортироанный список (по возрастанию элементов в нем): ', list_sequence)

if element < min(list_sequence):
    print(f'Числа {element} нет в последовательности (меньше мин. эл-а последовательности {min(list_sequence)})')
elif element > max(list_sequence):
    print(f'Числа {element} нет в последовательности (больше макс. эл-а последовательности {max(list_sequence)})')
elif element == max(list_sequence):
    print(f'Число {element} последнее в последовательности (равно макс. эл-а последовательности {max(list_sequence)})')
else:
    el_index = binary_search(list_sequence, element, 0, len(list_sequence) - 1)
    rI = min(list_sequence, key=lambda x: (abs(x - element), x))
    ind = list_sequence.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < element:
        print(f'Позиция элемента, который меньше введенного пользователем числа ({element}), а следующий за ним больше или равен этому числу: {list_sequence.index(rI)}')
    elif min_ind < 0:
        print(f'Введенноe пользователем число ({element}) самое маленькое в последовательности, его позиция: {list_sequence.index(rI)}')
    elif rI > element:
        print(f'Позиция элемента, который меньше введенного пользователем числа ({element}), а следующий за ним больше или равен этому числу: {list_sequence.index(rI)}')