# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код
def generate_random_name():
    """
    Инициализируем список, в который передаем латинский алфавит.
    Берем цикл While с флагом True делаем его количество повторных вызовов бесконечным для новой генерации.
    Создаем список из 2-ух элементов, каждый из которых является случайным словом, состоящим из латинских букв.
     Для этого используется генератор списка, который вызывает функцию `random.choices()`
     для выбора случайных букв из списка `a_b_c` и функцию `random.randint()` для определения случайной длины слова
      (от 1 до 15 символов).
    """
    a_b_c = list('abcdefghijklmnopqrstuvwxyz')
    while True:
        name1 = ''.join(random.choice(a_b_c) for i in range(random.randint(1, 15)))
        name2 = ''.join(random.choice(a_b_c) for i in range(random.randint(1, 15)))
        yield f"{name1} {name2}"


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
