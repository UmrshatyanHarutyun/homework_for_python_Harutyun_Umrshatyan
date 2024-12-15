#6.Цикл while
#խնդիր 1
# n=int(input("please enter number: "))
# i=1
# while i<=n:
#     print(f"{i}^3={i**3}",end=" ")
#     i=i+1
#     print()
#խնդիր 2
# name=input("ինչպե՞ս է Ձեր անունը: ")
# debt=int(input("Ձեր պարտքի չափն է: "))
# new_message=print(f"{name},Ձեր պարտքը կազմում է {debt} դրամ")
# while True:
#     transfer=int(input(f"ինչքա՞ն եք պատրաստ վճարել։ "))
#     if transfer<debt:
#         print(f"քիչ է հարգելի {name},խնդրում եմ կրկին փորձել",end=" ")
#         print()
#     else:
#         print(f"Ձեր պարտքը վճարված է {name},շնորհակալություն համագործակցության համար",end="")
#         break   
# print()     
#խնդիր 3
# n=int(input("please enter number: "))
# digit_count=0
# if n==0:
#     digit_count=1
# else:
#     n=abs(n)
#     while n>0:
#         digit_count+=1
#         n//=10
#     print(digit_count)        
#խնդիր 4
# count_positive=0
# count_negative=0
# while True:
#     rate=int(input("please enter rate from -100 to 100: "))
#     if 0>rate>=-100:
#         count_negative+=1
#     elif 0<rate<=100:
#         count_positive+=1
#     elif rate==0:
#         break
#     else:
#         print("please enter rate only from -100 to 100")
# print(f"negative rates count is {count_negative}")
# print(f"positive rates count is {count_positive}")
#խնդիր 5-ստեղ break-ը պարտադիրա՞
# task_form_upper=0
# count_accepted_call=0
# n=1
# while True:
#     if n<=8:
#         print(f"{n} hour")
#         n=n+1
#         task=int(input("how many program he will make: "))
#         task_form_upper+=task
#         wife_calls=input("will yo accept wifes call YES or NO: ").lower()
#         if wife_calls=="yes":
#             count_accepted_call+=1
#         else:
#             count_accepted_call+=0    
#     else:
#         print(f"workind day is over,and you have done {task_form_upper} tasks")
#         if count_accepted_call>0:
#             print("you need visit market")
#             break
#         else:
#             print("you don't need vist market")
#             break
# print()    
#խնդիր 6
# year=0
# x=int(input("pleae enter deposit amount: "))
# p=float(input("please neter deposit yearly percentage: "))
# y=int(input("pleae enter wished deposit amount after years: "))
# while True:
#     if x<=y:
#         x=x*(100+p)/100
#         year+=1
#     else:
#         print(f"you need {year} years to reach amount you need")
#         break
#խնդիր 7
# import random
# comp_number=random.randint(0,10)
# count_of_attempts=1
# while True:
#     childs_number=int(input("please enter number to guess from 0 to 10: "))
#     if childs_number==comp_number:
#         print(f"you guessed right number,you have tried {count_of_attempts} times.")
#         break
#     else:
#         if childs_number<comp_number:
#             print(f"your number is lower,please try agian")
#             count_of_attempts+=1
#         elif childs_number>comp_number:
#             print(f"your number is higher,please try agian")
#             count_of_attempts+=1
#խնդիր 8
# import random
# left=0
# right=100
# comp_attempts=1
# user_number=int(input("please enter number from 0 to 100: "))
# while True:
#     comp_number=int(random.randint(left,right))
#     print(f"your number is {comp_number}?")
#     user_answer=input("please enter < or > or =")
#     if user_answer=="=":
#         print("finally i guesss your number")
#         break
#     else:
#         if  user_answer=="<":
#             right=comp_number-1
#             comp_attempts+=1
#         elif user_answer==">":
#             left=comp_number+1
#             comp_attempts+=1
# print(f"i guess it after {comp_attempts} attempts")
#7.for_цикл со счетчиком
#խնդիր 1
# import random
# for _ in range(1,11):
#     n=int(random.randint(-100000,100000))
#     print(f"client number {n}")
#     if abs(n%2)==0:
#         print("cleint is overdue")
#     else:
#         print("client is normal")
#խնդիր 2
# sum_=0
# count=0
# month=1
# for _ in range(0,12):
#     salary=int(input(f"please enter {month} month's salary: "))
#     sum_+=salary
#     count+=1
#     month+=1
# print(f"Average salary is {sum_/count} dram")    
#խնդիր 3
# n=int(input("please enter number for factorial: "))
# k=1
# for i in range(1,n+1):
#     k*=i
# print(f"factorial for number {n} is {k}")

#խնդիր 4
# import random
# n=int(input("please enter count of։ "))
# count_3=0
# count_4=0
# count_5=0
# for i in range (0,n+1):
#     points=random.choice([3,4,5])
#     print(f"the {i} student point is {points}")
#     if points==3:
#         count_3+=1
#     elif points==4:
#         count_4+=1
#     else:
#         count_5+=1
# print(f"Count of students that have 3 point= {count_3}\nCount of students that have 4 point= {count_4}\nCount of students that have 5 point= {count_5}")
 #խնդիր 5
#a=int(input("please enter number 1: "))
# b=int(input("please enter number 2: "))
# count=0
# sum_=0
# for i in range(a,b+1):
#     if i%3==0:
#         count+=1
#         sum_+=i
# print(f"average is {sum_/count}")
#խնդիր 6 - ստուգել
# for i in range(10,100):
#     if 3*(i//10)*(i%10)==i:
#         print(i)
#խնդիր 7 - ստուգել
#         print(i)
# import random
# n=int(input("please enter number of cards"))
# summ=0
# summ_correct=0
# for i in range(1,n):
#     k=int(input(f"please enter kard number {i}= "))
#     summ+=k
# for j in range (1,n+1):
#     summ_correct+=j
# print(f"you have left card number {summ_correct-summ}")

#9.Цикл for: работа со строками
#խնդիր 1
# days=["monday","thesday","wensday","thursday","friday","saturday","sunday"]
# day=input("please enter the day: ").lower()
# day_number=0
# for i in range(0,len(days)):
#     if days[i]==day:
#         day_number=i+1
#         break
# print(f"this is day number {day_number}")
#խնդիր 2
# count=0
# for _ in range(0,11):
#     word=input("please enter word:").lower()
#     if word=="karamba":
#         count+=1
# print(f"accepted only {count} saylors")    
#խնդիր 3
# n=input("please enter text: ")
# num_sumbol=0
# for i in range(len(n)):
#     if n[i]=="*":
#         num_sumbol=i+1
#         break
# print(f'symbol is in position {num_sumbol}')
#խնդիր 4 մի քիչ պատահականա ստացվել
# rows = int(input("Введите количество рядов: "))
# sits_inrow = int(input("Введите количество мест в ряду: "))
# meters = int(input("Введите количество метров между рядами: "))
# total_length = 2 * sits_inrow + meters + 2
# for row in range(rows):
#     for i in range(total_length):
#         if i < sits_inrow or i >= sits_inrow + meters + 2:
#             print("-", end="")
#         elif sits_inrow< i < sits_inrow + meters + 1:
#             print("*",end="")
#         else:
#             print(" ",end="")               
#     print()
# խնդիր 5 
        






