
from expense_management import add_expense, view_expenses, calculate_expenses_by_category
from monthly_reports import total_expenses

def print_expenses(expenses):
    for month, exp_list in expenses.items():
        print(f"\nExpenses for {month}:")
        for category, description, amount in exp_list:
            print(f" - {category}: {description} - ${amount}")

def main():
    expenses = {}

    while True:
        month = input("Enter month: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: $"))

        add_expense(expenses, month, category, description, amount)

        more = input("Add another expense? (yes/no): ").lower()
        if more != 'yes':
            break

    print_expenses(expenses)

    month_to_view = input("\nEnter month to view expenses: ")
    print(f"\nExpenses for {month_to_view}:")
    for expense in view_expenses(expenses, month_to_view):
        print(f" - {expense[0]}: {expense[1]} - {expense[2]}")

    print(f"\nTotal expenses for {month_to_view}: {total_expenses(expenses, month_to_view)}")

    print(f"\nExpenses by category for {month_to_view}:")
    for category, total in calculate_expenses_by_category(expenses, month_to_view).items():
        print(f" - {category}: ${total}")

if __name__ == "__main__":
    main()
