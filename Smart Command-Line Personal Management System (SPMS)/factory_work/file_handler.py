import config
import json

def read_json():
    try:
        with open(config.USER_FILE_PATH,'r') as user_file :
            return json.load(user_file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []



def append_json(user_info):
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
