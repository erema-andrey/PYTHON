# data = [15, 25,35,34,23,145,78]
# res = list(filter(lambda x: x % 10 == 5,data)) 
# print(res)


# user = ['user_1', 'user_2', 'user_3', 'user_4']
# # n = [4, 3, 2, 1]
# # salary = [333, 222,111]
# # data = list(zip(user, salary, n))
# data = list(enumerate(user))
# print(data)


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')


# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()


colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()
