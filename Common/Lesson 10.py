# x = int(input())
# def closest_higher_mod_5(x):
#     if x % 5 == 0:
#         return closest_higher_mod_5(x + 1)
# closest_higher_mod_5(x)

# int(input())
# def closest_higher_mod_5(x):
#     remainder = x % 5
#     if remainder == 0:
#         return (5 - (x % 5))
#         print(remainder)


# def closest_higher_mod_5(x):
#     y = x
#     while y % 5 != 0:
#         y += 1
#     return y




# mi = 0
# km = 0

# def mi_to_km(mi, km):
#     return(mi * 1.609)
#     return(km // 1.609)

# km_mi = input("choose km or mile ")
# if km:
#     km = float(input())
#     mi = km // 1.609
#     #print(mi)

# else:
#     mi= float(input())
#     km = mi * 1.609
#     #print(km)
# print(mi_to_km(mi, km))



# mi = 0
# km = 0

# def mi_to_km(mi, km):
#     return(mi * 1.609)
#     return(km // 1.609)

# km_mi = input("choose "or"  mi )
# if km_mi == km:
#     km = float(input())
#     mi = km // 1.609
#     #print(mi)


# elif km_mi == mi:
#     mi= float(input())
#     km = mi * 1.609
#     #print(km)
# else:
#     print("choose km or mi")

# print(mi_to_km(mi, km))


##########################################################################
#########################################################################


            
         ##########       Вызов функций         ############


           #####          Показаны мин и макс      #########


# Вы создаете программу для отображения минимальных и максимальных чисел.
# Заполните пропуски, чтобы завершить




#################################################################################


# a = int(input())
# b = int(input())
# c = int(input())
# def age(a, b, c):
#     return min(a, b, c)
# name = age(a, b, c)  
# print(name)

# print(min([int(input()) for i in range(3)]))


#############################################################################

# def greet_user(name):
#     return "Hello, " + name + "!"

# name = "Bob"
# message = greet_user(name)

# print(message)


##############################################################################


# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# def sum_numbers(a, b):
#     return (a + b)
# print("Result:", sum_numbers(num1,num2))


# a = str(input())
# b = str(input())
# c = input()
#  = input()
# e = input()
# f = input()
# def alf(a,b,c,,e,f):
#     for letter in (a,b,c,,e,f):
#         if letter == a:
#             continue
#     return min(a,b,c,,e,f)   
# print(alf)


##############################################################################
#############################################################################

###   Вычисление мощности с использованием основания и показателя степени   ###

#Напишите программу, которая принимает основание и показатель степени в качестве 
# входных данных и выводит результат возведения основания в степень показателя 
# степени. Программа должна считывать основание и показатель степени 
# от пользователя как целые числа, вычислять результат 
# с помощью функции pow() и выводить конечное значение.


# base = int(input())
# exponent = int(input())
# def power(base, exponent):
#     return pow(base, exponent)
# result =  power(base, exponent)
# print(result)   

# OR #

# print(int(input()) ** int(input()))

#################################################################################
#################################################################################

       ######     Найдите самое длинное слово      #######


# Создайте программу для поиска самого длинного из данных слов и вывода длины 
# самого длинного слова. Заполните пропуски правильными встроенными функциями.


# word1 = "short"
# word2 = "longer"
# word3 = "longest"
# def find_longest(word1, word2, word3):
#     return max(len(word1), len(word2), len(word3))
# result = find_longest(word1, word2, word3)
# print(result)    



###############################################################################
##############################################################################


# x = int(input())
# y = int(input())
# def total(x, y):
#    return sum((x, y))
# result = total(x, y)
# print(result)
#  OR #
# print(sum([x, y]))

############################################################################
###########################################################################



# print(input("Hello, world! Hello, "))


#################################################################################
#############################################################################
   ###     Добавление и удаление целых чисел из списка    #####

# Вы создаете простую программу. Программа начинается со списка целых чисел. 
# Цель — добавить новое целое число в конец списка, а затем удалить 
# первое вхождение указанного целого числа из списка. 
# Все, что вам нужно сделать, это заполнить пробелы в предоставленном коде, 
# чтобы завершить функциональность. 




###############################################################################
##########################################################################

                       # list comprehension syntax



# 1.  new_list = [x for x in other_list]

# 2.  new_list = [x for x in other_list if x == 0]

# 3.  new_list = [x if x > 0 else -100 for x in other_list]




# new_list = [x for x in some_iterable]

                       ################################
                           # the equivalent code

# new_list = []
# for x in some_iterable:
#     new_list.append(x)

############################################################################


# squared numbers

# numbers = [1, 2, 3]
# square_list = [x * x for x in numbers]  # [1, 4, 9]
# print(square_list)

###########################################################################


# from string to float

# strings = ["8.9", "6.0", "8.1", "7.5"]
# floats = [float(num) for num in strings]  # [8.9, 6.0, 8.1, 7.5]
# print(floats)


#############################################################################



   ############     Понимание списка с помощью if   ##################  


# list comprehension with condition

# new_list = [x for x in some_iterable if condition]



# # odd numbers
# numbers = [4, 8, 15, 16, 23, 42, 108]
# odd_list = [x for x in numbers if x % 2 == 1]  # [15, 23]
# print(odd_list)




# # conditions with functions
# text = ["function", "is", "a", "synonym", "of", "occupation"]
# words_tion = [word for word in text if word.endswith("tion")]  
# print(words_tion)  # ["function", "occupation"]


###    Наконец, мы можем ввести else оператор в list comprehension.   ###

#    [x if condition else y for x in some_iterable].

# Используя это, мы можем, например, получить 0 в новом списке для каждого
#  отрицательного числа в старом списке:


# old_list = [8, 13, -7, 4, -9, 2, 10]
# new_list = [num if num >= 0 else 0 for num in old_list]
# print(new_list)  # [8, 13, 0, 4, 0, 2, 10]


#############################################################################

                 ######      Граница         ##############

# Напишите программу, которая делит числа на два списка в зависимости от того, 
# больше они или меньше 5. Вам не нужно включать само число 5 .


# numbers = [int(n) for n in input()]

# less_than_5 = [x for x in numbers if x < 5] 
# greater_than_5 =[x for x in numbers if x > 5]

# print(less_than_5)
# print(greater_than_5)


