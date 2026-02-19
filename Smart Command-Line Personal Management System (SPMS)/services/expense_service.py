from factory_work import file_handler
from models.expense import Expense
def add_expense(user_id,title,amount,category):
    if title == '' :
        return False,"Title empty not allowed."
    if amount < 0:
        return False, "Amount cannot be negative."
    if category == '' :
        category = 'Personal Expense.'

    expense = Expense(user_id,title,amount,category)
    expense_dict = expense.to_dict()
    file_handler.expense_write_json(expense_dict)

    return True, "Expense added Successfully."