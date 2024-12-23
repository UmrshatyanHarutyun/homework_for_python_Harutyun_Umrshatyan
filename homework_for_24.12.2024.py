#exs. 174
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
# a = int(input("please enter first number: "))
# b = int(input("please enter second number: "))
# result = gcd(a, b)
# print(f"The max number between {a} and {b} is equal {result}")

#exs. 176
# phonetic_dict = {
#     'A': 'Alpha',    'J': 'Juliet',    'S': 'Sierra',
#     'B': 'Bravo',    'K': 'Kilo',      'T': 'Tango',
#     'C': 'Charlie',  'L': 'Lima',      'U': 'Uniform',
#     'D': 'Delta',    'M': 'Mike',      'V': 'Victor',
#     'E': 'Echo',     'N': 'November',  'W': 'Whiskey',
#     'F': 'Foxtrot',  'O': 'Oscar',     'X': 'Xray',
#     'G': 'Golf',     'P': 'Papa',      'Y': 'Yankee',
#     'H': 'Hotel',    'Q': 'Quebec',    'Z': 'Zulu',
#     'I': 'India',    'R': 'Romeo'
# }
# text=input("please enter new text: ").upper()
# text_list=list(text)
# def codding(text_list):
#     if text_list==[]:
#         return []
#     else:
#        return [phonetic_dict[text_list[0]]]+codding(text_list[1:])
# encoded_text=codding(text_list)
# print("Encoded text:", " ".join(encoded_text))
#exs. 184
# def prime_list(mylist):
#     if not mylist:  #այս հատվածը chat gpt-ինա հուշել խնդրում եմ հետո բացատրես
#         return []    
#     if type(mylist[0]) == list:
#         return prime_list(mylist[0]) + prime_list(mylist[1:])
#     else:
#         return [mylist[0]] + prime_list(mylist[1:])
# print(prime_list([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))