#odd_list = [x for x in numbers if x % 2 == 1]

#new_list = [num if num >= 0 else 0 for num in old_list]


#################################################################################

                   ######      Список слов     ######

# Напишите программу, которая берет список слов, создает новый список слов, 
# начинающихся с буквы «а» в первом списке, и печатает его.

# Используйте метод string str.startswith(('a', 'A'))для захвата всех слов, 
# начинающихся с 'a'или 'A'. В качестве альтернативы, измените регистр 
# проверяемого слова на нижний с помощью str.lower(), но учтите, 
# что это изменение не должно быть постоянным.

# Например words = ['apple', 'pear', 'banana', 'Ananas'], если , 
# то ваша программа должна вывести список ['apple', 'Ananas'].





# words = input().split()
# words_a = [word for word in words if word.startswith(('a', 'A')) == True]
# print(words_a)

# words = input()
# word_list = [word for word in words if word.startswith(('a','A'))]
# print(word_list)


 
 
# # conditions with functions
# text = ["function", "is", "a", "synonym", "of", "occupation"]
# words_tion = [word for word in text if word.endswith("tion")]  
# print(words_tion)  # ["function", "occupation"]

 ###############################################################################
            #####         Длина        ##########

# Учитывая список слов в коде ниже, создайте список длин этих слов и выведите его.
 

# words = ["apple", "it", "creek", "pelican", "subsequent", "horse",]
# wordslen = [len(word) for word in words]
# print(wordslen)

###   OR   ###
# print([len(word) for word in words])


###############################################################################

                       ######     Среднее     ########

# При наличии числовой последовательности на входе создайте список, 
# в котором каждое число будет цифрой из этой входной строки. 
# Затем используйте этот список для вычисления среднего арифметического, 
# то есть суммы всех цифр, деленной на их общее количество.


# num_list = [int(i) for i in input()]
# print(sum(num_list) / len(num_list))

# data = input()
# num_list = [int(numbers) for numbers in data]
# print(sum(num_list) / len(num_list))

# numbers = input()
# digits = [int(x) for x in numbers]
# mean = sum(digits) / len(digits)
# print(mean)


###############################################################################
##########################################################################


#Начните читать код с «for».
 
#Сначала разрешите «for x in range(11) if x % 2 == 1» 
# (что означает «взять все числа от 0 до 10, если они нечетные»)
# Затем «x * 2» — это и есть желаемый результат.

# nums = int(input())
# nums = [x * 2 for x in range(11) if x % 2 == 1]
# print(nums)

# nums = []
# for x in range(11):
#     if x % 2 == 1:
#         x = x * 2
#         nums.append(x)
# print(nums)




################################################################################
################################################################################


                    #####     Сколько дней     #####



         # Day = 24 hours * 60 minutes * 60 seconds = 86400 seconds
         # You can either use // or int()

# Список секунд — это список чисел, представляющих секунды. 
# Преобразуйте количество секунд в полные дни и выведите список, 
# содержащий эти значения. Количество полных дней должно быть значением int.


# numbers = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# seconds = [x // (60 * 60 * 24) for  x in numbers]
# print(seconds)


          ###########################################

# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# print([days / 86400 for days in seconds])


          ############################################

# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# print([int(sec / 60 / 60 / 24) for sec in seconds])

#            ############################################


# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# divider = 60 * 60 * 24
# print([x // divider for x in seconds]) 

#              #############################################

# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# print([int(day / (60 * 60 * 24)) for day in seconds])

#              ###############################################

# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# print([days // (60 * 60 * 24) for days in seconds]) 

#                  ###############################################

# import math
# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# day = 86400
# days = [math.floor(x / day) for x in seconds]
# print(days)

#                     ###############################################


# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# days = [second // 86400 for second in seconds]
# print(days)

#                      ###############################################

# seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# # create a list of days here
# day = 86400
# days = [int(x // day) for x in seconds]
# print(days)

##################################################################################
################################################################################


                     #########    Тройной      ############

           # Выведите список чисел от 1 до 1000 , которые делятся на 3 


# print([x for x in range(1, 1001) if x % 3 == 0])

           # OR #

# print([x for x in range(int(input())) if x % 3 == 0])

            #   OR   #

# print(list(range(3, 1000, 3)))          

             #     OR    #

# number = [x for x in range(int(input())) if x % 3 == 0]  # [15, 23]
# print(number)



################################################################################
###########################################################################

 
                #####    Индексы    ####
 
 #   Вы хотите получить доступ к последнему вычислению   ###

# calculations = input()#.split()
# print(calculations[-1])

################################################################################
################################################################################



      #### Доступ к элементам в списке и обработка ошибок индекса ####


# animals = ['cat', 'dog', 'elephant', 'giraffe']
# first_animal = animals[0]
# last_animal = animals[-1]
# out_of_index_animal = animals[10] if len(animals) > 10 else "List has less than 11 elements"
# print("First animal: " + first_animal)
# print("Last animal: " + last_animal)
# print("Out of index animal: " + out_of_index_animal)

###############################################################################


# Выясните, какой из этих символов отмечает конец строки, 
# сохраненной в переменной sentence, и выведите его.

# sentence = input()
# print(sentence[-1] 
# if sentence[-1] in {'.', '!', '?'} 
# else "No punctuation mark found.")
  
   
# OR #

# sentence = input()
# if sentence[-1] in {'.', '!', '?'}:
#    print(sentence[-1])
# else:
#    print("No punctuation mark found.")

#  OR  #

# sentence = input()
# print(sentence[-1])



##############################################################################


# Приложение погоды сохраняет ежедневные температуры в списке. 
# Можете ли вы заполнить пробелы, чтобы отобразить температуру на среду? 
# Помните, Python использует индексацию от нуля для списков.


# temperatures = [22, 24, 26, 28, 27, 25, 23]
# wednesday_temp = temperatures[2]
# print(f"The temperature for Wednesday is: {wednesday_temp}°C\n")


############################################################################

          ######     Последовательность элементов     #####

# Учитывая последовательность seq, сопоставьте ее элементы с соответствующими 
# индексами

# seq = [1, 2, 3, 4, 5]

# >>> seq[-len(seq)]  # How the problem gets position 0
# 1
# >>> seq[0]  # How you usually get position 0
# 1
# >>> seq[-len(seq)+1]  # How the problem gets position 1
# 2
# >>> seq[1]  # How you usually get position 1
# 2

