# num1 = input("Enter divider:")
# num2 = input("Enter dividend:")
# try:
#     num1 = int(num1)
#     num2 = int(num2)
#     num3 = num1 / num2
#     print("Result ov devision:", num3)
#     if num3 <= 5:
#         print("num3 less than 5")
#     elif num3 > 5 and num3 < 10:
#         print("num3 begger than 5")
#     else:
#         print("num3 begger or eqal to 10")
# except: 
#     print("Enter correct numbers")
# finally: 
#     print("Block 'try' end action")
#     print("end of the program")

# word = "people"
# text = "Hello, my name is Aliya"
# list = [1, 2, 3, 4, 5, 6]

# slice_word = word[2] # slice is working on "str" also
# print(slice_word)

# search = "name"
# if search in text or search in list:
#     print(f"{search} is in the text!")
# else:
#     print(f"{search} is not in the text")
# if search in list:
#     print(f"{search} is in the list!")
# else:
#     print(f"{search} is not in the list")

# num1 = int(input("Enter a number:"))
# if num1 % 2:
#     print("Even")
# else: 
#     print("odd")


# Python easy tasks

# A = int(input("Enter your number:"))
# if A > 0:
#     print("A is possitive TRUE")
# elif A == 0:
#     print("A is zero FALSE")
# else:
#     print("A is negative FALSE")

# if A % 2:
#     print("A is even. FALSE")
# else: 
#     print("A is odd. TRUE")


# if A % 2:
#     print("A is even. True")
# else: 
#     print("A is odd. False")

# B = int(input("Enter your number:"))
# if A > 2 and B <= 3:
#     print("TRUE")
# else:
#     print("WRONG") 


# print(A > 2 and B <= 3)

# C = int(input("Enter your number:"))
# print(A<B<C)

# print(A<B<C)

# if A % 2 and B % 2:
#     print("TRUE")
# else: 
#     print("FALSE")

# if A % 2  or B % 2:
#     print("TRUE")
# else: 
#     print("FALSE")

# if A % 2  and B % 2:
#     print("FLASE")
# elif A % 2  or B % 2: 
#     print("TRUE")
# else:
#     print("Non of them is odd")

# word = "people"
# new_word = word.lower() 
# print(new_word)

# .upper make each letter in word capital
# .lower make eachb letter small
# .capitalize ,ake word beginning from Capital letter

# word = "milk"
# list = ["milk", "egg", "bread", "sugar"]
# if word in list:
#     new_word = word.replace('milk', 'Cookies')
#     print(new_word)

# # .replace(old, new) is replacing old objects to new obgects 
# name = "Aliya"
# name1 = name.swapcase()
# print(name1)
#  .swapcase is changing all letters after first one to cappital

# name2 = name.strip()
# print(name2) 

# strip([chars])
# Удаляет пробелы и указанные символы chars в начале и конце строки.

# split([separator])
# Разбивает строку на список подстрок по указанному разделителю separator.
# Если разделитель не указан, используется пробел.

# index(substring)
# Возвращает индекс первого вхождения подстроки substring.
# Если подстрока не найдена, выбрасывает ошибку.

# len(string) Возвращает длину строки string.

# Seminar 3 
# task 1
# a = str(32)
# b = str(3.5)
# x = str(True)

# # task 2
# str_ = input("Enter something:")

# # task 3
# name = input("Write your name: ")
# surname = input("Write your surname: ")

# # task 4
# res = name + " " + surname
# print(res)
# # Task 5 
# name = input("Write your name: ")
# score = input("Enter your score: ")
# print(f"Hello, {name}! Your score is {score}")

# # task 6 
# age = input("Enter your age: ")
# print(f"My name is {name}, and i am {age} years.")

# task7 
# python = 'Python is easy'
# sp = python[0]
# print(sp)
# sp1 = python[-1]
# print(sp1)
# sp2 = python[:2]
# print(sp2)
# sp3 = python[-3:]
# print(sp3)
# sp4 = python[2:5]
# print(sp4)
# sp5 = python[1:9]
# print(sp5)
# sp6 = python[1:-1]
# print(sp6)
# sp7 = python[::2]
# print(sp7)
# sp8 = python[1::2]
# print(sp8)
# sp9 = python[::-1]
# print(sp9)
# sp10 = python[4:1:-1]
# print(sp10)
# sp11 = python[::-2]
# print(sp11)

# Task 8 
# ppl = "PythonProgrammingLanguage"
# ppl1 = ppl[:6]
# ppl2 = ppl[17:]
# print(f"{ppl1} {ppl2}")

# task 9 
# love = "I love Python programming!"
# sl1 = love.replace("Python", "Java")
# print(sl1)

# task 10
# name = input("Enter your name: ")
# name1= (f"Hi, {name.capitalize()}!")
# print(name1)

# task 11
# code = 'atgcaagttgacaattta'
# code1 = code.upper()
# print(code1)

# task 12
# code = 'augcaagugacaauuua'
# code1= code.replace("u", "t")
# print(code1)

# task 13 
# nun_phone = '   +7(919)-@784-54_18@@     ' 
# nun_right = nun_phone.strip().replace('@', '').replace('_', '')
# print(nun_right)

# task 14
# str_ = '67dg#uin_87' 
# lenght = len(str_)
# index = str_.index('#')
# print("Длинна строки:", lenght)
# print("Индекс символа '#' :", index)

# task 15
name = input("Enter your name: ")
name1 = name.capitalize()
text = """ Имя этого героя "name". Поход в театр для него целый ритуал. Входя в фойе, "name" демонстративно снимает шляпу, поправляет галстук и вешает
ольто на руку. Он непременно думает, что все, кому он знаком говорят про себя: "Ах, сегодня "name" неотразим!" После чего "name"
занимает лучшее место бенуара и с важным видом достает очки."""
text2 = text.replace('"name"', name1)
print(text2)
