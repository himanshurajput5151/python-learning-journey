
from services import auth_service


def menu():
    print("1. Register ")
    print("2. Login ")
    print("3. Exit")

import factory_work.validator
print("Validator imported successfully")


while True:
    menu()
    choice = int(input("Choose from the following menu: "))
    if choice == 1 :
        print("\tSign up ")
        user_name = input("Enter your UserName: ")
        email = input("Enter your EmailId: ")
        password = input("Enter your Password: ")
        reg_result = auth_service.register_user(user_name,email,password)
        print(reg_result)
    elif choice == 2:
        print("\tSign in ")
        user_name = input("Enter UserName or EmailId : ")
        password = input("Enter your Password: ")

    else:
        break