# the next-to-last element   ----   len(seq) - 2
# the last element            ----   len(seq) - 1
# the second element         -----   -len(seq) + 1
# the first element          -----    -len(seq) 0


###############################################################################



# # Save the input in this variable
# ticket = input()
# # Add up the digits for each half
# half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
# # Thanks to you, this code will work
# if half1 == half2:
#     print("Lucky")
# else:
#     print("Ordinary")


# OR #


# ticket = str(input())
# # Add up the digits for each half
# half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

# # Thanks to you, this code will work
# if half1 == half2:
#     print("Lucky")
# else:
#     print("Ordinary")

# OR #

# ticket = [int(x) for x in input()]
# print(sum(ticket[:3]) == sum(ticket[-3:]) and "Lucky" or "Ordinary")

# OR #


# ticket = [int(x) for x in input()]
# # Add up the digits for each half
# half1 = sum(ticket[:3])
# half2 = sum(ticket[3:])

# # Thanks to you, this code will work
# if half1 == half2:
#     print("Lucky")
# else:
#     print("Ordinary")
   

# OR #


# ticket = input()

# # Add up the digits for each half
# half1 = sum(int(i) for i in ticket[:3])
# half2 = sum(int(i) for i in ticket[3:])

# # Thanks to you, this code will work
# if half1 == half2:
#     print("Lucky")
# else:
#     print("Ordinary")


##############################################################################
###############################################################################


          #########      Импорт модулей     ########## 


# import super_module

# # calling a function defined in super_module
# super_module.super_function()  

# # accessing a variable defined in super_module
# print(super_module.super_variable) 


  ###  AND   ### 

# импортировать только требуемые функции или переменные из модуля, 
# но не сам модуль.
  
# from super_module import super_function

# # super_function is now available directly at the current module
# super_function()  

# super_module.super_function()  
# # note that in this case name super_module is not imported, 
# # so this line leads to an error


### AND  ###

# import module1
# import module2
# import module3

# # the rest of module code goes here


###   AND   ###

# импортом по шаблону и имеет синтаксис 
# 
#       from module import *     #


###   AND   ###



  ###   доступ к математическим функциям  ###.

# import math

# print(math.factorial(5))  # prints the value of 5!

# print(math.log(10))  # prints the natural logarithm of 10

# print(math.pi)  # math also contains several constants
# print(math.e)


###   AND   ###


 ###   Модуль string содержит общие строковые операции и константы .   ### 

# from string import digits

# print(digits)  # prints all the digit symbols


# Модуль случайного выбора предоставляет функции, позволяющие вам делать случайный
#  выбор.


# from random import choice

# # print a random item from the list
# print(choice(['red', 'green', 'yellow']))  


###    AND   ###
 
# import super_module                     ---  Импортируйте весь модуль.
# from super_module import super_function ---- Импортируйте одну функцию из модуля.
# from module import *                    ---  Импортировать все имена из модуля.
# super_module.super_function()           ---  Доступ к функции, загруженной из модуля.

#############################################################################



     #####     Вычисление факториала с помощью циклов     #####


 ###   С помощью цикла while:   ###

# n = int(input())
# factorial = 10
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)

#############################################################################

###  Вычисление факториала с помощью цикла for: ###

# n = int(input())
# factorial = 10
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)

# OR #

# product = 1
# for n in range(1, int(input()) + 1):
#     product *= n
# print(product)

###############################################################################

       ######      Нахождение факториала рекурсией     #######

# #n = int(input())
# def fac(n):
#     if n == 1:
#         return 1
#     return fac(n - 1) * n
# print(fac(5))


#    OR   ###

# import math
# n = int(input())
# def calculate_factorial(n):
#     return math.factorial(n)
# print(calculate_factorial(n))


################################################################################

###### import   Функция factorial модуля math     #####

# import math

# n = int(input())
# factorial = math.factorial(n)
# print(factorial)

# OR #

# from math import factorial
# print(factorial(int(input())))

# OR #

# import math
# print(math.factorial(int(input())))

###   OR   ###


# from math import factorial
# n = int(input())
# print(factorial(n))


###   OR   ###

# import math

# n = int(input())
# print(math.factorial(n))

##########################################################################
#########################################################################


      ###   Калькулятор построения окружности круга   ####

# Python для вычисления длины окружности по заданному радиусу:

# import math
# def calculate_circumference(radius):
#    return 2 * math.pi * radius
# circumference = calculate_circumference(5)
# print(circumference)
 
###  i made BETTER!!! ###

# import math
# radius = int(input())
# print(2 * math.pi * radius)


################################################################################
###############################################################################



#######     Вычисление площади круга по заданному радиусу    ######

 
# import math
# def calculate_area(radius):
#     return math.pi * (radius**2)
# area = calculate_area(5)
# print(str(area))

### OR ###

# import math
# radius = int(input())
# print(math.pi * (radius**2))

#########################################################################
########################################################################

        #####       Вызов функции pow ((2,3) = 2*2*2 = 8)   #########

##     Вы работаете над реализацией функции для вызова math.pow  функции   ####

# import math
# def invoke_pow(x,y):
#    return math.pow(x,y)
# print(invoke_pow(2,3))

############################################################################
#########################################################################

     ######     Все слова с заглавной буквы   ######

# Напишите программу, которая берет строку, делает все слова в ней заглавными, 
# а затем выводит результат. Используйте функцию capwords из модуля string :


# import string
# print(string.capwords(input()))

# OR #

# import string
# input_string = input()
# print(string.capwords(input_string))

# OR #

# print(input().title())

 # OR WITH fUNCTION ##

# import string
# n = input()
# def cap_let(n):
#    return string.capwords (n)
# print(cap_let(n))

#############################################################################
############################################################################

          # Реализация функции квадратного корня в скрипте утилиты #

# вычисления квадратного корня числа в функции invoke_sqrt. 
# Затем эта функция должна быть вызвана для вычисления квадратного корня 
# из 25 и вывода результата на печать.

# import math
# def invoke_sqrt():
#     return str(math.sqrt(25))
# print(invoke_sqrt())

#############################################################################


                 ###   Функция копирования подписи   ####

