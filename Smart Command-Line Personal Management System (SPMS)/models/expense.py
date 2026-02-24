from datetime import date,datetime



class Expense :
    def __init__(self,user_id,expense_id,public_expense_id,
                 amount,category,merchant_name,city, description,
                 tags,is_recurring):
        self.user_id = user_id
        self.expense_id = expense_id
        self.public_expense_id = public_expense_id
        self.amount = amount
        self.category = category
        self.currency = "INR"
        self.date = date.today()
        now = datetime.now()
        formatted_time = now.strftime("%H:%M")
        self.time = formatted_time
        self.merchant_name = merchant_name
        self.city = city
        self.description = description
        self.tags = tags
        self.is_recurring = is_recurring


    def to_dict(self):
        return {
            'user_id' : self.user_id,
            'expense_id' : self.expense_id,
            'public_expense_id' :self.public_expense_id,
            'category': self.category,
            'amount' : self.amount,
            'currency' : self.currency,
            'date' :self.date,
            'time':self.time,
            'merchant' : self.merchant_name,
            'city': self.city,
            'description' :self.description,
            'tags' : self.tags,
            'is_recurring' : self.is_recurring


        }

