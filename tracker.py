#Expense Tracker - Installment 5. Author: Kurt Cyrus Viel T. Lopez. The tracker makes decisions.
print("=" * 40)
print("\t\tEXPENSE TRACKER\n \tA tool to log your expenses.")
print("=" * 40)

subtotal = 0
expenseCount = 0
bigExpenseWarning = False
name = input("\nWhat's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print("Welcome,", name,"!\n")

print("\nMAIN MENU" \
"\n [1] Add an expense" \
"\n [2] View all expenses\t\t(coming soon)" \
"\n [3] Show total spent" \
"\n [4] Exit")

while True :
    choice = input("Choose 1-4: ")

    if choice == "1" : 
        expenseAmount = float(input("Amount? "))
        
        if expenseAmount > 200 :
            print("  Huge expense - are you sure?")
        elif expenseAmount > 100 :
            print("  Big expense.")
        elif expenseAmount > 50 :
            print("  Moderate expense.")
        elif expenseAmount <= 50 :
            print("  Small expense.")

        if expenseAmount > 100 :
            if bigExpenseWarning :
                print("  Two big expenses in a row - slow down!")
            bigExpenseWarning = True
        else :
            bigExpenseWarning = False

        subtotal += expenseAmount
        expenseCount += 1
    
    elif choice == "2" :
        print("Coming soon: the tracker can't remember each item yet.")

    elif choice == "3" :
        tax = tax_percent / 100 * subtotal
        total = subtotal + tax
        over_budget = budget <= total
        left = budget - total

        print("   Expenses:\t\t", expenseCount)
        print("   Subtotal:\t\t$", subtotal)
        print("   Tax (", tax_percent, "):\t$", tax)
        print("   Grand total:\t\t$", total)
        
        if total > budget :
            print("   Over budget by $", abs(left), "!")
        elif total > budget * 0.9 :
            print("   Careful: only $", left, " left.")
        else :
            print("   Within budget: $", left, " left.")

    elif choice == "4" :
        print("Goodbye,", name, "!")
        break

    else :
        print("Please choose 1, 2, 3 or 4.")
    
print("-" * 40)
print("Made by: Kurt Cyrus Viel Lopez  |  Installment 5")
print("=" * 40)