# Напишите программу, которая принимает два числа с плавающей точкой, x и y ,
#  и печатает x со знаком y . Используйте функцию copysign, определенную в модуле
#  math .


# import math
# x, y = map(float, input().split(' '))
# z = math.copysign(x, y)
# print(z)

#  OR #

# from math import copysign
# x, y = map(float, input().split(' '))
# print(copysign(x, y))

# OR #

# from math import copysign
# x, y = map(float, input().split(' '))
# print(copysign(x, y))


#################################################################################
   ###   Е ** х - 1   ###

# Напишите программу, которая принимает целое число x и выводит результат,
# Для этой цели используйте функцию, expm1() определенную в модуле math .
#  Она принимает X в качестве аргумента и возвращает результат формулы выше.


# import math           # from math import expm1
# x = int(input())
# print(math.expm1(x))

# OR #

# import math
#print(math.expm1(int(input())))

# OR #

# from math import expm1
# print(expm1(float(input())))

# OR #

# import math
# print(math.expm1(int(input())))


#############################################################################
#############################################################################


# Python может генерировать случайные числа с помощью randomмодуля. 
# Но иногда мы хотим сделать ограничения по диапазону.
# Напишите программу, которая создает nпеременную, которая является 
# случайным числом от -100 до 100. Используйте функцию randint из randomмодуля. 
# Эта функция вводит два числа: начало и конец диапазона



# import random
# def randint(a, b):
#    return random.randint(a, b)
# print(randint(-100, 100))

             # OR #

# import random
# n = random.randint(-100, 101)
# print(random.randint(-100, 101))

# import random
# a = -100, 100
# b = int(input())
# print(random.randint(-100, 100))
# if b > a:
#    print("choose less")
# elif b < a:
#    print("choose more")
# else:
#    print("you are win")




##############################################################################
###############################################################################
#############################################################################


# numb = int(input("Введите целое число: "))
 
# # множество делителей заданного числа
# delitellist = {1}
 
# # первый делитель любого натурального числа
# sumlist = 1
 
# i = 2 # следующий возможный делитель заданного числа
 
# # вычислять, пока квадрат делителя не больше заданного числа
# # накопительная сумма делителей не больше заданного числа
# while i * i <= numb and sumlist <= numb:
 
#     # если заданное число делится без остатка на "делитель"
#     if (numb % i == 0):
 
#         # то к накопительной сумме делителей добавим
#         # "делитель" и частное от "число"//"делитель",
#         # если они не равны
#         # ("делитель" - 6; "число" - 36 -> 6 == 36//6 -> один делитель 6
#         # "делитель" - 6; "число" - 42 -> 6 != 42//6 -> два делителя 6, 7
#         sumlist += i + (numb//i if i != numb//i else 0)
 
#         # в множество делителей добавляем "делитель" и "частное"
#         # Если они одинаковы, то в множество "попадет" одно значение
#         delitellist.update({i, numb//i})
    
#     # увеличиваем "делитель" на 1
#     i += 1
 
# # если заданное число == сумме делителей
# if sumlist == numb:
#     print(*sorted(delitellist))
# else:
#     print(0)

###############################################################################
##############################################################################
#########################################################################


               ######   Elif statement   ######



# Код внутри блока else выполняется только в том случае, 
# если все условия перед ним — False . Смотрите следующий пример:

# light = input()  # there can be any other color
# if light == "green":
#     print("You can go!")
# elif light == "yellow":
#     print("Get ready!")
# elif light == "red":
#     print("Just wait.")
# else:
#     print("No such traffic light color, do whatever you want")



            ##############################################

                ###   Вложенные операторы elif   ###

# # nested elifs example
# traffic_lights = "green, yellow, red"
# # a string with one color
# light = "green"  # variable for color name
# if light in traffic_lights:
#     if light == "green":
#         print("You can go!")
#     elif light == "yellow":
#         print("Get ready!")
#     else:
#         # if the lights are red
#         print("Just wait.")
# else:
#     print("No such traffic light color, do whatever you want")

       ###################################################################


  # Цепочка ifутверждений подразумевает, что условия, указанные в них, 
  # совершенно не связаны и могут быть выполнены независимо друг от друга,  


     
# animal = 'unicorn'
# if animal in 'crow, dog, frog, pony':
#     print('This animal exists')
# if animal in 'unicorn, pegasus, pony':
#     print('This animal is a horse')

###############################################################################
             ######      Оценка по шкале от A до F      ######

# Вы только что получили фрагмент кода, который оценивает числовой балл в 
# градуированном представлении от A до F. Можете ли вы определить и переставить 
# строки кода в правильном порядке, чтобы гарантировать, что он работает 
# правильно? Помните, что наивысший балл (A) соответствует числовому баллу 90 и 
# выше, а самый низкий балл (F) соответствует любому числовому баллу менее 60.


# a = int(input())
# def evaluate_grade(score):
#    if score >= 90:
#       return "A\n"
#    elif score >= 80:
#       return "B\n"
#    elif score >= 70:
#       return "C\n"
#    elif score >= 60:
#       return "D\n"
#    else:
#       return "F\n"
# print(evaluate_grade(a))


#######################################################################


  #######       Сравнение двух целых чисел в Python     ######

# Дано два целых числа, num1 и num2, вам нужно определить, больше ли num1,
#  меньше ли или равно num2, и присвоить результат переменной 'comparison_resul'

# num1 = 10
# num2 = 20
# comparison_result = ""
# if num1 > num2:
#     comparison_result = "num1 is greater than num2"
# elif num1 < num2:
#     comparison_result = "num1 is less than num2"
# else:
#     comparison_result = "num1 is equal to num2"
# print(comparison_result)

##############################################################################

# Энн посмотрела телепрограмму о здоровье и узнала, что рекомендуется спать 
# не менее А часов в день. Пересыпание также вредно для здоровья, и вам 
# не следует спать больше, чем Б часов. Сейчас Энн спит H часов в день.


# a, b, h = int(input()), int(input()), int(input())
# print('Deficiency' if h < a else 'Excess' if h > b else 'Normal')

# OR #

# A = int(input())
# B = int(input())
# H = int(input())
# if H < A:
#    print("Deficiency")
# elif H > B:
#    print("Excess")
# else:
#    print("Normal")   

############################################################################


