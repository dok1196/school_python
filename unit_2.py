# Задание 1
a = 4
P = a * 4
S = a * 2
D = a * 2 ** 0.5
print(f'Периметр квадрата равна {P} \nПлощадь квадрата равна {S} \nДиагональ квадрата равна {round(D, 2)}')

# Задание 2
a1 = float(4)
b1 = float(-16)
c1 = float(10)
Dis = b1 ** 2 - 4 * a1 * c1
if Dis < 0:
    print('Уравнение не имеет действительных корней')
else:
    x1 = (-b1 + Dis) / (2 * a1)
    x2 = (-b1 - Dis) / (2 * a1)
    x1 = round(x1, 2)
    x2 = round(x2, 2)
    print("Корни уравнения:", x1, x2)

# Задание 3
r = 'Первый обзац'
o = 'Вторая строчка'
q = r + " " + o
print(q, q.split(), r.replace(r[:2], o[:2]), o.replace(o[:2], r[:2]))

# Задание 4
way = r'C:\Users\11089\PycharmProjects\pythonProject\home_work.py'
path = way.split("\\")
file_name = path[-1]
file_name = file_name.split(".")[0]
print(file_name)

# Задание 5
a = 5
b = 7
c = a + b
C = a * b
print(f'{a} + {b} = {c} \n{a} * {b} = {C}')

# Задание 6
text = 'Вышел месяц из тумана'
b = text[::2]
print(b)

# Задание 7
t = 'tnb'
d = 'My cat home fun qrd bgwz'
set_t = set(t)
set_d = set(d)
intersection_set = set_t.intersection(set_d)
result = d[min([d.index(x) for x in intersection_set]): max([d.index(x) for x in intersection_set])+1]
print(result)

# Задание 7 вариант 2
t = 'Myc'
d = 'My cat home fun qrd bgwz'
t1 = t[0]
l1 = d.find(t1)
t2 = t[1]
l2 = d.find(t2)
t3 = t[2]
l3 = d.find(t3)
d_min = min(l1, l2, l3)
d_max = max(l1, l2, l3)
res = d[d_min:d_max+1]
print(res)
