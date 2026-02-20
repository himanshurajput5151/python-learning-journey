

from factory_work import file_handler
from models.expense import Expense

'''
    function to add expense of specific user
'''


def add_expense(user_id, title, amount, category):
    if title == '':
        return False, "Title empty not allowed."
    if amount < 0:
        return False, "Amount cannot be negative."
    if category == '':
        category = 'Personal Expense.'

    expense = Expense(user_id, title, amount, category)
    expense_dict = expense.to_dict()
    file_handler.expense_write_json(expense_dict)

    return True, "Expense added Successfully."


'''
    function to view all expense of specific user
'''


def view_all_expense(user_id):
    username = ''
    l1 = []
    user_file = file_handler.user_read_json()
    for item in user_file:
        if item['user_id'] == user_id:
            username = item['username']
            break
    user_expense = file_handler.expense_view_json()
    for item in user_expense:
        if item['user_id'] == user_id:
            l1.append([item['expense_id'], item['title'], item['amount'], item['category']])
    return True, l1, f"All expenses of {username}"

'''
    function to delete an expense of user
'''
def delete_expense_user(expense_id_from_user):
    expense_file_info = file_handler.expense_delete_json(expense_id_from_user)
    return expense_file_info
