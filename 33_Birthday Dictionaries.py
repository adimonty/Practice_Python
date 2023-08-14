def get_birthday(name, birthday_dict):
    if name in birthday_dict:
        return birthday_dict[name]
    else:
        return "Birthday not found for " + name

def main():
    birthday_dict = {
        "Geoff": "April 5, 1990",
        "Jefe": "June 15, 1985",
        "Thierry": "September 10, 1992",
        "Dennis": "March 22, 1988",
        "Edu": "December 3, 1995"
    }
    
    name = input("Enter a name to get the birthday: ")
    birthday = get_birthday(name, birthday_dict)
    print(birthday)

if __name__ == "__main__":
    main()
