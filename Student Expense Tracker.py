import datetime
expenses = [] 
  
def add_expense():  
       category = input("Enter category(Food/Travel/Shopping/Others): ")   
       amount = float(input("Enter amount: "))   
       date = input("Enter date (DD-MM-YYYY): ")           

       expense = [category, amount, date]     
       expenses.append(expense)    
       print("Expense added!\n")

def view_expenses():   
       if len(expenses) == 0:        
           print("No expenses recorded yet.\n")   
       else:        
           print("\n--- All Expenses ---")        
           for i, expense in enumerate(expenses, 1):            
                 print(f"{i}. {expense[0]} - ₹{expense[1]} (Date: {expense[2]})")        
           print()

def show_total():    
        total = 0   
        for expense in expenses:        
             total += expense[1]    
        print(f"\nTotal Expenses: ₹{total}\n")
def main():   
       while True:      
           print("Expense Tracker Menu")        
           print("1. Add Expense")        
           print("2. View Expenses")        
           print("3. Show Total")        
           print("4. Exit")

           choice = input("Choose an option (1-4): ")

           if choice == "1":
               add_expense()
           elif choice == "2":
               view_expenses()
           elif choice == "3":
               show_total()
           elif choice == "4":
               print("Goodbye!")
               break
           else:
               print("Invalid choice. Try again.\n")

main()
