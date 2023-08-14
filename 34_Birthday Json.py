import json

def get_birthday(name, birthday_dict):
    if name in birthday_dict:
        return birthday_dict[name]
    else:
        return "Birthday not found for " + name

def add_new_scientist(birthday_dict):
    name = input("Enter the name of the scientist: ")
    birthday = input(f"Enter the birthday of {name}: ")
    birthday_dict[name] = birthday
    return name

def update_json_file(birthday_dict):
    with open("scientists_birthdays.json", "w") as file:
        json.dump(birthday_dict, file, indent=4)

def main():
    with open("scientists_birthdays.json", "r") as file:
        birthday_dict = json.load(file)
    
    name = input("Enter the name of a famous scientist to get the birthday: ")
    birthday = get_birthday(name, birthday_dict)
    print(birthday)
    
    add_new = input("Do you want to add a new scientist's birthday? (yes/no): ").lower()
    if add_new == "yes":
        new_name = add_new_scientist(birthday_dict)
        update_json_file(birthday_dict)
        print(f"{new_name}'s birthday has been added and the JSON file has been updated.")

if __name__ == "__main__":
    main()
