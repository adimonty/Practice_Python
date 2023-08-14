import datetime

name = input("What is your name: ")
age = int(input("How old are you: "))

current_year = datetime.datetime.now().year
year_to_100 = current_year + (100 - age)

print(f"{name}, you will be 100 years old in the year {year_to_100}")
