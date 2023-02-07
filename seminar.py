# Напишите программу, которая принимает на вход строку, и отслеживает, сколько 
# раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

    
         

# empty = 'a a a b c a a d c d d'
# list_empty = empty.split()
# direction = {}
# res_str = ' '
# for i in list_empty:
#     if direction.get(i) != None:
#         direction[i] += 1
#         res_str += i+f'_{direction[i]} '
#     else:
#         direction[i] = 0
#         res_str += f'{i} '
# print(res_str)
           
           
      
# empty = 'a a a b c a a d c d d'
# list_empty = empty.split()
# direction = {}
# res_str = ' '
# for i in list_empty:
#     if direction.get(i) != None:
#         direction[i] += 1
#         res_str += i+f'_{direction[i]} '
#     else:
#         direction[i] = 0
#         res_str += f'{i} '
# print(res_str)
           
input_str = 'a a a b c a a d c d d'

input_lst = input_str.split()
print(input_lst)
res = []

for i in range(len(input_lst)):
    x = input_lst[:i]
    if x.count(input_lst[i]) == 0:
        res.append(input_lst[i])
    else:
        res.append(f'{input_lst[i]}_{x.count(input_lst[i])}')
print(res)
out_str = ' '.join(res)
print(out_str)
           