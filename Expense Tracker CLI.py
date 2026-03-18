import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create file if not exists
def create_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount"])
    except FileExistsError:
        pass

# Add entry
def add_entry():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')

    entry_type = input("Enter type (income/expense): ")
    category = input("Enter category (food, salary, etc.): ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, entry_type, category, amount])

    print("✅ Entry added successfully!\n")

# View summary
def view_summary():
    income = 0
    expense = 0

    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Type"] == "income":
                    income += float(row["Amount"])
                else:
                    expense += float(row["Amount"])

        print("\n📊 Summary:")
        print(f"Total Income: ₹{income}")
        print(f"Total Expense: ₹{expense}")
        print(f"Balance: ₹{income - expense}\n")

    except FileNotFoundError:
        print("No data found!\n")

# Main menu
def main():
    create_file()

    while True:
        print("==== Expense Tracker ====")
        print("1. Add Entry")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()