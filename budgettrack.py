def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": str(amount)})
    print("Added expense: " + description + " and amount: " + str(amount))
def get_total_expense(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total
def get_balance(budget, expenses):
    return budget - get_total_expense(expenses)
def budget_details():
    print("Budget details:")
    print("Initial budget:" + budget)
    total_expense = get_total_expense(expenses)
    print("Total expense:" + str(total_expense))
    balance = get_balance(budget, expenses)
    print("Balance:" + str(balance))
def main():
    print("Your personal Budget Tracker is here!")
    intial_budget = float(input("Enter your initial budget: "))
    budget = intial_budget
    expenses = []
    while True:
        print("\nWhat would you like to do?\n")
        print("1. Add expense\n")
        print("2. Show budget details\n")
        print("3. Exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            add_expense(expenses, description, amount)
        elif choice == "2":
            budget_details()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("That is not a valid choice.")
if __name__ == "__main__":
    main()
