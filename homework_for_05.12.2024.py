#խնդիր 1
# num = [10,20,30,(10,20),40]
# c = 0
# for n in num:
#     if isinstance(n, tuple):
#         break  
#     c += 1
# print(c)
#խնդիր 2
# num = (10,20,30)
# num1=reversed(num)
# print(tuple(num1))
#խնդիր 3
# num = (10,20,30)
# print(len(num))
#խնդիր 4
# num = (10,20,30)
# num1=str(num)
# print(num1)
#խնդիր 5
# num = (10,20,30)
# summ=0
# for i in range(len(num)):
#     summ+=num[i]
# print(summ) 
#խնդիր 6
# num = ("alen","karen","samuel","mike")
# name="samuel"
# for i in num:
#     if i==name:
#         break
# print(f"name is {name}")
#խնդիր 7
# numbers =[10,1,2,3]
# summ=0
# for i in numbers:
#     summ+=i
# print(summ)
#խնդիր 8
# numbers =[10,1,2,3]
# print([x*2 for x in numbers])
#խնդիր 9
# num = ["alen","karen","sam","mike"]
# k=num[0]
# for i in range (0,len(num)):
#     if len(num[i])>len(k):
#         k=num[i]
# print(k)        
#խնդիր 10
# numbers1 =[10,1,2,3]
# numbers2 =[5,6,2,3]
# for i in range (0,len(numbers1)):
#     for j in range (0,len(numbers2)):
#         if numbers1[i]==numbers2[j]:
#             print(numbers1[i],end=" ")                  
# print()
#excersise 1
# mixed_list = [42, "hello", 3.14, True, [1, 2, 3],("key","value")]
# print(mixed_list)
#excersise 2
# my_list =["Hp","Asus","Dell","Mac","Lenovo"]
# for i in my_list:
#     if i=="Mac":
#         print("True")
#         break 
#excersise 3
# password = input("Please enter password: ")
# symbols = ['!', '@', '#', '$', '%', '&', '*']
# digit_count = 0
# symbol_count = 0
# if len(password) < 8:
#     print("Weak password")
# else: 
#     for char in password:
#         if char.isdigit():
#             digit_count += 1
#         if char in symbols:
#             symbol_count += 1 
#     if digit_count >= 2 and symbol_count >= 2:
#         print("Strong password")
#     else:
#         print("Weak password")
#excersise 5
# text=input("please enter password: ")
# if text==text[::-1]:
#     print("open")
# else:
#     print("trash")    
#excersise 6
# x="karen"
# y=list(x)
# print(y)
#excersise 7
# x=[24,15,64,87,79]
# for i in x:
#     if i%2==0:
#         print(i,end=" ")
# print()        
#excersise 8
# x=[24,15,64,87,79]
# for i in range(len(x)-1,-1,-1):
#     if x[i]%2==0:
#         del x[i]
# print(x)
#excersise 9-այստեղ էլ չի ստացվում
# import random
# group = ["alen", "karen", "sam", "mike", "anna"]
# while group:
#     name = input("Please enter your name: ")
#     group_without_self = [person for person in group if person != name]
#     choosed_name = random.choice(group_without_self)
#     print(f"{name}, your choice is {choosed_name}")
#     group.remove(choosed_name)



    

    
  