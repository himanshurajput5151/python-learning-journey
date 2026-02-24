import random

from factory_work import file_handler
from models.expense import Expense
import uuid



'''
def to create to public expense id
'''

def generate_public_id():
    return f"EXP{random.randint(0,99999):05d}"


'''
    function to add expense of specific user
'''


def add_expense(user_id,amount_val,category_name,merchant_name,
                city_name,description,tags,is_recurring):


    expense_id_dev = str(uuid.uuid4())              #expense_id for dev people

##expense id for public use case which we provide to user
    while True:
        expense_id_public = generate_public_id()
        is_public_id_valid = file_handler.expense_public_id_json(expense_id_public)
        if not is_public_id_valid :
            break

##object creation of expense -
    expense = Expense(user_id,expense_id_dev,expense_id_public,amount_val,category_name,
                      merchant_name,city_name,description,tags, is_recurring)

    ##converting it to dictionary for json format.
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
    if not user_file :
        return False,[], "User has no expense."
    for item in user_file:
        if item['user_id'] == user_id:
            username = item['username']
            break
    user_expense = file_handler.expense_view_json()
    if not user_expense:
        return False,l1,f"{username} do not have any expense registered."
    for item in user_expense:
        if item['user_id'] == user_id:
            l1.append([item['public_expense_id'], item['amount'], item['category'],item['merchant'], item['city']])
    return True, l1, f"All expenses of {username}"



'''
    function to delete an expense of user
    1)load user file 
'''
def delete_expense_user(expense_id_from_user,user_id):

    expense_file_info = file_handler.expense_delete_json(expense_id_from_user,user_id)
    return expense_file_info
