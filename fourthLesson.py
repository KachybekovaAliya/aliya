# import math as mt
# # exit() code working till this moment 
# num1 = 5.83
# # print(mt.ceil(num1))
# num2 = round(num1, 2)

# num3 = mt.ceil(num1,)

# num4 = mt.floor(num1)

# num5 = mt.radians(30)


# num6 = mt.degrees(0.5235987755982988)
# num7 = mt.pow(3, 2)  # ** 3**2=9
# num8 = mt.sqrt(81)   # 81 ** 0.5

# print(num2, num3, num4)
# print(num5) 
# print(num6)
# print(num7)
# print(num8)

# name1, name2, name3 = "Jack", "Bob", "Alice"
# print(name2)
# print(max(2, 3, 6, 8, 34, 800, 789)) # choosing the biggest number
# print(min(2, 4, 937, 1, -3)) # coosing the smallest number

# student1 = ["Tom", 29, True, "male", "bank"]
# numbers = [1, 2, 3, 4, 5]
# people = ["Tom", "Sam", "Bob", "Tobey", "Kate", "Ruki", "Simon", "Lily"]
# people.append("Rob")    #  adding element in the end of the list
# # len_list = len(people)
# # print(len_list)
# # people[-1] = "Tom"
# people.insert(0, "Alex")
# people2 = ["Sara", " Roma", "Lolla"]
# people.extend(people2)
# people.remove("Tom")
# people2.clear()
# KateIndex = people.index("Kate")
# print(KateIndex)
# people[4] = "Trina"
# print(people2)
# print(people)


# slice_people = people[:-2]   # [start:stop:step]
# print(slice_people)
# slice_people.reverse()
# name_list = [people[0]] *10
# prist_list = [people[2]] *10
# people[0] = "Jack"
# student1[1] = type(float)
# print(student1)
# print(people)
# print(name_list)
# print(prist_list)

# age = int(input("Enter your age:"))
# a = age %10 == 0 and age >= 50 when we have "AND" both reqirements should be considered 
# print(a)

# age = int(input("Enter your age:"))
# a = age %10 == 0 or age >= 50 When we have "OR" that means it consider one of the reqierments 
# print(a)

# name = "Sara"
# if name == "Bob":
#     print("It's male")
# else:
#     print("It's female")

# a = int(input("Enter a nimber:"))
# if (a > 0) or (5 == a):
#     print("Positive")
# elif a == 0:
#     print("Zero")
# else:
#     print("Negative")

# print(f"person is older than 15 years old!", {person == "student"}, {person == "10th grade"}, {person == "11th grade"}) sample of another idea
# person = input("status of person:")
# if person == "student" or person == "10th grade" or person == "11th grade":
#     print(f"person is older than 15 years old!, Because {person}") 
# else:
#     print("This person is under 15 years old")

 
# age = input("Enter your age:")
# if age < 13:
#     print("Baby")
# elif age < 18:
#     print("Teenager")
# elif age >= 18 and age < 50:
#     print("Adult")
# elif age >= 50 and age <200:
#     print("Pensioner")
# else:
#     print("incorrect value")

# try:
#     age = int(age)
# except:
#     print("Incorrect value")

list = ["Sonya", "Tim", "Kate", "Bella", "Jack"]
if "Sahsa" in list:
    print("Yes, He in the list")
    print(list)
else:
    print("He is not in the list")
    list.append("Sasha")
    print("Now he is", list)
