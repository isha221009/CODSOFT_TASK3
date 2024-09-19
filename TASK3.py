import random
import string

# Function to generate a password
print("**** Password Generator ****")

while True:
    try:
        length = int(input("\nEnter the lenght of the password: "))
        if length < 6:
            print("Password length should be at least 6 characters!")
            continue
    except ValueError:
        print("Invalid input! ")
        continue

    # Characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    print(f"Generated Password: {password}")

    # Ask if user wants to generate another password
    another = input("Do you want to generate another password? (yes/no): ").lower()
    if another != "yes":
        print("Goodbye!")
        break
