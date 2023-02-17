# def calk1(a, b):
#     return a + b 

# def calk2(a, b):
#     return a * b 

# def math(op, x, y):
#     print(op(x, y))
# # calk1 = lambda a,b:a+b
# math(lambda a,b:a+b, 5, 45)


# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар 
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data :
#     if i % 2 == 0:
#         out.append((i, i ** 2))
# print(out)

# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i ** 2 ))
# print (res)

# def select(f,col):
#     return[f(x) for x in col]

# def where(f,col):
#     return[x for x in col if f(x)]
# res = map(int,data)
# print(res)
# res = where(lambda x: x % 2 == 0,res)
# print(res)
# res = map(lambda x:(x, x ** 2),res)
# print(res)

# list_1 = [x for x in range(1, 10)]
# print(list_1)
# list_1 = list(map(lambda x: x +10 ,list_1))
# print(list_1)


# Задача: C клавиатуры вводится некий набор чисел, в качестве 
# разделителя используется пробел. Этот набор чисел будет
# считан в качестве строки. Как превратить list строк в list
# чисел?

# .split(' , ') приводит строку в список используя пробел 
# или запятую
# data = '1 2 3 5 8 15 23 38'
# print(data)

# data = list(map(int, data.split()))
# print(data)






