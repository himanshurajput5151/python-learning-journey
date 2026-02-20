import uuid


class Expense :
    def __init__(self,user_id,title,amount,category):
        self.user_id = user_id
        self.expense_id = str(uuid.uuid4())
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
