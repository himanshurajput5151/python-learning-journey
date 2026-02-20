import config
import json

def user_read_json():
    try:
        with open(config.USER_FILE_PATH,'r') as user_file :
            return json.load(user_file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []



def user_append_json(user_info):
    try:
        with open(config.USER_FILE_PATH,'r') as user_file:
            data = json.load(user_file)
    except (FileNotFoundError,json.JSONDecodeError):
        data =[]
    data.append(user_info)
    with open(config.USER_FILE_PATH,'w') as user_file:
        json.dump(data,user_file,indent=4)


'''
    Given function is for adding expense in the expense.json 
'''

def expense_write_json(expense_info):
    try:
        with open(config.EXPENSES_FILE_PATH,'r') as expense_file:
            data = json.load(expense_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(expense_info)
    with open(config.EXPENSES_FILE_PATH,'w') as expense_file:
        json.dump(data,expense_file,indent=4)

'''
    given function to read expense file and return and if file empty return empty list 
'''


def expense_view_json():
    try:
        with open(config.EXPENSES_FILE_PATH,'r') as expense_file :
            return json.load(expense_file)
    except (FileNotFoundError,json.JSONDecodeError) :
        return False,[]


'''
    given function to read expense file and return and if file empty return empty list and if file
    found search expense id and delete it.
'''




def expense_delete_json(expense_id):
    try:
        with open(config.EXPENSES_FILE_PATH,'r') as expense_file :
            expense_user_data = json.load(expense_file)
    except (FileNotFoundError,json.JSONDecodeError) :
        return False,[]
    if not any(item for item in expense_user_data if item.get('expense_id')==expense_id):
        return False,"Expense ID not found."

    expense_user_data = [item for item in expense_user_data if item.get('expense_id') != expense_id ]

    with open(config.EXPENSES_FILE_PATH,'w') as expense_file :
        json.dump(expense_user_data,expense_file,indent=4)
        return True,f"Expense Id : {expense_id} is deleted successfully."
