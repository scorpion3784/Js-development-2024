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



args = (2,'No such file or directory')
Attribute characters_written not accessible.
errno = 2
filename = myfile.txt
filename2 = None
strerror = No such file or directory
winerror = None
with traceback = <built-in method with traceback of
   FileNotFoundError object at Ox0000000003416DC8>





