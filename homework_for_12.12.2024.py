#slide1
#ex. number 1
# dict1={"a":40,"b":10,'c':20,'d':30}
# values1=sorted(dict1.values())
# print(values1)
#ex. number 2
# dict1={"a":40,"b":10,'c':20,'d':30}
# dict1.setdefault('e',100)
# print(dict1)
#ex. number 3
# dict1={"a":40,"b":10,'c':20,'d':30}
# n=input("please enter new check for dictionary: ")
# print(dict1.get(f'{n}',None))
#ex. number 4
# dict1={'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dict1.update(dict2)
# print(dict1)
#ex. number 5
# mydict = {'a':1,'b':2,'c':12}
# k=1
# for i in mydict:
#     k*=mydict[i]
# print(k)
#ex. number 6
# mydict={'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# keys1=sorted(mydict,key=mydict.get,reverse=True)[:3]
# values1=sorted(mydict.values(),reverse=True)[:3]
# newdict={}
# for i,j in zip(keys1,values1):
#     newdict[i]=j
# print(newdict)
#slide2
# students={   
#     "John Carter": 7,
#     "Emily Harper": 4,
#     "Michael Dawson": 9,
#     "Sophia Bennett": 6,
#     "Daniel Hayes": 8,
#     "Olivia Reed": 5,
#     "William Cooper": 10,
#     "Emma Brooks": 3,
#     "James Foster": 2,
#     "Isabella Green": 1
# }
#ex. number 1
# print(students)
#ex. number 2
# points=students.values()
# summa=0
# for i in points:
#     summa+=i
# print(summa/len(points))
#ex. number 3,4,5
# good={}
# bad={}
# for name,point in students.items():
#     if point>=5:
#         good[name]=point
#     else:
#         bad[name]=point    
# print(good)
# print(bad)
#ex. number 6
# name=input("please enter the name: ")
# print(students.get(f"{name}","absent"))
#ex. number 7
# s = 'a,2,b,5,c,8,a,4,e,11'
# letters = {}
# elements = s.split(',')
# for i in range(0, len(elements), 2):
#     letter = elements[i]
#     number = int(elements[i + 1])  
#     if letter in letters:
#         letters[letter] += number
#     else:
#         letters[letter] = number
# print(letters)
#ex. number 8
# word = 'exersise'
# dict1 = {}
# for letter in word:
#     if letter in dict1:
#         dict1[letter] += 1
#     else:
#         dict1[letter] = 1
# print(dict1)
          


