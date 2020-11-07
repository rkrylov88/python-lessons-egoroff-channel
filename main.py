# a = int(input())
# hunds = a // 100
# decs = (a // 10) % 10
# ones = a % 10
# print(hunds + decs + ones)

# a = int(input())
# n100 = a // 100
# n20 = (a - n100*100) // 20
# n10 = (a - n100*100 - n20*20) // 10
# n5 = (a - n100*100 - n20*20 - n10*10) // 5
# n1 = (a - n100*100 - n20*20 - n10*10 - n5*5) // 1
# print(n100 + n20 + n10 +n5 +n1)

# Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент.
# Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
# Учтите, что число n может быть больше, чем количество минут в сутках.

# n = int(input())
# n = n % 1440
# hours = n // 60
# mins = n % 60
# print(hours, mins)

# Дано целое число n. Выведите следующее за ним четное число.
# Задачу необходимо решить целочисленными операциями без использования условных операторов и\или циклов.
# n = int(input())
# print(((n//2)+1)*2)

# Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов в диапазоне
# от 0 до 23, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд.
# Количество минут и секунд при необходимости дополняются до двузначного числа нулями.
# Программа получает на вход число n - количество секунд, которое прошло с начала суток.
# Выведите показания часов, соблюдая формат.
# n = int(input())
# n = n % (60*60*24)
# hours = n // 3600
# m = n - hours * 3600
# mins = m // 60
# sec = m % 60
# decmins = mins // 10
# onesmins = mins % 10
# decsec = sec // 10
# onessec = sec % 10
# print(hours,":",decmins,onesmins,":",decsec,onessec,sep='')
#
# print(r"  /~~~\ ")
# print(r" //^ ^\\")
# print(r"(/(_*_)\)")
# print(r"_/''*''\_")
# print(r"(/_)^(_\)")

# a = map(int, input().split())
# print(777 in a)

# a = list(map(int, input().split()))
# print(type(a))
# print(min(a), max(a), sep=' ')
# a,b  = input().split()
# A = list(a.upper())
# B = list(b.upper())
# a = '-'.join(A)
# b = '-'.join(B)
# print(a, b, sep = ' ')


# a = list(input())
# b = a.copy()
# b.reverse()
# if a == b:
#     print("YES")
# else:
#     print("NO")

# s1 = input()
# s2 = input()
# l1 = list(s1)
# l2 = list(s2)
# l2.reverse()
# if l1 == l2:
#     print("YES")
# else:
#     print("NO")

# a, b, c = map(int, input().split())
# if (a + b) > c and (a + c) > b and (b + c) > a:
#     print("YES")
# else:
#     print("NO")

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером (иногда и с незначащими нулями),
# где сумма первых трех цифр равна сумме последних трех. Т.е. билеты с номерами 385916 и 001010 – счастливые,
# т.к. 3+8+5=9+1+6 и 0+0+1=0+1+0. Вам требуется написать программу, которая проверяет счастливость билета.
# Программа получает на вход одно целое число N (0 ≤ N < 106) и должна вывести «YES»,
# если билет с номером N счастливый и «NO» в противном случае.

# s1 = input()
# s = s1.zfill(6)
# l = list(s)
# if int(l[0]) + int(l[1]) + int(l[2]) == int(l[3]) + int(l[4]) + int(l[5]):
#     print("YES")
# else:
#     print("NO")

# Для положительного целого числа n определим функцию f:
# f(n) = -1+2-3+4-5...
# Ваша задача — посчитать f(n) для данного целого числа n.
# В единственной строке записано положительное целое число n
# Выведите f(n) в единственной строке.
# i = int(input())
# if i % 2:
#     i = -i
#     print(i//2)
# else:
#     print(i//2)

# n, m = map(int, input().split())
# i = 1
# while (n + i // m - i) > 0:
#     i = i + 1
# print(i)

# a, b = map(int, input().split())
# i = 1
# while a < b:
#     a = a ** 3
#     b = b ** 2
#     i = i + 1
# print(i)

