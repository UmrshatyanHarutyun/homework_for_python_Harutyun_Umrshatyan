#137
# import random
# new_list={
#     2:0,
#     3:0,
#     4:0,
#     5:0,
#     6:0,
#     7:0,
#     8:0,
#     9:0,
#     10:0,
#     11:0,
#     12:0,
# }
# for _ in range(1000):
#     a=random.randint(1,6)
#     b=random.randint(1,6)
#     dice_total=a+b
#     for i in new_list:
#         if dice_total==i:
#             new_list[i]+=1

# for j in new_list:
#     new_list[j]/=10
# print(new_list)
#138
# phone_keybord={
#     "1":".,?!:",
#     "2":"ABC",
#     "3":"DEF",
#     "4":"GHI",
#     "5":"JKL",
#     "6":"MNO",
#     "7":"PQRS",
#     "8":"TUV",
#     "9":"WXYZ",
#     "0":" "
# }
# message=input("please enter text: ").upper()
# result=""
# for letter in message:
#     for key,value in phone_keybord.items():
#         if letter in value:
#             result+=key*(value.index(letter)+1)
# print(result)
#139
# morse_alphabet = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
#     'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
#     'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
#     'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
#     'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
#     'Z': '--..',
#     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
#     '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
# }
# new_text = input("Please enter text: ").upper()
# new_text_code = ""
# for letter in new_text:
#     if letter in morse_alphabet:
#         new_text_code += morse_alphabet[letter] + " "
#     else:
#         continue
# print(new_text_code)
# 140-ավելի կարճ տարբերակ կա՞
# regions={
#     'A': 'Newfoundland and Labrador',
#     'B': 'Nova Scotia',
#     'C': 'Prince Edward Island',
#     'E': 'New Brunswick',
#     'G': 'Eastern Quebec',
#     'H': 'Montreal',
#     'J': 'Western Quebec',
#     'K': 'Eastern Ontario (excluding Ottawa)',
#     'L': 'Central Ontario',
#     'M': 'Toronto',
#     'N': 'Southwestern Ontario',
#     'P': 'Northern Ontario',
#     'R': 'Manitoba',
#     'S': 'Saskatchewan',
#     'T': 'Alberta',
#     'V': 'British Columbia',
#     'X': 'Northwest Territories and Nunavut',
#     'Y': 'Yukon'
# }       
# post_code=input("Please entr post code: ")
# for key,value in regions.items():
#     if post_code[0]==key and post_code[1]=="0":
#         post_code=regions[key]+",place is village"
#         print(post_code)
#         break
#     elif post_code[0]==key and post_code[1]!="0":
#         post_code=regions[key]+",place is city"
#         print(post_code)
#         break
# else:
#     print("fatal error")
#141-կարճ տարբերակ՞
# hundreds = {
#     "1": "one hundred",
#     "2": "two hundred",
#     "3": "three hundred",
#     "4": "four hundred",
#     "5": "five hundred",
#     "6": "six hundred",
#     "7": "seven hundred",
#     "8": "eight hundred",
#     "9": "nine hundred"
# }
# tens = {
#     "1": "ten",
#     "2": "twenty",
#     "3": "thirty",
#     "4": "forty",
#     "5": "fifty",
#     "6": "sixty",
#     "7": "seventy",
#     "8": "eighty",
#     "9": "ninety",
#     "0": ""
# }
# teens = {
#     "10": "ten",
#     "11": "eleven",
#     "12": "twelve",
#     "13": "thirteen",
#     "14": "fourteen",
#     "15": "fifteen",
#     "16": "sixteen",
#     "17": "seventeen",
#     "18": "eighteen",
#     "19": "nineteen"
# }
# units = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }
# number =input("please enter number:")
# number_in_text=""
# if len(number) == 3:
#     number_in_text = hundreds[number[0]]
#     if number[1] == "1":
#         number_in_text += " " + teens[number[1] + number[2]]
#     elif number[1] != "0":
#         number_in_text += " " + tens[number[1]]
#     if number[1] != "1" and number[2] != "0":
#         number_in_text += " " + units[number[2]]
# elif len(number) == 2:
#     if number[0] == "1":
#         number_in_text = teens[number]
#     else:
#         number_in_text = tens[number[0]]
#         if number[1] != "0": 
#             number_in_text += " " + units[number[1]]
# elif len(number) == 1:  
#     number_in_text = units.get(number[0], "zero")  
# else:
#     number_in_text = "Invalid input. Please enter a number between 0 and 999."
# print(number_in_text)
#145
# game_point_list={
#     1:"AEILNORSTU",
#     2:"DG",
#     3:"BCMP",
#     4:"FHVWY",
#     5:"K",
#     8:"JX",
#     10:"QZ"
# }
# new_word=input("please enter new word: ").upper()
# points=0
# for letter in new_word:
#     for key,value in game_point_list.items():
#         if letter in value:
#             points+=key
# print(points)
        


  