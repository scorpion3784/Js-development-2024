# LetterNum = 1
# for Letter in "Привет":
#    print("Бyквa ", LetterNum, "будет", Letter)
#    LetterNum 
#    LetterNum+=1;



# Value = input("Введите менее 6 символов: ")
# LetterNum = 1
# for Letter in Value:
#    print ("Буква ", LetterNum," будет ", Letter)
#    LetterNum+=1
#    if LetterNum > 6:
#       print ("Строка слишком длинная!")
#       break;
  
  
# LetterNum = 1
# for Letter in "Привет":
#    if Letter =="и":
#       continue
#    print("Haйдeнo и, не обработано.")
#    print("Бyквa ", LetterNum," будет ", Letter)
#    LetterNum+=1  



# LetterNum = 1
# for Letter in "Привет":
#    if Letter == "и":
#       pass
#       print ("Naideno и, не обработано.")
#    print("Буква ", LetterNum, "будет", Letter)
#    LetterNum+=1;


# Value = input ("Введите менее 6 символов: ")
# LetterNum = 1
# for Letter in Value:
#    print ("Буква ", LetterNum," будет ", Letter)
#    LetterNum=1
# else:
#    print("Cтpoкa пуста.")



# X = 1
# Y = 1
# print('{:>4}' .format(' ') , end= '')
# for X in range(1, 11):
#    print('{:>4}'.format(X), end='')
# print()
# for X in range(1, 11):
#    print('{:>4}'.format(X), end='')
#    while Y <= 10:
#       print('{:>4}'.format( X * Y), end='')
#       Y+=1
#    print ()
#    Y=1


#print(mi_to_km(mi, km))





scores = input()
correct = 0
wrong = 0
for i in scores:
    if i == 'C':
        correct += 1
    elif i == 'I':
        wrong += 1
        if wrong >= 3:
            print(f"Game over\n {len({correct})}")
            break
else:
    print(f"You won\n {len(correct)}") 

# print("Игра: Вставь пропущенную букву")
# print("Вставьте пропущенные буквы в следующее слово:")
# print("С_рен_венький")
# x = input("Первая буква:")
# if x == "i":
#     print("Отлично, продолжаем!")
# else:
#     print("GAME OVER")
# y = input("Вторая буква:")
# if y == "e":
#     print("Прекрасно, вы справились!!!")
# else:
#     print("GAME OVER")