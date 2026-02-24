from fuzzywuzzy import process


CATEGORIES = ["Food & Dining", "Transportation", "Shopping", "Utilities",
              "Entertainment", "Health", "Housing", "Education", "Travel", "Others"]

def get_best_category(expense_cat):
    threshold = 60
    match,score = process.extractOne(expense_cat,CATEGORIES)
    if score>=threshold :
        return match
    else:
        return "Others"