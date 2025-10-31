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
# name = input("Enter your name: ")
# name1 = name.capitalize()
# text = """ Имя этого героя "name". Поход в театр для него целый ритуал. Входя в фойе, "name" демонстративно снимает шляпу, поправляет галстук и вешает
# ольто на руку. Он непременно думает, что все, кому он знаком говорят про себя: "Ах, сегодня "name" неотразим!" После чего "name"
# занимает лучшее место бенуара и с важным видом достает очки."""
# text2 = text.replace('"name"', name1)
# print(text2)

# task 16
# str_ = '84hj#55hjl'
# str1 = str_.replace('#', '#abc')
# print(str1)

# task 16.2
# str_ = '84hj#55hjl'
# str1 = str_[0:5]
# str2 = str_[5:]
# str3 = str1 + 'abc' + str2 
# print(str3)

#  task17
# tel = '0777784500'
# format = f"+996 ({tel[1:4]}){tel[4:7]}-{tel[7:]}"
# print(format)

# task 18
# str_ = input('Write something: ')
# try:
#     if str_ [5]:
#         print("Too long")
# except:
#     if str_ [0]:
#         print(str_)

# task 19
# str_ = input('Write password: ')
# try:
#     if str_ [5]:
#         print('Too long!')
#         str_new = input("try again:")
#         print(str_new)
# except:
#     if str_ [0]:
#         print(str_)

# ADDITION TO TASK

# str_1 = input('Confirm password: ')
# try:
#     if str_1 [5]:
#         print('Too long!')
#         str_new1 = input("try again:")
#         print(str_new1)
# except:
#     if str_ [0]:
#         print(str_1)

# if str_ == str_1 or str_new == str_1 or str_new == str_new1 or str_ == str_new1:
#     print("Password saved!")
# else:
#     print("not match!")
# task 20
# password = input("Create your password:")
# if '#' in password or '@' in password or '%' in password:
#     print(password)
# else:
#     print("Password is unreliable")

# task 21
# password = input("Create your password:")
# if '#' in password or '@' in password or '%' in password:
#         print(f"Password '{password}' saved!")
# elif '#' not in password or '@' not in password or '%' not in password:
#         password2 = input("Invalid password. Please re-enter:")
# if '#' in password2 or '@' in password2 or '%' in password2:
#         print(password2)
# else:
#         print("You have exhausted the number of attempts!")

# task 22
# list = 'айданургулсайкалаймээржылдызбакытайчолпонмадинажаныбекбекжолдостукэлиябатыржанаталмазбекчингизталанталтынбекмаратсаматтайырбеказаматбекмуратасанбек'
# yn = input("Enter your name: ")
# if yn in list:
#     print("Поздравляю, вам положена повышенная стипендия.")
# else:
#     print("Увы, Вашего имени в списке нет")

# task 23
# code = 'GGGGGGGGGAATTATGATCCTTACTTT'
# index = code.index('G')
# if index == 0:
#     code1 = code[0:1].replace('G', 'A')
#     print(code1 + code[1:])
# else:
#     print(code)
# if index > 5 in code:
#     code2 = code.append("G")
#     print(code2)
# else:
#     print(code)

# task 24
# names = input('Write names:')
# names1 = names[:6] 
# names2 = names[6:]
# names3= names1 + '\n' + names2 
# print(names3)

# task 25 
prod_name = input("Enter name of product: ")
old_price = input("Enter old price of product")
new_price = input("Enter new price product: ")



