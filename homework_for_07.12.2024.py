# խնդիր 110
# list=[]
# n=int(input("please enter number: "))
# while n!=0:
#     list.append(n)
#     n=int(input("please enter number: "))
# else:
#     list.sort()
#     print(list)
# խնդիր 111
# list=[]
# n=int(input("please enter number: "))
# while n!=0:
#     list.append(n)
#     n=int(input("please enter number: "))
# else:
#     list.sort(reverse=True)
#     print(list)
# խնդիր 112 խնդրի պահանջը ճիշտ եմ հասկացել՞
# list1=[]
# n=int(input("please enter number: "))
# while n!=0:
#     list1.append(n)
#     n=int(input("please enter number: "))
# else:
#     if len(list1)<4:
#         print("Error you have entered few aguments")
#     else:
#         list1.sort()
#         print(list1)  
# new_list=list1.copy()
# new_list.remove(max(new_list))
# new_list.remove(min(new_list))
# print(new_list)
# խնդիր 113
# list1=[]
# n=input("please enter text: ")
# while n!="":
#     list1.append(n)
#     n=input("please enter text: ")
# else:
#     for i in range(len(list1)-1,-1,-1):
#         if list1.count(list1[i])>1:
#             list1.pop(i)
#     print(list1)            
# խնդիր 114
# list1=[]
# positive=[]
# negative=[]
# zero=[]
# n=input("please enter text: ")
# while n!="":
#     list1.append(n)
#     n=input("please enter text: ")
# else:
#     for i in list1:
#         if int(i)>0:
#             positive.append(i)
#         elif int(i)<0:
#             negative.append(i)
#         else:
#             zero.append(i)
# print(positive)
# print(negative)
# print(zero)   
             
# խնդիր 115
# n=int(input("please enter number: "))
# new_list=[]
# for i in range(1,n//2+1):
#     if n%i==0:
#         new_list.append(i)
# print(new_list)

# խնդիր 116(part 1)
# n=int(input("please enter number: "))
# summ=0
# new_list=[]
# for i in range(1,n//2+1):
#     if n%i==0:
#         new_list.append(i)
# for j in new_list:
#     summ+=j
# if summ==n:        
#     print("its perfet number")
# else:
#     print("it isn't perfect number")    
# խնդիր 116(part 2)
# for n in range(1, 10000):
#     summ = 0
#     new_list = []
#     for i in range(1, n // 2 + 1): 
#         if n % i == 0:
#             new_list.append(i)  
#     summ = sum(new_list)  
#     if summ == n:  
#         print(n)
#կարտերի խնդիր
# import random
# master=["♥","♦","♣","♠"]
# karter=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
# new_list=[]
# person_1=[]
# person_2=[]
# person_3=[]
# person_4=[]
# for i in master:
#     for j in karter:
#         new_list.append(i+j)
# while len(person_1)<8 and new_list:
#         selected_card=random.choice(new_list)
#         person_1.append(selected_card)
#         new_list.remove(selected_card)
# while len(person_2)<8 and new_list:
#         selected_card=random.choice(new_list)
#         person_2.append(selected_card)
#         new_list.remove(selected_card)
# while len(person_3)<8 and new_list:
#         selected_card=random.choice(new_list)
#         person_3.append(selected_card)
#         new_list.remove(selected_card)
# while len(person_4)<8 and new_list:
#         selected_card=random.choice(new_list)
#         person_4.append(selected_card)
#         new_list.remove(selected_card)                 
# print(f"first person's cards={person_1},\nsecond person's cards={person_2},\nthird pesons cards={person_3},\nfourth person's cards={person_4}")     










