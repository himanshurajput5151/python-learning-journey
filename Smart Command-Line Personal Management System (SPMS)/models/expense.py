


class Expense :
    __is_expense_counter = 100
    def __init__(self,user_id,title,amount,category):
        Expense.__is_expense_counter +=1
        self.user_id = user_id
        self.expense_id = Expense.__is_expense_counter
        self.title = title
        self.amount = amount
        self.category = category

    def to_dict(self):
        return {
            'user_id' : self.user_id,
            'expense_id' : self.expense_id,
            'title' : self.title,
            'amount' : self.amount,
            'category' : self.category

        }
