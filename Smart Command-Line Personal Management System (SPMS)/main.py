
from services import auth_service,expense_service


def menu():
    print("1. Register ")
    print("2. Login ")
    print("3. Exit")


def dashboard(user_dashboard_id):
    print("1) Add Expense")
    print("2) View Expense")
    print("3) Delete Expense")
    print("4) Logout")

    expense_choice = int(input("Enter your option: "))
    if expense_choice==1:
        '''
            to add expenses of user which is mapped to user.
        '''
        title_name = input("Enter Title: ")
        amount_val = int(input("Enter amount: "))
        category_name = input("Enter category: ")
        expense_result_dev, expense_result_user = expense_service.add_expense(user_id, title_name, amount_val,category_name)
        print(expense_result_user)
        dashboard(user_dashboard_id)
    elif expense_choice ==2:
        '''
            to view all expense of specific user by passing user_id
        '''
        view_expense_result = expense_service.view_all_expense(user_dashboard_id)
        expense_dev_result, expense_list,expense_msg = view_expense_result
        print(expense_msg)
        print(expense_list)
        dashboard(user_dashboard_id)

    elif expense_choice==3:
        '''
            to delete expense of user using expense Id
        '''
        expense_id_from_user = input("Enter Expense Id: ")
        expense_delete_result = expense_service.delete_expense_user(expense_id_from_user)
        expense_delete_dev, user_delete_msg = expense_delete_result
        print(user_delete_msg)
        dashboard(user_dashboard_id)
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