# male_c = int(input())
# male_l = list(map(int, input().split()))
# fem_c = int(input())
# fem_l = list(map(int, input().split()))
# exact = 0
# count = 0
# while count < len(male_l):
#     if fem_l.count(male_l[count]):
#         fem_l.remove(male_l[count])
#         male_l.remove(male_l[count])
#         exact = exact + 1
#     count = count + 1
# count = 0
# while count < len(male_l):
#     if fem_l.count(male_l[count] - 1):
#         fem_l.remove(male_l[count] - 1)
#         male_l.remove(male_l[count] - 1)
#         exact = exact + 1
#     count = count + 1
# count = 0
# while count < len(male_l):
#     if fem_l.count(male_l[count] + 1):
#         fem_l.remove(male_l[count] + 1)
#         male_l.remove(male_l[count] + 1)
#         exact = exact + 1
#     count = count + 1
# print(exact)

#Нужно посчитать количество пар целых чисел (a, b) (0 ≤ a, b), которые удовлетворяют системе.
# n, m = map(int, input().split())
# a = 0
# b = 0
# count = 0
# while a < 10:
#     while b < 10:
#         if (a*a + b == n) and (a + b*b == m):
#             count += 1
#         b += 1
#     a += 1
#     b = 0
# print(count)

# У Василия есть a свечей. Когда Василий зажигает новую свечу, сначала она горит ровно один час, а затем тухнет.
# Василий — сообразительный малый, поэтому из b потухших свечей он умеет получать одну новую свечу.
# В последствии эту новую свечу (так же как и другие новые свечи) можно зажечь.
# a, b = map(int, input().split())
# h = 0
# while a // b > 0:
#     h += a
#     a = a // b
# h += a
# print(h)

# В последний день уходящего 2016 года Лимак собирается принять участие в соревновании по спортивному программированию.
# Соревнование начнётся в 20:00 и будет продолжаться четыре часа, то есть ровно до полуночи.
# Участникам будет предложено n задач, упорядоченных по возрастанию сложности, то есть задача 1 будет самой лёгкой,
# а задача номер n — самой сложной. Лимак знает, что ему потребуется 5·i минут на решение i-й задачи.
# Друзья Лимака планирую устроить роскошную новогоднюю вечеринку и Лимак хочет прибыть в полночь или ранее.
# Он знает, что ему требуется ровно k минут чтобы добрать до места проведения вечеринки от своего дома,
# где он собирается участвовать в соревновании.
# n, k = map(int, input().split())
# time = 240 - k
# count = 0
# while n > 0 and time >= 5*count:
#     count += 1
#     n -= 1
#     time -= 5*count
# print(count)

#Как-то раз ему в голову пришла строка длины n, состоящая из нулей и единиц.
# Рассмотрим следующую операцию — мы выбираем любые две соседние позиции в строке, и если в одной из них ноль,
# а в другой — единица, то разрешается удалить обе эти цифры, в результате чего строка строка становится длины n-2.
# i = int(input())
# s = input()
# while s.count("10"):
#     s = s.replace("10", "")
# print(len(s))

# Программа принимает на вход одно натуральное число и выводит на экран сумму цифр данного числа
# i = int(input())
# sum = 0
# while i // 10 > 0:
#     sum += i % 10
#     i = i // 10
# sum += i
# print(sum)

# Программа принимает на вход одно натуральное число и выводит на экран произведение цифр данного числа
# i = int(input())
# sum = 1
# while i // 10 > 0:
#     sum *= i % 10
#     i = i // 10
# sum *= i
# print(sum)

# Программа принимает на вход одно натуральное число. Ваша задачи найти сколько раз встречается цифра 7 в этом числе
# i = input()
# print(i.count("7"))

