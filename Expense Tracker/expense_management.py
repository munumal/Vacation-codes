

def add_expense(expenses, month, category, description, amount):
    if month not in expenses:
        expenses[month] = []
    expenses[month].append((category, description, amount))

def view_expenses(expenses, month):
    if month in expenses:
        return expenses[month]
    return []

def calculate_expenses_by_category(expenses, month):
    if month not in expenses:
        return {}
    category_totals = {}
    for category, _, amount in expenses[month]:
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += amount
    return category_totals