# Напишите программу Python, которая просит пользователя ввести одно целое число.
#  На основе ввода пользователя ваша программа должна отнести число к одной из 
# трех категорий. Если число является однозначной цифрой (меньше 10), 
# она должна указать, что это однозначное число. Если оно является двузначным 
# числом (меньше 100), она должна указать это. Для любого числа, которое состоит 
# из трех или более цифр, ваша программа должна указать, что число состоит из 
# нескольких цифр. 


# user_input = int(input("Please enter a number: "))
# if user_input < 10:
#    print("It's a single digit number.")
# elif user_input < 100:
#     print("It's a double digit number.")
# else:
#     print("The number has multiple digits.")


###############################################################################
                  
                  ####     Координаты    #####

# Найдите точку на декартовой координатной плоскости: к какому из четырех 
# квадрантов принадлежит точка?

# Считайте из ввода два числа, не обязательно целых, первое число будет обозначать
# положение на оси X, второе — на оси Y. Продолжим обозначать квадранты римскими
#  цифрами, как показано на рисунке.

# Если точка является началом координат (0, 0), вывести It's the origin!
# Если точка лежит на осях, с x = 0 или y = 0, вывести 
# One of the coordinates is equal to zero!


# принять два плавающих входных значения x и y
# Сначала проверьте 4 варианта, где оба должны быть больше 0 («I»), 
# оба должны быть меньше 0 («III»), x должен быть больше 0, 
# а y должен быть меньше 0 («IV») или x должен быть меньше 0, 
# а y должен быть больше 0 («III»).
# затем позаботьтесь о ситуации, когда и x, и y должны быть равны 0("Origin")
# затем позаботьтесь о том, когда одна из координат x, y должна быть равна нулю
# ("One of the coordinates is equal to zero")


# x = float(input())
# y = float(input())
# if x > 0 < y:
#    print("I")
# elif x < 0 > y:
#    print("II")
# elif x < 0 < y:
#    print("III")
# elif x > 0 > y:
#    print("IV")
# elif x == 0 and y == 0:
#    print("It's the origin!")
# elif x == 0 or y == 0:
#    print("One of the coordinates is equal to zero!")

                      ###########################

# x = float(input())
# y = float(input())
# if x == 0 and y == 0:
#     print("It's the origin!")
# elif x == 0 or y == 0:
#     print("One of the coordinates is equal to zero!")
# elif x > 0:
#     print('I' if y > 0 else 'IV')
# else:
#     print('II' if y > 0 else 'III')

               ########################################


# x, y = float(input()), float(input())

# if x * y == 0:
#     print("It's the origin!" if x + y == 0 else "One of the coordinates is equal to zero!")
# elif x > 0:
#     print("I" if y > 0 else "IV")
# else:
#     print("II" if y > 0 else "III")



############################################################################
###########################################################################

               ################  Vlozeniy if else  #####################

# x = float(input())
# if x > 1000:
#    print("!")
# elif x > 500:
#    print("@")
# else:
#    if x > 250:
#       print("#")
#    else:
#       print("$")


###########################################################################
##########################################################################


# Напишите программу, которая спрашивает пользователя, сколько времени в среднем
#  он проводит за компьютером в день. Если это меньше 2 часов, 
# программа должна вывести "That's rare nowadays!". Если это 2 часа или больше,
#  но меньше 4 часов в день, она должна вывести "This seems reasonable". 
# В любом другом случае вывести "Don't forget to take breaks!"



# hours = float(input())
# if hours < 2:
#     print("That's rare nowadays!")
# elif hours >= 2 and hours < 4:
#     print("This seems reasonable")
# else:
#     print("Don't forget to take breaks!")


##############################################################################
#############################################################################



                                 ###################

# Напишите программу, которая считывает целое число из входных данных и печатает:

# «отрицательное», если число меньше 0;

# «положительный», если число больше 0;

# «ноль», если число равно 0.

                             #######################

# number = int(input())
# if number < 0:
#    print("negative")
# elif number > 0:
#    print("positive")
# else:
#    print("zero")

# OR #

# n = int(input())
# print(["zero", "positive", "negative"][-(n < 0) + (n > 0)])

# OR #

# n = int(input())
# print("negative" if n < 0 else "zero" if n == 0 else "positive")



#################################################################################


# Шахматный король может стоять на любой клетке и может передвигаться на один шаг по горизонтали, вертикали или диагонали в любом направлении в пределах доски.

# На входе будут координаты, на которых находится король. Вам следует посчитат
# 
# и вывести, сколько ходов может сделать фигура: например, из позиции (1, 8) 
# король может сделать только 3 хода (вправо, вниз, по диагонали).

# Вот шаги, которым вы можете следовать:

# Начните со считывания координат короля с входных данных.

# Чтобы определить количество возможных ходов короля, рассмотрите все 
# возможные
#  направления: по горизонтали (влево и вправо), по вертикали (вверх и вниз) 
#  и по диагонали (вверх-влево, вверх-вправо, вниз-влево, вниз-вправо).

# Пройдитесь по каждому возможному направлению и проверьте, может ли король 
# переместиться на соответствующую клетку. Убедитесь, что новая позиция 
# находится в пределах шахматной доски (координаты от 1 до 8 включительно).

# Следите за количеством допустимых ходов.

# Наконец, выведите общее количество допустимых ходов.

                    #########################


# получить входные данные от x и y как целое число
# и использовать оператор if как строку в (1,8) и столбец в (1,8)
# и распечатать(3)
# как эта строка elif в (1,8) или столбец в (1,8)
# затем напечатайте 5
# elese печать 8

                       ########################

# THE BEST #

# column = int(input())
# row = int(input())
# if column in (1, 8) and row in (1, 8):
#     print(3)
# elif column in (1, 8) or row in (1, 8):
#     print(5)
# else:
#     print(8)


#  OR  #


# x = int(input())
# y = int(input())
# if ((x or y) == 1) and ((x or y) == 8):
#     print('3')
# elif ((x or y) == 1) or ((x or y) == 8):
#     print("5")
# else:
#     print('8')


#  OR   

# x = int(input())
# y = int(input())
 
# if (x == 1 or x == 8) and (y == 1 or y == 8):
#     print(3)
 
# elif 2 <= x < 8 a nd 2 <= y < 8:
#     print(8)
 
# else:
#     print(5)


#  OR  #


