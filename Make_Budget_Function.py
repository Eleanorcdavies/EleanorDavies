
#This takes the instances of the expenses and puts them into place for a budget plan

# import os
# import datetime

import datetime
import os

user_db_path = "Budget Project/Budget_data/"


def make_budget_plan():
    print ("You have selected creating a new budget")
     #Must create new document title: First Last Month and Year
    start_new_budget()
    budget_completion_status = False
    if budget_completion_status == False:
        try:
            does_user_need_to_add_expenses = int(input("Do you need to add an expense? 1) Yes 2) No"))
            if does_user_need_to_add_expenses == 1:
                add_expense()
            elif does_user_need_to_add_expenses == 2:
                budget_completion_status = True
                return budget_completion_status
            else:
                print ("You have selected an invalid option")
                budget_completion_status = False
                return budget_completion_status
        except ValueError:
            print("Invalid response.")
            budget_completion_status = False
            return budget_completion_status
    else:
        print ("You have selected that your budget has been created and completed with all expenses.")


def start_new_budget():
    month = input("What month is this budget for? \n")
    year = input("What year is this budget for? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")

    create(first_name, last_name, month, year)

    # double check that this account name doesn't already exist
    
    if completion_state:
        print ("Your budget has been opened")
        print("Now we will add some parameters to this budget.\n")
        #This should take you through asking the dollar amount you have available for your monthly expenses.
        
        try:
            total_monthly_budget = int(input("What is the total dollar amount you have available for this month's expenses? Please type in only a number without commas or decimals.\n"))
            # this is where you create a Budget Parent Class, and then one Child Expense class of Misc!
            #adding/subtracting here should default to Misc.
            budget_name = Budget(total_monthly_budget)
            Misc = Expense(total_monthly_budget)
            
        except ValueError:
            print("You must enter a number without commas or decimals. Please try again")

    else:
        print("Your budget has not been opened. Please try again.")




def add_expense(budget_name):
    expense_name = input("What is the name of this expense?\n")
    try:
        expense_amount = int(input("What is the amount you forsee spending on this during the budget month? Please type in only a number without commas or decimals.\n"))
        expense_name = Expense(expense_name, expense_amount)
        f = open(user_db_path + budget_name + ".txt", "w")
        f.write(datetime)
        f.write("You added %s to your budget %s" % expense_name, budget_name)
        f.close()
        return print("You have added %s to your budget %s" % expense_name, budget_name)
    except ValueError:
        print("You must enter a number without commas or decimals. Please try again")



def create(first_name, last_name, month, year):
    budget_name = first_name + " " + last_name + " " + month + " " + year
    if does_budget_exist(budget_name):
        print ("This budget already exists")
        return False
    completion_state = False   
    try:
            f = open(user_db_path + str(budget_name) + ".txt", "x")
    except FileExistsError:
            print ("There is an error, FileExistsError")
    else:
            f.write(str(budget_name))
            f.write(datetime)
            completion_state = True
    finally:
            f.close()
            return completion_state

    


def does_budget_exist(budget_name):
        all_budgets = os.listdir(user_db_path)
        for budget in all_budgets:
            if budget == str(budget_name) + ".txt":
                return True
        return False

def read(budget_name):

    # find budget name
    # fetch content of the file

    try:

        if does_budget_exist:
            f = open(user_db_path + str(budget_name) + ".txt", "r")
        else:
            f = open(user_db_path + budget_name, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False

    #  From there, it should ask you the individual expenses. By default, it should create a Misc category. That is all it does.
    # Then create a Budget Class with total budget
    #  Have them put in the expenses
    
class Budget:
    def __init__(self, total_budget):
        self.total_budget = total_budget

        # Include amount spent and amount available

    # It also creates a document with the person's name, the date of the first day in the budget, the time period, and the full budget.
    #methods
    #I am letting them go negative because they are just tracking, and if you are out and about you wouldn't know. When this gets updated, you will then know you have to transfer from one expense to the negative one. Otherwise, you will simply be negative. This is simply a tracking tool.
    def increase_budget(self, budget_name):
        budget_increase_description = str(input("Please describe the budget increase.\n"))
        budget_increase_amount = int(input("How much would you like to increase this expense's budget by? Please type a number without commas or decimals.\n"))
        original_total = self.total_budget
        self.total_budget = self.total_budget + budget_increase_amount
        f = open(user_db_path + budget_name + ".txt", "w")
        budget_increase_string = ("\n" + str(Expense) + datetime + "\nThis expense was increased from %s to %s. The description is as follows:\n %s" % str(original_total), str(self.total_budget), budget_increase_description)
        f.write(budget_increase_string)
        print ("Your budget for this expense has increased to %s" % self.total_budget)
        print(f.read)
        f.close()
        return self.total_budget
    # this should update the document

    def check_balance(self, budget_name):
        f = open(user_db_path + budget_name + ".txt", "r")
        print (read(budget_name))
        f.close()
        

    def enter_payment(self, budget_name):
        payment_description = str(input("Please describe this expense.\n"))
        payment_amount = int(input("How much was the payment out of this expense? Please type a number without commas or decimals.\n"))
        original_total = self.total_budget
        self.total_budget = self.total_budget - payment_amount
        f = open(user_db_path + budget_name + ".txt", "w")
        f.write(datetime)
        payment_string = ("\n" + str(Expense) + datetime + "\nThis expense was decreased from %s to %s. The description is as follows:\n %s" % str(original_total), str(self.total_budget), payment_description)
        f.write(payment_string)
        f.close()
        # this should update the document

    


    # this should update the document

# This child should take all of the methods from the previous class, but NOT the __init__ because I want it to different things.\
class Expense(Budget):
    def __init__(self, category, total_budget):
        self.category = category
        self.total_budget = total_budget


    def transfer(self, budget_name):
            from_expense = input("Which expense would you like to transfer from? \n")
            to_expense = input("Which expense would you like to transfer to? \n")
            from_expense.enter_payment()
            to_expense.increase_budget()
            from_expense.check_balance()
            to_expense.check_balance()
            budget_name.check_balance()
        # amount_remaining_for_expense ???

    # This should add the expense to the budget document.


# class
# Clothing = Budget("Clothing", 1000)
# Food = Budget("Food", 1000)
# Entertainment = ("Entertainment", 1000)

def locate_budget():
    all_budgets = os.listdir(user_db_path)
    print (all_budgets)
    target_budget = input("Which of these budgets would you like to update? Please type it exactly as printed.\n")
    
    if does_budget_exist(target_budget):
        f = open(user_db_path + str(target_budget) + ".txt", "x")       
        print("Your budget %s has been opened and is ready to be updated./n" %str(target_budget))
        return target_budget
    else:
        print("That budget does not exist. Please try again.")


