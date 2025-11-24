Expenses_List = [] # list of all expenses

print("Welcome to the Finance Tracker : Have Less Expense.")

while True:
    print("\n===Menu===")
    print("1.Add Expenses")
    print("2.View All Expenses")
    print("3.View Total Expenses")
    print("4.View Expenses by Category")
    print("5.Delete Expense")
    print("6.View Category Summary")
    print("7.Exit")
    
    Select = int(input("Please enter your choice : " ))
    
    #Add expenses
    if(Select == 1):
        Date = input("Enter the date (DD-MM-YYYY) :")
        Category = input("Enter the category of expenses :")
        Description = input("Enter the extra details of expenses:")
        Amount = float(input("Enter the amount of expenses :"))
        expense= { 
            "date": Date, 
            "category": Category, 
            "description" : Description, 
            "amount": Amount 
        }
        Expenses_List.append(expense)
        print(" \n Done bro. Expense added successfully")
    
    # 2. view all expenses
    elif(Select == 2):
        if( len(Expenses_List) == 0):
            print("No Expenses Visible. Go First And Have Expenses")
        else:
            print("=====This Is Your All Expenses=====")
            count = 1
            for eachexpense in Expenses_List:
                print(f"Expense Number {count} -> {eachexpense["date"]} , {eachexpense["category"]} , {eachexpense["description"]}, {eachexpense["amount"]}")
                count = count + 1
    
    # 3. view total spending
    elif(Select == 3):
        total = 0
        for eachexpense in Expenses_List:
            total = total +eachexpense["amount"]
        print(f"Your Total Expenses is : " ,total)
        
    # 4. view expenses by category
    elif(Select==4):
        searchcat = input("Enter category name : ")
        print(f"\n=====Expenses in '{searchcat}' =====")
        found=False
        for eachexpense in Expenses_List:
            if eachexpense["category"]==searchcat:
                print(f"{eachexpense['date']} , {eachexpense['description']} , {eachexpense['amount']}")
                found=True
        if found==False:
            print(f"No expenses in '{searchcat}' category.")
    
    # 5. delete expense
    elif(Select==5):
        if len(Expenses_List)==0:
            print("No expenses to delete.")
        else:
            print("\n=====Your Expenses=====")
            count = 1
            for eachexpense in Expenses_List:
                print(f"{count}. {eachexpense['date']} , {eachexpense['category']} , {eachexpense['amount']}")
                count = count + 1
            
            delnum = int(input("\nEnter expense number to delete : "))
            if delnum>=1 and delnum<=len(Expenses_List):
                deleted=Expenses_List.pop(delnum-1)
                print(f"Deleted -> {deleted['description']} of Rs.{deleted['amount']}")
            else:
                print("Invalid number")
    
    # 6. category summary
    elif(Select==6):
        if len(Expenses_List)==0:
            print("No data available")
        else:
            cattotals={}
            for eachexpense in Expenses_List:
                c=eachexpense["category"]
                if c in cattotals:
                    cattotals[c]=cattotals[c]+eachexpense["amount"]
                else:
                    cattotals[c]=eachexpense["amount"]
            
            print("\n=====Category Totals=====")
            for cat,amt in cattotals.items():
                print(f"{cat} : Rs.{amt}")
    
    # 7. exit
    elif(Select == 7):
        print("Thank You For Using The Finance Tracker. Have A Awesome Day")
        break
    else:
        print("Invalid Choice . Please Enter A Valid Choice")