# import datetime
# print(datetime.datetime.now())
# print(ord("N"))   



                  # Function & Argument



# def hello(sss):
#     print(sss)
# hello("rrrrrrrrr")

# def hello2(gree):
#     print(gree)
# hello2("dfhdhdhdgh")
# hello2(123+45)

# def AddIt(Valuel, Value2):
#     print(Valuel, "+", Value2, "=",Valuel + Value2)
# AddIt(Value2=4, Valuel=5)

# def hello3(greeting = "Znacenie Otsustvuet"):
#     print(greeting)
# hello3()

# def Hello4 (ArgCount, *VarArgs):
#     print ("Передано аргументов: ", ArgCount)
#     for Arg in VarArgs:
#        print (Arg)
# Hello4(3,"odin","dva","tri")


# def DoAdd(Valuel, Value2):
#     return Valuel + Value2
# print("Сумма значений 3 + 4 равnа ", DoAdd(3, 4))
# print ("3 + 4 равио 2 + 5 бу­деt", (DoAdd (3, 4) == DoAdd(2, 5)))

# Name = input ("Укажите свое имя: ")
# print("Привет, ", Name )

# ANumber = float ( input ("Введите число: " ))
# print ( "Bы ввели: ", ANumber)



            #  if, if...else,  if...elif

# TestMe = 6
# if TestMe == 6:
#    print("Значение переменной TestMe равно 6!");
#    print("Завершено!");


# Value = int(input("Bвeдитe число от 1 до 10: "))
# if (Value > 0) and (Value <= 10):
#    print("Bы ввели: ", Value);


# Value = int(input("Bвeдитe число от 1 до 10: "))
# if (Value > 0) and (Value <= 10):
#    print ("Вы ввели: ", Value)
# else:
#    print("Введенное значение некорректно!");



# print("l. Красный")
# print ( "2. Оранжевый")
# print("З. Желтый")
# print ("4. Зеленый")
# print("S. Синий")
# print ("6. Пурпурный")
# Choice = int(input("Bыбepитe ваш любимый цвет:"))
# if (Choice == 1):
# print("Bы выбрали красный цветl")
# elif (Choice -- 2) :
# print("Bы выбрали оранжевый цвет 1 ")
# elif (Choice -- 3) :
# print("Bы выбрали желтый цвет'")
# elif (Choice -- 4) :
# print("Bы выбрали зеленый цвет!")
# elif (Choice -- 5) :
# print("Bы выбрали синий цвет 1 ")
# elif (Choice -- 6) :
# print("Bы выбрали пурпурный цвет!")
# else:
# print("Bы сделали неверный выбор!")



# One = int (input("Bвeдитe число от 1 до 10: "))
# Two = int ( input ("Введите число от 1 до 10: ") )
# if(One >= 1) and (One <=10):
#   if (Two >= 1) and (Two <= 10):
#    print ("Ваш секретный номер: ", One * Two)
#   else:
#    print("Bтopoe значение некорректно!")
# else:
#    print("Пepвoe значение некорректно!");




print("l. Яичница")
print("2. Блинчики с творогом")
print("3. Бельгийские вафли")
print("4. Овсяная каша")
MainChoice = int (input ("Выберите блюдо на завтрак: ") )
if (MainChoice == 2):
   Meal = "блинчики с творогом"
elif (MainChoice == 3):
   Meal = "бельгийские вафли"
if (MainChoice == 1):
   print("l. Бутерброд с ветчиной")
   print("2. Бутерброд с сыром")
   print ("3. Бутерброд с рыбой")
   print("4. Бутерброд с салом")
   Bread = int(input("Bыбepитe бутерброд: "))
   if (Bread == 1):
      print("Bы выбрали яичницу и бутерброд с ветчиной.")
   elif (Bread == 2) :
      print("Bы выбрали яичницу и бутерброд с сыром.")
   elif (Bread == 3) :
      print("Bы выбрали яичницу и бутерброд с рыбой.")
   elif (Bread == 4) :
      print("Bы выбрали яичницу и бутерброд с салом.")
   else:
      print("Y нас есть яичница, но нет такого бутерброда.")
elif (MainChoice == 2) or (MainChoice == 3):
   print("l. Сироп")
   print ( "2. Клубника")
   print("3. Сахарная пудра")
   Topping = int(input("Bыбepитe десерт:"))
   if (Topping == 1) :
      print ("Вы выбрали " + Meal + " с сиропом. ")
   elif (Topping == 2):
      print ("Вы выбрали " + Meal + " с клубникой. ")
   elif (Topping == 3):
      print ("Вы выбрали " + Meal + " с сахарной пудрой.")
   else:
      print ("У нас есть " + Meal + ", но нет такого десерта.")
elif (MainChoice == 4):
   print ("Вы выбрали овсяную кашу.")
else:
      print("Y нас нет этого блюда на завтрак!")      