# if 1 > x > 8 and 1 > y > 8:
#     print(8)
# elif x == 1 or x == 8 and y != x:
#     print(5)
# else:
#     print(3)


###############################################################################
###############################################################################

# Один из способов классификации языков мира — рассмотрение их морфологических 
# систем. Одна из классификаций основана на индексе синтеза , 
# который отражает среднее количество морфем в слове. 
# Значения варьируются от 1 до 4, и существует 3 типа языков в соответствии 
# с этой системой. Вот они:



# index = float(input())
# if index < 2:
#    print("Analytic")
# elif index >= 2 and index <= 3:
#    print("Synthetic")
# else:
#    print("Polysyntetic")


# OR #


# index = float(input())
# if index < 2:
#    print("Analytic")
# elif 2 <= index <= 3:
#    print("Synthetic")
# else:
#    print("Polysynthetic")


#   OR   #
   

# n = float(input())
# print(['Analytic', 'Synthetic', 'Polysynthetic'][(n >= 2) + (n > 3)])


##########################################################################
#########################################################################
###########################################################################


#########        Python RANGE function and its methods        ###########



# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1
# for i in count_up_to(5):
#     print(i)


# sum = 0
# for i in range(2, 10, 2):
#     sum += i
# print(sum)  # output = 20


# sum = 0
# for i in range(2, 10, 2):
#     sum += i
# print(list(range(2, 10, 2)))


# numbers = list(range(10))
# print(numbers)  # output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# numbers = [i for i in range(10)]
# print(numbers)  # output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# for a in range(5, 0, -1):
#    s = a
# s = len(range(5, 0, -1))
# print(s)


# length = 
# print(length)  # output = 10  


# fruits = ['apple', 'banana', 'cherry']
# for i, fruit in enumerate(fruits):
#     print(i,fruit)
# Output
# 0 apple
# 1 banana
# 2 cherry


# fruits = ['apple', 'banana', 'cherry']
# for i in range(len(fruits)):
#     print(i, fruits[i])
# Output
# 0 apple
# 1 banana
# 2 cherry4


# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# for name, age in zip(names, ages):
#     print(name, age)
# Output
# Alice 25
# Bob 30
# Charlie 35




# Python
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# for i in range(len(names)):
#     print(names[i], ages[i])
# Output
# Alice 25
# Bob 30
# Charlie 35




# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
# for fruit in fruits[1:4]:
#     print(fruit)
# Output
# banana
# cherry
# date

# Для генерации индексов среза можно использовать функцию range():

# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
# for i in range(1, 4):
#     print(fruits[i])
# Output
# banana
# cherry
# date


# squares = {i: i * i for i in range(10)}
# print(squares)
# Output
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# for i in range(1, 101):
#     if i % 15 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)



###########################################################################
#############################################################################
#############################################################################

# word = input()
# for char in word:
#     print(char)

# times = int(input('How many times should I say "Hello"?'))
# for i in range(times):
#     print('Hello!')    


#  names = ['Rose', 'Daniel']
# surnames = ['Miller', 'Smith']
# for name in names:
#     for surname in surnames:
#          print(name, surname)   



         #####     Среднее значение всех чисел     #####

# Напишите программу, которая выполняет следующие действия:
# Прочитайте два целых числа, aи b, из пользовательского ввода. 
# Эти числа определяют диапазон [a, b] (включительно).

# Найдите все числа в этом диапазоне (включая aи b), которые делятся на 3.

# Рассчитайте и выведите среднее значение этих чисел.

# Пример: если диапазон входных данных — [-5, 12], то числа, делящиеся на 3, 
# будут: -3, 0, 3, 6, 9, 12. Среднее значени


# a = int(input())
# b = int(input())
# i = [i for i in range(a, b + 1) if i % 3 == 0]
# t = sum(i) / len(i)
# print(t)


# a = int(input())
# b = int(input())
# total = 0
# count = 0
# for i in range(a, b + 1):
#    if i % 3 == 0:
#       total = total + i
#       count = count + 1
# avarege = total / count
# print(avarege)


###########################################################################
##########################################################################

    #   FIND FACTORIAL NUMBER   #

# n = int(input('Enter number: '))  
# result = 1  
# for i in range(1, n + 1):
#     result = result * i
# print(f"The factorial of ", n, " is : ", result)

###########################################################################

#####     Расчет размеров прямоугольника с помощью PEP 8     #####

# В коде есть некоторые пропущенные части, отмеченные знаком «▭». 
# Заполните пробелы в коде, чтобы вычислить площадь и периметр прямоугольника, 
# и выведите результаты, следуя руководству по стилю PEP 8.



# def calculate_area(lenght, width ):
#    area = length * width
#    return area

# def calculate_perimeter(length, width):
#    perimeter = 2 * (length + width)
#    return perimeter

# length = float(input())
# width = float(input())    

# area = calculate_area(length, width)
# perimeter = calculate_perimeter(length, width)
# print(f"The area is: {area}")
# print(f"The perimeter is: {perimeter}")


############################################################################
#############################################################################

      #      Функция, аргументы и параметры     #


# def responsibility(developer, tester, project_manager, designer):
#     print(developer, "writes code")
#     print(tester, "tests the system")
#     print(project_manager, "manages the product")
#     print(designer, "develops design")

                   ## именованных аргументов  ###

# responsibility(project_manager="Sara", developer="Abdul", tester="Yana", designer="Mark")

              ##### не emенованныe  аргументы   ####

# responsibility("Abdul", "Yana", "Sara", "Mark")


     # Python знает имена аргументов, которые принимает наша функция.#

# help(responsibility)


#######################################################################

       ###   Приветствие с индивидуальным подходом    ###

# def greet_person(name):
#    greeting =  "Hello, " + name + "!"
#    return greeting
# name = input()
# print(greet_person(name))


######################################################################

# a = float(input())
# b = float(input())
# def square_odds(a, b):
#     start = a
#     if a % 2 == 0:
#         start += 1
#     end = b + 1
#     for odd in range(start, end, 2):
#       print(odd ** 2)

######################################################################

# Вам даны компоненты функции, которая получает имя и фамилию 
# пользователя в качестве аргументов, и в случае, если фамилия 
# не указана, по умолчанию принимает значение 'Doe'. 
# Функция создает приветственное сообщение, используя эти имена, 
# и возвращает указанное сообщение. 