#Дано натуральное число N. Определить, является ли оно простым. Натуральное число N называется простым,
# если у него есть только два делителя: единица и само число N.
# i = int(input())
# if i < 0:
#     i = -1 * i
# s = []
# count = 1
# if i == 0:
#     print("Yes")
# elif i == 1:
#     print("Yes")
# else:
#     while count * count < i:
#         if i % count == 0:
#             s.append(count)
#         count += 1
#     if len(s) > 0:
#         print("Yes")
#     else:
#         print("No")

# i = int(input())
# if i < 0:
#     i = -1 * i
# s = []
# count = 1
# if i == 0:
#     print("0")
# elif i == 1:
#     print("1")
# else:
#     while count <= i:
#         if i % count == 0:
#             s.append(count)
#         count += 1
#     print(sum(s))

# вводим сначала количество строк, потом сами строки и ищем в них слово "рок", выводим номер строчки и позицию символа
# n = int(input())
# my_list = []
# my_list1 = []
# for i in range(n):
#     my_list.append(input())
# for i in range(len(my_list)):
#     my_list1.append(my_list[i].lower())
#     if my_list1[i].find("рок") != -1:
#         print(i+1, my_list1[i].find("рок") + 1)

# n = int(input())
# s = ""
# for i in range(n):
#     temp = input()
#     if temp.find("соль") == -1:
#         if len(s) == 0:
#             s = temp
#         else:
#             s = s + ", " + temp
# print(s)

# char = input()
# my_string = input()
# my_list = my_string.split()
# for i in range(len(my_list)):
#     if char in my_list[i]:
#         print(my_list[i])

# Напишите программу, которая находит рекордное количество вхождений (не обязательно подряд) символа в строку.
# s = input()
# s.lower()
# my_list = []
# for i in range(len(s)):
#     my_list.append(s.count(s[i]))
# print(max(my_list))

# Для делимости числа на 11 необходимо, чтобы разность между суммой цифр, стоящих на четных местах, и суммой цифр,
# стоящих на нечетных местах, делилась на 11.
# Требуется написать программу, которая проверит делимость заданного числа на 11.
# Выведите “YES”, если число делится на 11, или “NO” иначе.

# s = input()
# n = list(s)
# nechet = 0
# chet = 0
# for i in range(len(n)):
#     if i % 2 == 0:
#         chet += int(n[i])
#     else:
#         nechet += int(n[i])
# if (nechet - chet) % 11 == 0:
#     print("YES")
# else:
#     print("NO")

#На вход вашей программе поступает положительное целое число n, а ваша задача вывести в порядке возрастания все цифры,
# которые встречались в этом числе, и напротив каждого также необходимо вывести
# сколько раз данная цифра встречалась в числе n

# my_list = list(input())
# for i in range(len(my_list)):
#     my_list[i] = int(my_list[i])
# my_list.sort()
# my_set = set(my_list)
# for elem in my_set:
#     print(elem, my_list.count(elem))

#В этой задаче вам предстоит построить лесенку из чисел. Программа принимает на вход
# целое положительное число n (n<=15) - количество уровней, ваша задача вывести n уровней,
# в каждом из которых стоят числа от 1 до значения уровня.

# a = int(input())
# my_list = []
# tempstr = "1"
# if a > 0:
#     my_list.append(tempstr)
#     for i in range(1, a):
#         tempstr = tempstr + " " + str(i + 1)
#         my_list.append(tempstr)
#     for i in range(len(my_list)):
#         print(my_list[i])


# Ваша задача состоит в том, чтобы решить несколько более общую задачу – а именно по числу n
# найти количество простых чисел p из интервала n < p < 2n.

def isprime(i):
    if i < 0:
        i = -1 * i
    s = []
    count = 1
    if i == 0:
        return True
    elif i == 1:
        return True
    else:
        while count * count <= i:
            if i % count == 0:
                s.append(count)
            count += 1
        if len(s) > 1:
            return False
        else:
            return True

n = int(input())
my_list = []
for i in range(n+1, 2 * n):
    if isprime(i):
        my_list.append(i)
print(len(my_list))





