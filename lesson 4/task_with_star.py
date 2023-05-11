# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    num_str = str(num)
    length = len(num_str)
    if length == 1:
        return -1  # нет решения
    if num % 3 == 0:
        max_num = num
        for i in range(length):
            for j in range(0, 10):
                new_num_str = num_str[:i] + str(j) + num_str[i+1:]
                new_num = int(new_num_str)
                if new_num % 3 == 0:
                    max_num = max(max_num, new_num)
        return max_num
    else:
        half_length = (length + 1) // 2
        first_half = int(num_str[:half_length])
        second_half = int(num_str[half_length:])
        if second_half % 3 == 0:
            return num # можно сразу вернуть исходное число
        else: max_num = num
            for i in range(half_length, length):
                for j in range(0, 10):
                    if j % 3 == 0:
                        new_second_half_str = str(second_half)[:i-half_length] + str(j) + str(second_half)[i-half_length+1:]
                        new_num_str = str(first_half) + new_second_half_str
                        new_num = int(new_num_str)
                        if new_num % 3 == 0:
                            max_num = max(max_num, new_num)
            return max_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')