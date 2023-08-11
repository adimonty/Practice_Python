import random
import string

def generate_weak_password(length=8):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_type = input("Do you want a weak or strong password? ").lower()
        
        if password_type == "weak":
            password = generate_weak_password()
        elif password_type == "strong":
            password = generate_strong_password()
        else:
            print("Invalid choice. Please choose 'weak' or 'strong'.")
            return
        
        print("Generated password:", password)
    except ValueError:
        print("Please enter a valid choice.")

if __name__ == "__main__":
    main()
