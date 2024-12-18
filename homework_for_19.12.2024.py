#խնդիր 85
# a=int(input("xndrum em mutqagrel ej 1-i erkarutyun: "))
# b=int(input("xndrum em mutqagrel ej 2-i erkarutyun: "))
# def koghmer(a,b):
#     return (a**2+b**2)**0.5

# print(f'erankjan nerqnadziq@ = {koghmer(a,b)}')
#խնդիր 86
# def yandex(n):
#     return round(4+0.25*(n/140),2)
# distance=int(input("please enter distance: "))
# print("$", yandex(distance))
#խնդիր 87
# def delivery(n):
#     if n <= 0:
#         return 0
#     return 10.95 + ((n - 1) * 2.95)
# delivery_count = int(input("Please enter goods count: "))
# if delivery_count <= 0:
#     print("The goods count must be at least 1.")
# else:
#     print(f"The final cost for delivery is {delivery(delivery_count):.2f} $")
#խնդիր 88
# def meridian(a,b,c):
#     return (a+b+c)-max(a,b,c)-min(a,b,c)
# a=float(input("please enter number: "))
# b=float(input("please enter number: "))
# c=float(input("please enter number: "))
# print(f'meridian for this three numbers is {meridian(a,b,c)}')
#խնդիր 91-բայց ինձ թվումա խնդիրը սխալ եմ հասկացել
# day = int(input("Please enter day number from 1 to 31: "))
# month = int(input("Please enter month number from 1 to 12: "))
# year = int(input("Please enter year: "))
# list_of_months_max_date1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
# list_of_months_max_date2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
# def ordinalDate(day, month, year):
  
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         days_in_months = list_of_months_max_date2  
#     else:
#         days_in_months = list_of_months_max_date1  

#     if month < 1 or month > 12:
#         return f"Error: Month must be between 1 and 12. You entered {month}."
#     if day < 1 or day > days_in_months[month - 1]:
#         return f"Error: Day must be between 1 and {days_in_months[month - 1]} for month {month}. You entered {day}."
#     day_summ = sum(days_in_months[:month - 1]) + day
#     return f"The ordinal day for {day}/{month}/{year} is: {day_summ}"
# result = ordinalDate(day, month, year)
# print(result)
#խնդիր 92
