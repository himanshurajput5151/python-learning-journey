
from services import auth_service,expense_service


def menu():
    print("1. Register ")
    print("2. Login ")
    print("3. Exit")


def dashboard(user_id):
    print("Add Expense")
    print("View Expense")
    print("Delete Expense")
    print("Logout")

    expense_choice = int(input("Enter your option: "))
    if expense_choice==1:
        title_name = input("Enter Title: ")
        amount_val = int(input("Enter amount: "))
        category_name = input("Enter category: ")
        expense_result = expense_service.add_expense(user_id, title_name, amount_val,category_name)
        print(expense_result)
    elif expense_choice ==2:
        print()
    elif expense_choice==3:
        print()
    else:
        exit()



while True:
    menu()
    choice = int(input("Choose from the following menu: "))
    if choice == 1 :
        print("\tSign up ")
        user_name = input("Enter your UserName: ")
        email = input("Enter your EmailId: ")
        password = input("Enter your Password: ")
        reg_result = auth_service.register_user(user_name,email,password)
        view_by_dev_result, to_be_printed_result = reg_result
        print(to_be_printed_result)
    elif choice == 2:
        print("\tSign in ")
        user_name = input("Enter UserName or EmailId : ")
        password = input("Enter your Password: ")
        login_result = auth_service.login_user(user_name, password)
        view_by_dev_result , to_be_printed_result, user_id = login_result
        print(to_be_printed_result)
        if view_by_dev_result :
            dashboard(user_id)
    else:
        break
