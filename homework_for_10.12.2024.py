#task 1
# x=input("please enter text: ")
# list1=list(x)
# for i in range(len(list1)-1,-1,-1):
#     if list1.count(list1[i])>1:
#         list1.pop()
# print(len(list1))
#task 2
# x = input("Please enter a list of numbers (comma-separated): ").split(',')
# list1 = [int(i) for i in x]  
# n = int(input("Please enter step: "))
# if n > len(list1):
#     print("Error: Step is greater than the length of the list.")
# else:
#     new_list = list1[-n:] + list1[:-n]
#     print("Modified List:", new_list)
#List comprehensions-ex. 1
# text=input("please enter the text: ").lower()
# vowels=["a","e","i","o","u"]
# new_list=[i for i in text if i in vowels]
# print(f"{new_list}\n{len(new_list)}")
#List comprehensions-ex. 2
# n=int(input("please enter number: "))
# list1=[i for i in range(n) if i%2==0,i==1,else i=i%5]
# primt(list1)


            