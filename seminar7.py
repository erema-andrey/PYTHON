# Задача №47. 
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values. 
 

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:   
#     print('ok')
# else:   
#     print('fail')

# # values = transformation = lambda x: x


# import math
# def find_farthest_orbitx(x):
#     spis = []
#     for i in x:
#         if i[0]! =i[1]:
        
#         # spis = list(lambda lst: lst[0] * lst[1] * p)
        
# from math import pi


        
        
# from math import pi

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# def find_farthest_orbit(list_of_orbits: list):
#     for orbit in list_of_orbits:
#            # если площадь текущей орбиты = максимальной (максимальную находим в списке площадей всех орбит, кроме круговых)
#         if orbit[0] * orbit[1] * pi == max(map(lambda lst: lst[0] * lst[1] * pi,filter(lambda lst: lst[0] != lst[1], list_of_orbits))):
#             return orbit
# print(*find_farthest_orbit(orbits))       
        
        
        
        
# Задача №51.Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют
# одинаковое значение некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод: 
# Вывод: values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
# print(‘same’) 
# else: print(‘different’)

def same_by(characteristic, objects):
    if len(objects) == 0:
        return True
    char_compare = characteristic(objects[0])   # находим значение хар-ки первого эл-та
    # сравниваем значения хар-к всех эл-тов
    result_list = list(map(lambda x: characteristic(x) == char_compare, objects))
    return all(result_list)

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print('same') 
else: 
    print('different')



