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

#Expense Tracker - Installment 3. Author: Kurt Cyrus Viel T. Lopez. 
name = input("\nWhat's your name? ")
print("Welcome,", name,"! Let's log two expenses.\n")

firstExpense = input("First expense? ")
firstExpenseAmount = float(input("Amount? "))
secondExpense = input("Second expense? ")
secondExpenseAmount = float(input("Amount? "))
subtotal = firstExpenseAmount + secondExpenseAmount
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
tax = tax_percent / 100 * subtotal
total = subtotal + tax
over_budget = budget <= total
left = budget - total

print("\n", ("-" * 40))
print("SUMMARY" \
"\n - ", firstExpense, "\t\t$", firstExpenseAmount, \
"\n - ", secondExpense, "\t\t$", secondExpenseAmount, \
"\nSubtotal:\t\t$", subtotal, \
"\nAverage:\t\t$", subtotal / 2, \
f"\nTax ({tax_percent}):\t\t$ {tax}" \
"\nGrand total:\t\t$", total, \
"\nOver budget? \t\t", over_budget, \
f"\nLeft in budget: \t$ {left:.2f}")
print("-" * 40)
print("Made by: Kurt Cyrus Viel Lopez  |  Installment 3")