# try:
#     Value = int(input("Bвeдитe число от 1 до 10: "))
# except ValueError:
#     print("Hyжнo ввести число от 1 до 10!")
# else:
#     if (Value > 0) and (Value <= 10):
#        print("Bы ввели: ", Value)
#     else:
#         print("Введенное значение некорректно!");


# try:
#    Value = int(input("Bвeдитe число от 1 до 10: "))
# except:
#    print("Обобщенная ошибка!")
# except ValueError:
#    print("Hyжнo ввести число от 1 до 10!")
# else:
#     if (Value > 0) and (Value <= 10):
#       print("Bы ввели: ", Value)
#     else:
#       print("Введенное значение некорректно!")




# try:
#    Value = int(input("Bвeдитe число от 1 до 10: "))
# except ValueError:
#    print("Hyжнo ввести число от 1 до 10!")
# except:
#    print("Обобщенная ошибка!")
# else:
#    if (Value > 0) and (Value <= 10):
#       print("Bы ввели: ", Value)
#    else:
#       print("Введенное значение некорректно!")




# import sys
# try:
#    File = open('myfile.txt')
# except IOError as e:
#    print("Ошибка при открытии файлаl\r\n" +
#       "Номер ошибки: (0} \r\n". format (e. errno) +
#       "Текст ошибки: {0}". format (e. strerror))
# else:
#    print("Фaйл открыт, как ожидалось.")
#    File. close ();
   
   
   
   
# import sys
# try:
#    File = open('myfile.txt')
# except IOError as е:
#    for Arg in e.args:
#       print(Arg)
# else:
#    print("Фaйл открыт, как ожидалось.")
#    File.close(); 

# import sys
# try:
#    File = open('myfile.txt')
# except IOError as e:
#    for Entry in dir(e):
#       if (not Entry.startswith("_")):
#          try:
#            print (Entry,"=",e.__getattribute__(Entry))
#          except AttributeError:
#             print("Атрибут ", Entry, "недоступен.")
# else:
#    print("Фaйл открыт, как ожидалось.")
#    File.close();



# args = (2,'No such file or directory')
# Attribute characters_written not accessible.
# errno = 2
# filename = myfile.txt
# filename2 = None
# strerror = No such file or directory
# winerror = None
# with traceback = <built-in method with traceback of
#    FileNotFoundError object at Ox0000000003416DC8>





             #  PYTHON na Hyperskill.org


# print("This is the first line.\nThis is the second line.")
# print()
# print("This is the first line "+
#       "This is the second line.")

# print('''Shopping List:
# 1. Apples
# 2. Bread
# 3. Milk''')


# print("""The only limit to our realization of tomorrow,
# is our doubts of today.
# Franklin D. Roosevelt""")


# print("Yes, I'm ready to learn Python.")

# print('Yes, "I am ready to learn Python."')

# print('I can\'t attend the meeting tomorrow.')

# print (-3.14)
# print(type(-3.14))

# city = "Kiev"
# print(city)
# print(type(city))

# city = "Kiev"
# print(city)
# print(type("Kiev"))

# _55 = "odessa"
# print(_55)
# print(type("odessa"))




# cost_1 = 500
# cost_2 = 400
# _2tal_cost = 900
# print(_2tal_cost)


# age_of_mike = 5
# print(age_of_mike)


# a = 5
# b = 4

# print("The sum of a and b is", a + b)
# print("The product of a and b is", a * b)
# print("The product of a and b is", 5 * 4)

# total_money = 20
# cost = 10
# print(total_money - cost)

# first_month = 200
# Second_moth = 150
# Third_moth = 250
# total_savings = first_month + Second_moth + Third_moth
# print(total_savings)

# total_savings = 150 + 200 + 250
# print(150 + 200 + 250)


# length = 5
# width = 5
# print(length * width)

# print(type(4 + 3))
# print(type(4 - 3))
# print(type(4 * 3))
# print(type(4 / 3))

# print(type(4 / 2))
# print(12 / 3)

# print(7 / 2)
# print(7 // 2)


# sum = 1500
# spend = 600 + 300 + 200
# result = (sum - spend)
# print(result // 25)



# Initial_height = 2
# Number_of_Days = 4
# print(Initial_height ** Number_of_Days)

# a = 2
# b = 4
# print(a**b)


# volume  = 4 ** 3
# print(volume)


# print(15-(15//6)*6) # =3
# print(7//3)        # =2
# print(7-(7//3 )*3) # =1


# print(25-(25//2)*2) same
# print(25 % 2)       same

# print(20 % 2)  same
# print(20-(20//2)*2)   same


# print(62 % 12)

# total_chocolates = 15
# num_children = 4
# counts = total_chocolates % num_children
# print(counts)

#print((5 + 3) - 6**2 / 3)

# print(856 // 60) get hours
#print(856 % 60)  get minute



############################################################################

#("Formula for calculating  value of the investment (a), "+
# use anual inerest (r), sum  of invest ($x), and for how many years (y).")

# x = 1000
# r = 5
# y = 12
# a = x *(1 + r/100)**12
# print(a)


            #  calculate the income from a savings account #
            
