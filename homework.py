#Задача 2
#Найдите сумму цифр трехзначного числа.

#num = int(input("Введите целое: "))
#mult = 1
#while (num != 0):
#    mult = mult * (num % 10)
#    num = num // 10
#print("Произведение цифр равно: ", mult)


#Задача 4
#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, 
#что Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#s = int(input())
#p = s//4
#k = s//2
#c = s//4
#print(p, c, k)


#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
#и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
#где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
#т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#a = int(input())   
#if (len(str(a)) == 6):
#    a1 = a // 100000
#    a2 = a // 10000 % 10
#    a3 = a // 1000 % 100 % 10
#    a4 = a // 100 % 1000 % 100 % 10
#    a5 = a // 10 % 10000 % 1000 % 100 % 10
#    a6 = a % 10
#    b1 = (a1 + a2 + a3)
#    b2 = (a4 + a5 + a6)
#    if (b1 == b2):
#        print('YES')
#    else:
#        print('NO')



#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

#n = int(input())
#m = int(input())
#k = int(input())

#if k < n * m and ((k % n == 0) or (k % m == 0)):
#    print('YES')
#else:
#    print('NO')

n,m,k = int(input()),int(input()),int(input())
if n*m>k:
    if k%n==0 or k%m==0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')    