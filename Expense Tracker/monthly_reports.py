

def total_expenses(expenses, month):
    return sum(amount for _, _, amount in expenses.get(month, []))
