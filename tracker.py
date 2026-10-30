#Expense Tracker - Installment 4. Author: Kurt Cyrus Viel T. Lopez. The tracker makes decisions.
print("=" * 40)
print("\t\tEXPENSE TRACKER\n \tA tool to log your expenses.")
print("=" * 40)
print("\nMAIN MENU" \
"\n [1] Add an expense \t\t(coming soon)" \
"\n [2] View all expenses\t\t(coming soon)" \
"\n [3] Show total spent\t\t(coming soon)" \
"\n [4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")
print("Welcome,", name,"! Let's log two expenses.\n")

firstExpense = input("First expense? ")
firstExpenseAmount = float(input("Amount? "))

if firstExpenseAmount > 200 :
    print("  Huge expense - are you sure?")
elif firstExpenseAmount > 100 :
    print("  Big expense.")
elif firstExpenseAmount > 50 :
    print("  Moderate expense.")
elif firstExpenseAmount < 50 :
    print("  Small expense.")

secondExpense = input("Second expense? ")
secondExpenseAmount = float(input("Amount? "))

if secondExpenseAmount > 200 :
    print("  Huge expense - are you sure?")
elif secondExpenseAmount > 100 :
    print("  Big expense.")
elif secondExpenseAmount > 50 :
    print("  Moderate expense.")
elif secondExpenseAmount < 50 :
    print("  Small expense.")

if firstExpenseAmount > 100 and secondExpenseAmount > 100 :
    print("  Two big expenses in a row - slow down!")

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
"\nGrand total:\t\t$", total)

if total > budget :
    print("Over budget by $", abs(left), "!")
elif total > budget * 0.9 :
    print("Careful: only $", left, " left.")
else :
    print("Within budget: $", left, " left.")

print("-" * 40)
print("Made by: Kurt Cyrus Viel Lopez  |  Installment 4")