# amount = 1000
# interest_rate = 5
# years = 1
# income =(amount * interest_rate * years) / 100
# print(income)




               #  Convert 24 time hours to 12 time hours #
       
# def convert24(str1): 
    
#     # Checking if last two elements of time 
#     # is AM and first two elements are 12 
#     if str1[-2:] == "AM" and str1[:2] == "12": 
#         return "00" + str1[2:-2] 
        
#     # remove the AM     
#     elif str1[-2:] == "AM": 
#         return str1[:-2] 
    
#     # Checking if last two elements of time 
#     # is PM and first two elements are 12 
#     elif str1[-2:] == "PM" and str1[:2] == "12": 
#         return str1[:-2] 
        
#     else: 
        
#         # add 12 to hours and remove PM 
#         return str(int(str1[:2]) + 12) + str1[2:8] 

# # Driver Code         
# print(convert24("08:05:45 PM"))   
############################################################################


                        
                    # TASK
                    
# Task for python is value 24-hour convert to a 12-hour format and print the result.There are 4 cases you need to handle:
# hour == 0 should convert to 12AM
# hour < 12 stays the same and gets the AM modifier
# hour == 12 converts to 12PM
# hour > 12 subtrace 12 and add the PM modifier


                            # ANSWER
# hour = 24
# hour = (hour % 12) + 1
# if hour == 0:
#     print('12AM')
# elif hour < 12:
#     print(f'{hour}AM')
# elif hour == 12:
#     print('12PM')
# else:
#     print(f'{hour-12}PM')



############################################################################

# def converter(hour, mode=0,AM_or_PM='AM'):



    # """ Mode here refers to the 12 hour mode or the 24 hour mode.
    # If mode ==0, then it refers to the time given in 12 hour mode, thus converting to military mode (24 hour mode).
    # If mode ==1, then it refers to the 24 hour mode, thus converting to standard mode (12 hour mode).
    # Must provide the mode argument.

    # AM_or_PM here indicates whether a 12-hour cycle time given is AM or PM
    # """
    
    
    
    # if mode==0:
    #     if AM_or_PM == 'PM':
    #         return str(hour+12)
    #     else:
    #         return str(hour)
    # elif mode == 1:
    #     if hour ==0:
    #        return f'12AM'
    #     elif hour < 12:
    #        return f'{hour}AM'
    #     elif hour >= 12:
    #        return f'{hour}PM'
    # return str(hour)


# import datetime as dt

# time1 = dt.datetime(2024, 3, 24, 2, 4, 3, 1).strftime('%H%p')
# print(time1)
# now = dt.datetime.now().strftime('%H%p')
# print(now)

###############################################################################

#hour = 24
#print(hour % 12)

############################################################################

# temperature = 30
# if temperature > 75:
#     print("It's a hot day!")
# else:
#     print("It's not too hot today.")



             # код для вычисления площади круга: # 
    
# PI = 3.14159
# radius = 3
# AREA = PI * radius**2
# print(AREA)

########################################################################

#   программа ниже считывает имя пользователя и выводит приветствие.

# user_name = input();
# print('Hello, ' + user_name);

# age = input()
# print('Your age is ' + age)

# nick_name = input()
# print("Welcome back " + nick_name + "!")

# user_name = input('Please, enter your name: ')
# print('Hello, ' + user_name)


# print('Enter your name: ')
# user_name = input()
# print('Hello, ' + user_name)


# print("Enter your age:")
# age = input()
# print("Your age is " + age)


# dummy_variable = input("Enter some dummy value: ")
# print("Warning: Oh, cmon, you are taking too long")


# city = input("Insert the city you currently live in: ")
# country = input("Insert the country you currently live in: ")
# print("You live in " + city + ", " + country)
# zip_code = input("Insert your ZIP code: ")

# #  if you want inpur just number integer, code is below

# zip_code = int(input("Insert your ZIP code: "))



# user_name = input()
# user_profession = input()
# print("My name is " + user_name + " and I am a " + user_profession)


# or ############

# print("Hello " + user_name + "!" + " You are Great " + user_profession)

####     This is same But Shorter and Better ##########

# print(f"My name is {input()} and I am a {input()}")

######################################################################################

      #     преобразовать входные значения в целые числа.########
                          
# num_1 = int(input())
# num_2 = int(input())
# print(num_1 + num_2)



# # the average amount of money per month
# money = int(input("How much money do you spend per month: "))

# # the number of miles per unit of money
# n_miles = 2

# # earned miles
# miles_per_month = money * n_miles

# # the distance between London and Paris
# distance = 215

# # how many months do you need to get
# # a free trip from London to Paris and back
# print(distance * 2 / miles_per_month )




                         # Compound assignment operators  #
                         
# capital = int(input("Enter your capital: "))
# capital = capital * 0.8
# additional_income = 1000
# capital = capital + additional_income
# print(capital)


 # can be shortened and become more readable #

     
# capital = int(input("Enter your capital: "))
# capital *= 0.8
# additional_income = 1000
# capital += additional_income 
# print(capital)      