# def greet_user(first_name, last_name="Doe"):
#    message = f"Hello {first_name} {last_name}!"
#    return message
# print(greet_user("John"))
# print(greet_user("Jane", "Smith"))

   

# def greet_person(name,surname):
#    greeting =  f"Hello, {name} {surname}!"
#    return greeting
# name = input()
# surname = input()
# print(greet_person(name,surname))



####     POKA NEZNAJU   ###
 
# def greet_user(name, surnamename="Doe"):
#    message = f"Hello {name} {surname}!"
#    return message
# name = input()
# surname = input()   
# if name == True and surname != True:
#    print(greet_user(name, "Doe"))
# else: 
#    print(greet_user(name,surname))  


#####################################################################
#####################################################################


# Вот функция, которая называется pow():

# def pow(x, y):
#     return x ** y

# Объясните код
# Возвращает x, возведенный в степень y

######################################################################
######################################################################
# 'f string'
# print(str(a) + " x " + " <you finish!>)
# a, b, c = input.split()
# Вы можете использовать отформатированные строки, 
# что значительно упрощает подобные задачи.

# print(f"{ }...")



# Напишите функцию с именем , equation_writing()которая принимает 
# три параметра: a, b, и c. Функция должна вывести уравнение в формате 
# a x + b = c, где a, b, и c— значения, переданные в качестве аргументов.
#  x И другие символы в уравнении остаются неизменными.

# def equation_writing(a, b, c):
#    print(f"{a}x + {b} = {c}")


    # 1) print("{} x + {} = {}".format(a, b, c))
    # 2) print(a, "x +", b, "=", c)
    # Next ones are oly valid if a, b and c are strings:
    # 3) print(a + ' x + ' + b + ' = ' + c)
    # 4) print(a + str(" x + ") + b + str(" = ") + c)   



######################################################################
#######################################################################
#####################################################################

# def count(a, b, c):
#     return a + b - c
# print(count(b=3, c=2, a=1))


#     выводит квадраты нечетных чисел в указанном диапазоне    # 


# def square_odds(a, b):
#     start = a
#     if a % 2 == 0:
#         start += 1
#     end = b + 1
#     for odd in range(start, end, 2):
#         print(odd ** 2)

# ## from 22 to 42
# square_odds(22, 42)        

# ## from 15 to 31
# square_odds(b=32, a=15)

# ## from 42 to 49
# square_odds(b=49, a=42)


       ###   OR   ###


# nums = [15, 22, 31, 42, 49]
# square_odds(a=nums[1], b=nums[3])
# square_odds(a=nums[0], b=nums[2])
# square_odds(b=nums[4], a=nums[3])


#######################################################################
######################################################################



#                     Двойное приветствие                #

# Мы написали функцию, которая приветствует двух человек
# В первый раз она должна вывести Hello, first_name and second_name, 
# а во второй раз Hello, second_name and first_name



# name_1 = input()
# name_2 = input()
# def greeting(first_name, second_name):
#     print("Hello,", first_name, "and", second_name)


# greeting(name_1, name_2)
# greeting(name_2, name_1)
#       # OR #
# greeting(first_name=name_2, second_name=name_1)


#######################################################################
######################################################################


        ### Давайте посчитаем общую прибыль за этот период! ###
       ###  Вы знаете общую сумму прибыли по каждому товару: ###

# На этом этапе ваша программа должна:

# Распечатайте Earned amount:строку.

# Распечатайте названия предметов и полученную за каждый из них сумму

# Распечатайте общую прибыль, как показано ниже.



# total_earned = sum(items.values())
# print(f"earned_amount: ${total_earned:.2f}")
# sum = sum + float(v[2:])


# price = """Prices:
# Bubblegum: $2
# Toffee: $0.2
# Ice cream: $5
# Milk chocolate: $4
# Doughnut: $2.5
# Pancake: $3.2"""
# print(price)

# print()

# earned_amount = ("""Earned amount:
# Bubblegum: $202
# Toffee: $118
# Ice cream: $2250
# Milk chocolate: $1680
# Doughnut: $1075
# Pancake: $80""")
# income = 202 + 118 + 2250 + 1680 + 1075 + 80
# print(f"{earned_amount} \n\nIncome:  {float(income)}")


# staff = float(input("> "))
# print("Staff Expenses: ", staff)

# other = float(input("> "))
# print("other Expenses: ", other)

# net_income = income - staff - other
# print("Net income: ", float(net_income))


####################################################################
####################################################################

# Earned_amount = {
#     'Bubblegum': 202,
#     'Toffee': 118, 
#     'Ice cream': 2250,
#     'Milk chocolate': 1680,
#     'Doughnut': 1075,
#     'Pancake': 80,
# }
 
# print('Earned_amount: ')
# for item, price in Earned_amount.items():
#     print(f"{item}: ${price}")
    
# print(f"\nIncome: ${sum(Earned_amount.values())}")
 
# staff = {
#     'Cleaner': 850,
#     'Vendor': 1120,
#     'Manager': 1300,
#     'Loader': 900,
# }
# print(f"Staff expenses: \n>${sum(staff.values())}")
 
# other_expenses = {
#     'Electricity': 100,
#     'Municipal Service': 90,
#     'Security': 30,
# }
# print(f"Other expenses: \n>${sum(other_expenses.values())}")
 
# net_income = sum(Earned_amount.values()) - sum(staff.values()) - sum(other_expenses.values())
# print('Net income: $',float(net_income), sep='')


##################################################################
#################################################################

            ###   Конвертер формата времени   ###


#### значение времени в 24-часовом формате в переменной с именем hour. 
# Ваша задача — преобразовать это значение в 12-часовой формат и 
# распечатать результат. ###

# hours = 24
# hours = int(input())
# if hours == 0:
#    print(12)
# elif hours >= 0 and hours <= 12:
#    print(hours)
# elif hours > 12 and hours <= 24:
#    print(hours - 12)

### OR JUST SIMLE   ###

# print(hours % 12 or 12)

######################################################################
##################################################################
# print(16 % 2 == 0) # CHETNOE

# print(15 % 2 == 1) # NECHETNOE

#######################################################################

# x = 1000
# r = 5
# y = 10
# a = 1500
# print(x * (1 + r/100) ** y)

