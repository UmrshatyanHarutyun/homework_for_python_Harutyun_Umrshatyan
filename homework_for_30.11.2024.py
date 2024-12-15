# խնդիր 1
# for i in range(0,6):
#     for j in range(0,11,2):
#         print(f"{i+j:>3}",end=" ")
#     print()
# խնդիր 2
# n=int(input("please enter number: "))#սենց ավելի երկարա
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(i,end=" ")
#         else:
#             print(" ",end="")    
#     print()
#խնդիր 3
# n=int(input("please enter number: "))
# for i in range(0,n+1):
#     for j in range(0,n+1):
#         if j==0 or j==n:
#             print("|",end=" ")
#         elif i==0 or i==n:
#             print("-"*2,end=" ")
#         else:
#             print(" "*2,end=" ")
#     print()    
#խնդիր 4
# n = int(input('please enter number: '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if n == i + j or i == j:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print()
#խնդիր 5 
# n = int(input('Enter number: ')) # 17
# k = True
# for i in range(2, n):
#     if n % i == 0:
#         k = False

# if k == True:
#     print('Parz')
# else:
#     print('Baxadryal')
#խնդիր 6
# import math
# n=int(input("plese enter number: "))
# k=0
# for i in range(1,n+1):
#     k+=math.factorial(i)
# print(k)
#խնդիր 8
# n=int(input("please enter number"))
# size=n*2-1
# middle=size//2
# for i in range (0,n):
#     for j in range (0,(n*2-1)):
#         if middle-i<=j and middle+i>=j:
#             print("^",end="")
#         else:
#             print(" ",end="")
#     print()
#խնդիր 9
# n = int(input("Please enter a number: "))
# size = n * 2 - 1
# middle = size // 2
# current_number = 1
# for i in range(n):
#     for j in range(size):
#         if middle - i <= j <= middle + i:
#             if (j - (middle - i)) % 2 == 0:  
#                 print(f"{current_number:>2}", end="")
#                 current_number += 2  
#             else:
#                 print(" ", end="")  
#         else:
#             print(" ", end="")  
#     print()  
#խնդիր 10
# n = int(input("Please enter the size of the pattern: "))
# for i in range(n):
#     for j in range(n):
#         if j <= i:
#             print(n - j, end=" ")
#         else:
#             print(".", end=" ")
#     for j in range(n - 1, -1, -1):
#         if j <= i:
#             print(n - j, end=" ")
#         else:
#             print(".", end=" ")
#     print()  
    