import config
from models import user
print(config.APP_NAME)

def menu():
    print("1. Register ")
    print("2. Login ")
    print("3. Exit")



while True:
    menu()
    choice = int(input("Choose from the following menu: "))
    if choice == 1 :
        username = input("Enter the UserName : ")
        user_file = config.USER_FILE_PATH(username)
        user.User().create_username()
    elif choice == 2:
        print()
    else:
        break

