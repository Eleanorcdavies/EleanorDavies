# Now let's imagine we have a Categories of budgets e.g. Food Budget is one category, we can also have a Clothing category.
    # Your task is to
    # *    Create a class "Category" and instantiate it with a different categories such as Food, Clothing and Car expenses e.t.c (You can also add more) and their amounts.
    # *    Define the following methods in the class: Deposit, Withdraw, Transfer, Check Balance (Feel free to add any other method)
            
    # PS: Your solution must be dynamic and re-useable, it must support more budget in the future.
    # What we'll look out for when grading are
    # * Coding Conventions
    # * Proper use of Data Structures



#Write code for creating a budget, takes your input and gives you your budget. 
    # Parent class- Total overall budget
        # children- individual categories that add up to equal total. child classes so you can track/manipulate each category directly
            # 2 types of child categories: One time payment (Rent, insurance, phone bill are only paid once a month with an expected amount) or multiple purchases/spending instances (Get food multiple times a month). Spending in that category asks you how much you spent on that regular expense (rent- were you given a discunt ect). If you didn't spend the whole amount in that month, the remainder is pushed to Misc.
            #Adding overall (Bonus at work, gift money, discount on usual expenses, ect) goes to Misc. If you over spend from one category, it goes into the Misc category and takes from that. At the end of the month, it should tell you to put that money into your savings.
    #Opens a file for that month/year, sets your categories and tracks balance. Starts on the 1st and ends at the end of the month. Lets you know if you were over or under.
    #You should be able to include a description of the spend within the category so you can look through your past purchases. Make this a dictionary. Key is a list budget aspects, value is a tuple of spend amount and description. Each category should have its own dictionary.



import datetime
import os
import Make_Budget_Function


# Menu: create budget or update budget
# Update menu: enter payment, check balances, increase budget, transfer amounts between 
    # payment menu: select which expense, deduct amount spent from amount available
    # check balances: print available balances from main budget and all expenses
    # transfer: transfer money between expenses. If increase/loss in total budget, adjust the misc

def __init__():
    print ("Welcome to the Davies Monthly Budget Program")

    have_budget = int(input("Would you like to make a budget, or are you updating one in progress? \n1)Make a new budget \n2) I have already made my budget and. I would like to update a budget that is currently in progress\n"))
    if have_budget == 1:
        print ("Make New Budget")
        # Create the make account function
        Make_Budget_Function.make_budget_plan
        __init__()
        
           
        
    elif have_budget == 2:
        print ("Update Budget")
        update_budget(Make_Budget_Function.locate_budget())
        __init__()
        
        # create update budget function

def update_budget(budget_name):
        Make_Budget_Function.read(budget_name)
        selected_option = int(input("What would you like to update in your budget?\n1) Enter Payment 2) Increase Budget 3)Check Balances 4)Transfer 5) Exit"))
        if selected_option == 1:
            print ("Enter Payment function")
            Make_Budget_Function.Expense.enter_payemnt()
            print(Make_Budget_Function.read(budget_name))
            update_budget()

        elif selected_option == 2:
            print ("Increase Budget")
            print(Make_Budget_Function.read(budget_name))
            Make_Budget_Function.Expense.increase_budget()
            print(Make_Budget_Function.read(budget_name))
            update_budget()

        elif selected_option == 3:
            print ("Check Balances")
            print(Make_Budget_Function.read(budget_name))   
            update_budget()
        
        elif selected_option == 4:
            print ("Transfer between expenses")
            print(Make_Budget_Function.read(budget_name))
            Make_Budget_Function.Expense.transfer(budget_name)
            print(Make_Budget_Function.read(budget_name))
            update_budget()
        
        elif selected_option == 5:
            print ("Thank you for using the Davies Monthly Budget Program")
            __init__()


        else:
            print("You have selected an invalid option")
            __init__()


__init__()