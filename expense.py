import os
import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        self.expenses.append({
            "date": datetime.date.today(),
            "amount": amount,
            "category": category,
            "description": description
        })

    def list_expenses(self):
        for expense in self.expenses:
            print(f"{expense['date']} | {expense['amount']} | {expense['category']} | {expense['description']}")

    def calculate_total_expenses(self, start_date, end_date):
        total_expenses = 0
        for expense in self.expenses:
            if expense['date'] >= start_date and expense['date'] <= end_date:
                total_expenses += expense['amount']
        return total_expenses

    def generate_monthly_report(self):
        monthly_report = {}
        for expense in self.expenses:
            if expense['date'].month == datetime.date.today().month:
                if expense['category'] not in monthly_report:
                    monthly_report[expense['category']] = 0
                monthly_report[expense['category']] += expense['amount']

        print("Monthly Report for {}".format(datetime.date.today().strftime("%B")))
        for category, amount in monthly_report.items():
            print(f"{category}: ${amount}")

    def save_data(self):
        with open("expenses.txt", "w") as f:
            for expense in self.expenses:
                f.write(f"{expense['date']}|{expense['amount']}|{expense['category']}|{expense['description']}\n")

    def load_data(self):
        with open("expenses.txt", "r") as f:
            for line in f:
                expense = line.split("|")
                self.expenses.append({
                    "date": datetime.datetime.strptime(expense[0], "%Y-%m-%d"),
                    "amount": float(expense[1]),
                    "category": expense[2],
                    "description": expense[3]
                })

if __name__ == "__main__":
    expense_tracker = ExpenseTracker()

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Generate Monthly Report")
        print("5. Save Data")
        print("6. Load Data")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            expense_tracker.add_expense(amount, category, description)

        elif choice == "2":
            expense_tracker.list_expenses()

        elif choice == "3":
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            total_expenses = expense_tracker.calculate_total_expenses(start_date, end_date)
            print("Total expenses from {} to {}: ${}".format(start_date, end_date, total_expenses))

        elif choice == "4":
            expense_tracker.generate_monthly_report()

        elif choice == "5":
            expense_tracker.save_data()

        elif choice == "6":
            expense_tracker.load_data()

        elif choice == "7":
            break

        else:
            print("Invalid choice.")

        print("\n")