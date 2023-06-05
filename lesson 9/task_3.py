# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open('test_file/task_3.txt') as f:
    prices = []
    current_group = []
    for line in f:
        if line.strip():
            current_group.append(float(line.strip()))
        else:
            if current_group:
                prices.append(sum(current_group))
                current_group = []
    if current_group:
        prices.append(sum(current_group))
three_most_expensive_purchases = sum(sorted(prices, reverse=True)[:3])
assert three_most_expensive_purchases == 202346
