import json
from collections import defaultdict

def load_birthday_dict_from_file(file_name):
    with open(file_name, "r") as file:
        birthday_dict = json.load(file)
    return birthday_dict

def extract_month(birthday):
    return birthday.split()[1]

def count_birthdays_by_month(birthday_dict):
    months_count = defaultdict(int)
    for birthday in birthday_dict.values():
        month = extract_month(birthday)
        months_count[month] += 1
    return months_count

def main():
    file_name = "birthdays.json"
    birthday_dict = load_birthday_dict_from_file(file_name)
    months_count = count_birthdays_by_month(birthday_dict)
    
    print("Scientists' birthdays by month:")
    for month, count in months_count.items():
        print(f"{month}: {count} scientists")

if __name__ == "__main__":
    main()