####################################################################




########################################################################
# user_name = input()
# user_profession = input()
# print("My name is " + user_name + " and I am a " + user_profession + ".")

#######################################################################


# money = int(input("How much money do you spend per month: "))
# n_miles = 2
# miles_per_month = money 
# n_miles = 2
# distance = 215
# print(distance * 2 / miles_per_month)


###################################################################
                             

                  ### Расчет дохода  ###

# рассчитайте доход от сберегательного счета с процентной ставкой 5% 
# через год, учитывая сумму денег. Используйте простую формулу процентов
#  для расчета дохода:


# amount = 1000
# interest_rate = 5
# years = 1
# income = (1000 * 5 * 1) / 100
# print(income)


##################################################################

# capital = int(input("Enter your capital: "))
# capital *= 0.8
# additional_income = 1000
# capital += additional_income
# print(capital)

# capital = int(input("Enter your capital: "))
# capital = capital * 0.8
# additional_income = 1000
# capital = capital + additional_income

########################################################################
#######################################################################

# n =  int(input())
# Calculate the expression and print the result
# print(((n + 1) * n + 2) * n + 3)

#####################################################################


                    ###   Расчет 3D периметра   ###
# Tеперь приготовьтесь к решению классических математических задач.
# В этой задаче программа должна спросить пользователя о параметрах
#  прямоугольного параллелепипеда (3 целых числа, представляющих длину, 
# ширину и высоту) и вывести сумму длин ребер. Осталось только заполнить
# пробелы.



# Сумма длин всех ребер: c = 4(a + b + c)


# a = int(input())
# b = int(input())
# c = int(input())
# perimeter = 4 (a + b + c)
# print(perimeter)


########################################################################
######################################################################


                   ###   Расчет 3D поверхности   ###

# Перетаскивание — это просто, поэтому давайте поднимем планку немного 
# выше.В этой задаче программа должна спросить пользователя о параметрах
#  прямоугольного параллелепипеда 
# (3 целых числа, представляющих длину, ширину и высоту) и вместо этого 
# напечатать его поверхность. Пробелы должны быть заполнены с нуля.

 # формула  Площадь поверхности:    c = 2 * (a * b + b * c + a * b)

# a = int(input())
# b = int(input())
# c = int(input())
# surface = 2 * (a * b + b * c + a * c)
# print(surface) 


################################################################
#################################################################

               ### Аргументы Sep и end печати ###

# print('Chip ', ' Dale', sep='&')
# print('Chip ', ' Dale ', ' dame', sep="and")

#print('Gadget', 'Hackwrench', sep=' ')
# # Gadget Hackwrench

# print('Gadget', 'Hackwrench')
# # Gadget Hackwrench

# print(13, ' th', sep='')

#print('Tick-Toc', end=' the ')
# print('Crocodil', end='e')
# Tick-Tock the Crocodile


#characters = ('Humphrey the Bear','Spike the Bee','Fat Cat',)
#print(*characters)
#print('Humphrey the Bear', ' Spike the Bee ','Fat Cat', sep='')

# name = ['M', 'A', 'R', 'C', 'O']

# print(*name, sep='-', end="!")

# print(*name, sep='-', end='!')

#name = ['J', 'o', 'h', 'n']
#print(' '.join(name) + '!')

####################################################################
####################################################################

# numbers = [int(x) for x in input().split()]
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(*numbers, sep="")

#print(input().replace(' ', ''))


# txt = "welcome to the jungle"
# x = txt.split()
# print(x)


# txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 1)
# print(x)


######################################################################
#####################################################################

# adj = "Good"
# part_of_day = "morning"
# comma = ","
# title = "Ms."
# surname = "Johnson"

# print(f"{adj} {part_of_day}{comma} {title} {surname}!")

#print(adj, part_of_day + comma, title, surname, end="!")


######################################################################
#######################################################################
#######################################################################


#earnest = input()
#print(*earnest, sep=" ")

               ####   Межбуквенный интервал   ####

# Давайте сделаем форматирование текста. Прочитайте входное слово и 
# напечатайте его с указанным количеством пробелов между буквами. 
# Есть два разных ввода: слово в первой строке и количество пробелов 
# во второй строке.




# name = input()
# number = int(input()) 
# print(*name, sep=" " * number)


# print(*input(), sep=int(input()) * ' ')


# word = input()
# spaces = ' ' * int(input())
# print(*word, sep=spaces)



####################################################################
#################################################################



#print('a', 'b', 'c', sep='_', end='_')
#print('a', 'c', sep='_b_', end='_')
#print('a','_','b','_','c', end='_')


######################################################################
######################################################################


# poem = ['The night', 'the pharmacy', 'the street', 'the pointless lamppost in the mist']
# print(*poem, sep=', ', end='.')



# line1 = "Night, square, apothecary, lantern,"
# line2 = "Its meaningless and pallid light."
# line3 = "Return a half a lifetime after – "
# line4 = "All will remain. A scapeless rite."
# print(line1, line2, line3, line4, sep="\n")


#####################################################################
######################################################################



# Earned_amount ={
#     'Bubblegum': 202,
#     'Toffee': 118, 
#     'Ice cream': 2250,
#     'Milk chocolate': 1680,
#     'Doughnut': 1075,
#     'Pancake': 80,
# }
# print('Earned_amount: ')
# for item, price in Earned_amount.items():
#    print(f"{item}: ${price}")
# print(f"\nIncome: {sum(Earned_amount.values())}")
 
# staff = {
#     'Cleaner': 850,
#     'Vendor': 1120,
#     'Manager': 1300,
#     'Loader': 900,
# }
# print(f"Staff expenses: \n>${sum(staff.values())}")
 
# other_expenses = {
#     'Electricity': 100,
#     'Municipal Service': 90,
#     'Security': 30,
#     }
# print(f"Other expenses: \n>${sum(other_expenses.values())}")
 
# net_income = sum(Earned_amount.values()) - sum(staff.values()) - sum(other_expenses.values())
# print('Net income: $',float(net_income), sep='')


########################################################################################
####################################################################################


# earned_amount = {
# 'Bubblegum': 202,
# 'Toffee': 118,
# 'Ice cream': 2250,
# 'Milk chocolate': 1680,
# 'Doughnut': 1075,
# 'Pancake': 80
# }