# Задача №31.Последовательностью Фибоначчи называется последовательность 
# чисел a0, a1, ..., an, ...,где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи 

# Input: 7 
# Output: 21
# Задание необходимо решать через рекурсию


# def find_fibo(x, fibo_lst=[0, 1]): 
#     if len(fibo_lst) == x:
#         print(fibo_lst)
#         return fibo_lst[-1] 
#     fibo_lst.append(fibo_lst[-1] + fibo_lst[-2])
#     return find_fibo(x, fibo_lst)

# print(find_fibo(int(input('Введите номер числа Фиббоначи: '))))






# Задача №33.Хакер Василий получил доступ к классному журналу и хочет заменить все
# свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


from random import randint



# def change_my_marks_var1(marks):
#     max_mark = max(marks)   
#     min_mark = min(marks)   
#     marks = [str(i) for i in marks]   
#     #marks = list(map(str, marks))   #аналог 11 строки
#     return ' '.join(marks).replace(str(max_mark), str(min_mark))   


def change_my_marks_var2(marks):
    max_mark = max(marks)   
    min_mark = min(marks)   
    for i in range(len(marks)):   
        if marks[i] == max_mark:  
            marks[i] = min_mark   
    return marks

marks_list = [randint(1, 5) for _ in range(int(input('Введите количество оценок: ')))]
print(*marks_list)
# print(change_my_marks_var1(marks_list))  
print(*change_my_marks_var2(marks_list)) 
