# Expense Tracker Project

expenses = []       #list of all expenses in form of dictionary
print("Welcome to your Expense Tracker! : Let's shop more")


while True:
    print("__________MENU__________")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Now enter your choice :"))
#ADD Expense
    if(choice == 1):
        print("add your expenses: ")
        date = input("enter the date of expense (DD-MM-YYYY): ")
        category = input("enter the category of expense (e.g. Food, Transport, Entertainment): ")
        amount = float(input("enter the amount of expense: "))
        description = input("enter a description for the expense: ")

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        expenses.append(expense)
        print("Expense added successfully!")


#VIEW ALL EXPENSES
    elif(choice ==2):
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("____________This is your expense list____________")
            count = 1
        
            for your_expense in expenses:
                print(f"Expense {count}:")
                print(f"Date: {your_expense['date']}")
                print(f"Category: {your_expense['category']}")
                print(f"Amount: {your_expense['amount']}")
                print(f"Description: {your_expense['description']}")
                print("--------------Yay hurray these are your expenses!---------------")
                count += 1

#VIEW TOTAL EXPENSE
    elif(choice == 3):
        total = 0
        for eachExpense in expenses:
            total = total + eachExpense['amount']
        print(f"Total Expense: {total}")

#EXIT
    elif(choice == 4):
        print("Thank you for using the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

print("It was nice having used by you , Thankyou!")

