#Expense Tracker - Installment 1. Author: Kurt Cyrus Viel T. Lopez. A prototype main menu for an expense tracker program.
print("=" * 40)
print("\t\tEXPENSE TRACKER\n \tA tool to log your expenses.")
print("=" * 40)
print("\nMAIN MENU" \
"\n [1] Add an expense \t\t(coming soon)" \
"\n [2] View all expenses\t\t(coming soon)" \
"\n [3] Show total spent\t\t(coming soon)" \
"\n [4] Exit\t\t\t(coming soon)")
print("-" * 40)
print("Made by: Kurt Cyrus Viel Lopez  |  Installment 1")
print("=" * 40)

#Expense Tracker - Installment 2. Author: Kurt Cyrus Viel T. Lopez. An expense tracker that asks for user input and calculates their expenses.
name = input("\nWhat's your name? ")
print("Welcome,", name,"! Let's log two expenses.\n")

firstExpense = input("First expense? ")
firstExpenseAmount = float(input("Amount? "))
secondExpense = input("Second expense? ")
secondExpenseAmount = float(input("Amount? "))

print("\n", ("-" * 40))
print("SUMMARY" \
"\n - ", firstExpense, "\t\t$", firstExpenseAmount, \
"\n - ", secondExpense, "\t\t$", secondExpenseAmount, \
"\nTotal spent:\t\t$", firstExpenseAmount + secondExpenseAmount, \
"\nAverage:\t\t$", (firstExpenseAmount + secondExpenseAmount) / 2)
print("-" * 40)
print("Made by: Kurt Cyrus Viel Lopez  |  Installment 2")