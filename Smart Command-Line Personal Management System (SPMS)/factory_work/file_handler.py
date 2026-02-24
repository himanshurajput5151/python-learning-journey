import config
import simplejson as json
from models import encodejson

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
        json.dump(data,expense_file,indent=4,cls=encodejson.EnhancedJSONEncoder)

'''
    given function to read expense file and return and if file empty return empty list 
'''


def expense_view_json():
    try:
        with open(config.EXPENSES_FILE_PATH,'r') as expense_file :
            return json.load(expense_file)
    except (FileNotFoundError,json.JSONDecodeError) :
        return []


'''
    given function to read expense file and return and if file empty return empty list and if file
    found search expense id and delete it.
'''




def expense_delete_json(public_expense_id, user_id):
    try:
        with open(config.EXPENSES_FILE_PATH, 'r') as expense_file:
            expense_user_data = json.load(expense_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    # Check if expense exists AND belongs to user
    expense_found = False
    for item in expense_user_data:
        if (item.get('public_expense_id') == public_expense_id) and (item.get('user_id') == user_id):
            expense_found = True
            break

    if not expense_found:
        return False, "Expense ID not found for this user."

    # Keep everything except the matching expense
    updated_data = [
        item for item in expense_user_data
        if not (
            (item.get('public_expense_id') == public_expense_id) and
            (item.get('user_id') == user_id)
        )
    ]

    with open(config.EXPENSES_FILE_PATH, 'w') as expense_file:
        json.dump(updated_data, expense_file, indent=4)

    return True, f"Expense ID {public_expense_id} deleted successfully."


'''
to find whether the given public expense key is unique or not
'''
def expense_public_id_json(expense_id_public) :
    try:
        with open(config.EXPENSES_FILE_PATH,'r') as expense_file:
            expense_public_file = json.load(expense_file)
    except (FileNotFoundError,json.JSONDecodeError):
        return False
    for item in expense_public_file:
        if item['public_expense_id']==expense_id_public:
            return True
    return False

'''
to check whether user id already exist or not.
'''
def unique_user_id_json(public_user_id):
    try:
        with open(config.USER_FILE_PATH, 'r') as user_file:
            user_id_info = json.load(user_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return False  # Treat as no duplicates if file doesn't exist
    for item in user_id_info:
        if item['user_id'] == public_user_id:
            return True
    return False