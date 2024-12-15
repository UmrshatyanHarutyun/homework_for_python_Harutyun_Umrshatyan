# # խնդիր 1
# # x=int(input("Մուտքագրեք թիվ 1։  "))
# # y=int(input("մուտքագրեք թիվ 2։  "))
# # if x>y:
# #     print(x)
# # elif x<y:
# #     print(y)
# # else:
# #     print("Equal")

# # խնդիր 2
# # first_persons_name=str(input("please enter first person's name: "))
# # first_persons_age=int(input("please enter first person's age: "))
# # second_persons_name=input(("please enter second person's name: "))
# # second_persons_age=int(input("please enter second person's age: "))
# # third_persons_name=input(("please enter third person's name: "))
# # third_persons_age=int(input("please enter third person's age: "))

# # if max(first_persons_age,second_persons_age,third_persons_age)==first_persons_age and min(first_persons_age,second_persons_age,third_persons_age)==second_persons_age:
# #     print(f"The oldest one is {first_persons_name}.\nThe youngest one is {second_persons_name}.")
# # elif max(first_persons_age,second_persons_age,third_persons_age)==first_persons_age and min(first_persons_age,second_persons_age,third_persons_age)==third_persons_age:
# #     print(f"The oldest one is {first_persons_name}.\nThe youngest one is {third_persons_name}.")
# # elif max(first_persons_age,second_persons_age,third_persons_age)==second_persons_age and min(first_persons_age,second_persons_age,third_persons_age)==first_persons_age:
# #     print(f"The oldest one is {second_persons_name}.\nThe youngest one is {first_persons_name}.")
# # elif max(first_persons_age,second_persons_age,third_persons_age)==second_persons_age and min(first_persons_age,second_persons_age,third_persons_age)==third_persons_age:
# #     print(f"The oldest one is {second_persons_name}.\nThe youngest one is {third_persons_name}.")
# # elif max(first_persons_age,second_persons_age,third_persons_age)==third_persons_age and min(first_persons_age,second_persons_age,third_persons_age)==first_persons_age:
# #     print(f"The oldest one is {third_persons_name}.\nThe youngest one is {first_persons_name}.")
# # else:
# #     print(f"The oldest one is {third_persons_name}.\nThe youngest one is {second_persons_name}.")

# # խնդիր 3
# # x=int(input("Խնդրում եմ մուտքագրել քառանիշ թիվ։  "))
# # a=x//1000
# # b=x%1000//100
# # c=x%1000%100//10
# # d=x%1000%100%10
# # print(int(f"{d}{c}{b}{a}"))

# # խնդիր 4
# age=int(input("please enter the age: "))
# if age<=20 or age>=60:
#     print("Error")
# else:    
#     male=input("please enter the male M or W: ")
#     status=input("please enter the marital status Y or N:")
#     if male=="W":
#         print("Work only in urban areas")
#     elif male=="M" and age>20 and age<40:
#         print("Work in everywhere")
#     elif male=="M" and age>=40 and age<60:    
#         print("Work only in urban areas")
#     else:
#         print("Error")    


# # խնդիր 5
# import random
# import time
# name=input(f"please enter your name for new game: ".upper())
# time.sleep(0.5)
# print(f"Welcome to our game dear {name}".upper())
# time.sleep(0.5)
# result=input('If you are ready please enter Yes if you are not No: ').lower()
# if result=="yes":
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print("----Game is starting----")
#     time.sleep(2)
#     a='✊'
#     b='✋'
#     c='✌️'
#     pc_result = random.choice([a, b, c])
#     user_result = input("Please enter:\n a = ✊\n b = ✋\n c = ✌️\n")
#     time.sleep(0.5)
#     print(f"Pc choose= {pc_result}")
#     if user_result=="a":
#         user_result=a
#         time.sleep(0.5)
#         print(f"User choose=: {a}")
#     elif user_result=="b":
#         user_result=b
#         time.sleep(0.5)
#         print(f"User choose=: {b}")
#     else:
#         user_result=c
#         time.sleep(0.5)
#         print(f"User choose=: {c}")
#     if  pc_result==user_result:
#         time.sleep(0.5)
#         print("###### Its is draw ######")
#     elif user_result==a and pc_result==b:
#         time.sleep(0.5)
#         print("####### PC win ######")
#     elif user_result==a and pc_result==c:
#         time.sleep(0.5)
#         print("####### User win ######")
#     elif user_result==b and pc_result==a:
#         time.sleep(0.5)
#         print("####### User win ######")
#     elif user_result==b and pc_result==c:
#         time.sleep(0.5)
#         print("####### PC win ######")
#     elif user_result==c and pc_result==a:
#         time.sleep(0.5)
#         print("####### PC win ######")
#     elif user_result==c and pc_result==b:
#         time.sleep(0.5)
#         print("####### User win ######")
#     else:
#         time.sleep(0.5)
#         print("Something went wrong")
#         time.sleep(1)    
#     print('###### END GAME ######')
# else:
#     time.sleep(1)
#     print('----------------------------- EXIT -----------------------------')    

# # խնդիր 6
# import random
# user_folkowers=int(input("please enter numer of your followers: "))
# pc_followers=random.randint(0,100000)
# print(f"{user_folkowers}\n{pc_followers}")
# if user_folkowers>pc_followers*1.2:
#     print("user is blogger")
# else:
#     print("pc is blogger")

# # խնդիր 7
# pc_time=3/60
# user_time=pc_time*1.1
# distance=12
# speed=distance/user_time
# print(f"User speed is {round(speed)} km/hour")

# խնդիր 35
# user_number=int(input("Please enter number: "))
# if user_number%2==0:
#     print("Number is even")
# else:    
#     print("Number is odd")

# խնդիր 36 դասին արել եմ

# խնդիր 37
# letter=input("please enter any letter: ")
# if letter in ("aeiou"):
#     print("the letter is vowel")
# elif letter=="y":
#     print("It can be both")
# else:
#     prin("the letter is unspokena")         

# խնդիր 42
# name=input("please enter octave name like C4: ")
# note=name[0]
# octave=int(name[1])
# if note=="A":
#     print(f"{440.00/2**(4-octave)}")
# else:
#     print(f"{440.00/2**(4-octave)}")

            




