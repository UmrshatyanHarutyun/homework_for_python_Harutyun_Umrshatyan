#խնդիր 1
# number1=12
# number2=15
# for i in range(15,number1*number2,15):
#     if i%number1==0 and i%number2==0:
#         break    
# print(i)

#խնդիր 2
# even=0
# odd=0
# for i in range(1,101):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(f"even={even}")
# print(f"odd={odd}")  
          
#խնդիր 3
# import math
# for i in range (0,40):
#     a=round(((1+(math.sqrt(5)))**i-(1-(math.sqrt(5)))**i)/((2**i)*math.sqrt(5)))
#     print(a)

#խնդիր 4
# text=input("please enter text: ")
# count_letter=0
# count_number=0
# count_digits=0
# for i in text:
#     if i.isdigit():
#         count_number+=1
#     elif i.isalpha():
#         count_letter+=1
#     else:
#         count_digits+=1
# print(f"Letter count is: {count_letter}\nNumber count is: {count_number}\nDigit count is: {count_digits}")    

#խնդիր 5
# number=input("please eter the number: ")
# a=0
# for i in number:
#     if i in number:
#         a+=int(i)
# print(a)        

#խնդիր 6
# x=int(input("please enter number: "))
# fact=1
# for i in range(1,x+1):
#     fact*=i
# print(fact)    

#խնդիր 7
# user_age=int(input("please enter your age: "))
# user_sex=input("please enter your sex: ").lower()
# if user_age>=18 and user_age<=20 and user_sex=="male":
#     print("correct")
# else:
#     print("uncorrect")

#խնդիր 64
# a=4.95
# b=9.95
# c=14.95
# d=19.95
# e=24.95
# discount=60
# for i in (a,b,c,d):
#     discout_price=i*discount/100
#     new_price=i-discout_price
#     new_rounded_price=round(new_price,2)
#     print(new_rounded_price)

#խնդիր 65
# celsius=0
# farenheit=0
# for i in range(0,101,10):
#     celsius=i
#     farenheit=(celsius*9/5)+32
#     print(f"Celsius={celsius}",f"Farenheit={round(farenheit)}")

#խնդիր 71
# a=3
# for i in range(0,61,4):
#     a+=((4/((2+i)*(3+i)*(4+i)))-(4/((4+i)*(5+i)*(6+i))))
#     print(a)

#խնդիր 73
# text=input("please input text: ")
# length=int(input("please input the symbol cout: "))
# direction=int(input("please enter 1 or -1: "))
# for i in text:
#     if direction==1:
#         if ord(i)>=ord("a") and ord(i)<=ord("z")-length:
#             i=ord(i)+length
#             print(chr(i))
#         else:
#             i=ord(i)+length-ord("z")+(ord("a")-1)
#             print(chr(i))
#     else:
#         if ord(i)>=ord("a")+length and ord(i)<=ord("z"):
#             i=ord(i)-length
#             print(chr(i))
#         else:
#             i=ord(i)-length-ord("a")+(ord("z")+1)
#             print(chr(i))

#խնդիր 75
# word = input("Please enter the word: ")
# if word == word[::-1]:
#     print(f"This word: {word} is a Palindrome")
# else:
#     print(f"This word: {word} is not a Palindrome")


# #խնդիր 76

# text = input("please enter new text: ")
# result = text.replace(" ", "")
# if result == result[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

