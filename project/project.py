import csv
import sys
import re

class Transaction:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.date}, {self.category}, {self.amount}, {self.description}"

def main():
    while True:
        print("\n1. Add Income/Expense")
        print("2. Show Transactions")
        print("3. Analyze Transactions")
        print("4. Exit")
        choice = input("Make a choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            show_transactions()
        elif choice == '3':
            analyze_transactions()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_transaction():
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    while True:
        try:
            date_input = input("Enter the transaction date (YYYY-MM-DD): ")
            if re.match(date_pattern, date_input):
                date = date_input
                break
            else:
                print("Invalid date format. Please try again.")
        except KeyboardInterrupt:
            print("Program exited by user")
            sys.exit()

    category = input("Enter the transaction category: ")
    amount = format(float(input("Enter the amount: ")), '.2f')
    description = input("Enter the transaction description: ")

    transaction = Transaction(date, category, amount, description)
    save_transaction(transaction)

def save_transaction(transaction):
    try:
        with open('data/transactions.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([transaction.date, transaction.category, transaction.amount, transaction.description])
    except OSError as e:
        print(f"Error opening or writing to the file: {e}")
    except csv.Error as e:
        print(f"CSV file writing error: {e}")

def show_transactions():
    #show transactions from csv file
    try:
        with open('data/transactions.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except OSError as e:
        print(f"Error opening or reading the file: {e}")
    except csv.Error as e:
        print(f"CSV file reading error: {e}")


def analyze_transactions():
    # Analyze transaction from csv file
    total_income = 0
    total_expense = 0
    with open('data/transactions.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                amount = float(row[2])
            except ValueError:
                print(f"Error converting amount to float for row: {row}")
                continue

            if amount > 0:
                total_income += amount
            else:
                total_expense += amount

    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expense: {total_expense:.2f}")

if __name__ == "__main__":
    main()
