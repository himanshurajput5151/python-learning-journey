
from decimal import Decimal,ROUND_HALF_UP,InvalidOperation
from factory_work import fuzzy_matching,file_handler
from services import auth_service,expense_service

def user_handling():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        try:
            choice = int(input("Choose from the following menu: "))
            if choice < 1 or choice > 3:
                print("Enter value from given menu.")
                continue
        except ValueError:
            print("Enter value from given menu.")
            continue

        if choice == 1:
            print("\tSign up")
            user_name = input("Enter your UserName: ").strip().title()
            email = input("Enter your EmailId: ").strip()
            password = input("Enter your Password: ").strip()
            reg_result = auth_service.register_user(user_name, email, password)
            view_by_dev_result, to_be_printed_result = reg_result
            print(to_be_printed_result)

        elif choice == 2:
            print("\tSign in")
            user_info = input("Enter UserID or EmailId: ")
            password = input("Enter your Password: ")
            login_result = auth_service.login_user(user_info, password)
            view_by_dev_result, to_be_printed_result, user_id = login_result
            print(to_be_printed_result)
            if view_by_dev_result:
                dashboard(user_id)

        elif choice == 3:
            break  # Exit loop


def dashboard(user_dashboard_id):
    while True:
        print("1) Add Expense")
        print("2) View Expense")
        print("3) Delete Expense")
        print("4) Logout")

        expense_choice = 0
        try:
            expense_choice = int(input("Enter your option: "))
            if expense_choice <= 0 or expense_choice > 4:
                print("Invalid input. Try again.")
                continue
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if expense_choice == 1:
            # amount entry
            try:
                amount_val = Decimal(input("Enter amount: "))
                amount_val = amount_val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                if amount_val <= 0:
                    print("Amount should be greater than zero. Please enter a valid number.")
                    continue
            except InvalidOperation:
                print("Invalid input. Please enter a valid number.")
                continue

            # category entry
            print(f"Available Categories: {', '.join(fuzzy_matching.CATEGORIES)}")
            raw_category = input("Enter Category: ").strip()
            final_category = fuzzy_matching.get_best_category(raw_category)
            if final_category != raw_category.title() and final_category != "Others":
                confirm = input(f"Did you mean {final_category}? (y/n): ")
                if confirm.lower() != 'y':
                    final_category = "Others"

            # merchant entry
            merchant_name = input("Enter Merchant Name: ")
            merchant_name = merchant_name.strip().title() if merchant_name else 'Unknown'

            # city entry
            city_name = input("Enter City: ")
            city_name = city_name.strip().title() if city_name else 'Unknown'

            # description entry
            description = input("Enter the description: ")
            description = description.strip() if description else ""

            # tags entry
            tags = input("Enter tags: ")
            tags = set(tags.strip().lower().split()) if tags else set()

            # recurring entry
            while True:
                user_input = input("Is expense recurring: (y/n) ").strip().lower()
                if user_input in ('y', 'n'):
                    is_recurring = user_input == 'y'
                    break
                print("Please enter 'y' or 'n'.")

            # pass to expense service
            expense_result_dev, expense_result_user = expense_service.add_expense(
                user_dashboard_id, amount_val, final_category, merchant_name,
                city_name, description, tags, is_recurring
            )
            print(expense_result_user)

        elif expense_choice == 2:
            # view all expenses
            view_expense_result = expense_service.view_all_expense(user_dashboard_id)
            expense_dev_result, expense_list, expense_msg = view_expense_result
            if expense_dev_result:
                print(expense_msg," ",expense_list)
            else:
                print(expense_msg)

        elif expense_choice == 3:
            # delete expense
            expense_id_from_user = input("Enter Expense Id: ")
            expense_delete_result = expense_service.delete_expense_user(expense_id_from_user, user_dashboard_id)
            expense_delete_dev, user_delete_msg = expense_delete_result
            print(user_delete_msg)

        elif expense_choice == 4:
            break  # Exit loop
        else:
            print("Invalid option. Try again.")


user_handling()

