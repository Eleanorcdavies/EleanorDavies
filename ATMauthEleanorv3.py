# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# bank operations

#ASSIGNMENT
# 1. Consistent User Account Balance: When user deposits, withdrawals and do other banking operations, their account balance should be saved in a file.
    #deposit adds to the balance. That is at index 4 (a string) in the filename = (str(account_number) + ".txt")
    #withdrawals must check if amount (<=) balance. If it is, subtract the amount from the balance. That is at index 4 (a string) in the filename = (str(account_number) + ".txt")
    #display balance should just show current balance. That is at index 4 (a string) in the filename = (str(account_number) + ".txt")

# 2a. When user login to the system, create a file in the auth_session folder to keep track of their login.

# 2b. When user logout of the system, delete the file in auth_session to indicate that they have logged out of the system.
    


# Initializing the system
import random
import validation
import database
from getpass import getpass

user_db_path = "data/user_record/"

def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()
    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)
        
        if user:
            bank_operation(user)
#forgotten else statement. Without this, as soon as the bank_operation is resolved it will print the "Invalid account or password" statement.
        else:
            print('Invalid account or password')
            login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Current Balance (4) Logout (5) Exit \n"))

    if selected_option == 1:

        deposit_operation(user)
    elif selected_option == 2:

        withdrawal_operation(user)
    elif selected_option == 3:

        print ("Current balance is " + str(get_current_balance(user)))
        bank_operation(user)
    elif selected_option == 4:

        logout(user)
    elif selected_option == 5:

        exit(user)
    else:

        print("Invalid option selected")
        bank_operation(user)



##running testing on withdrawl to see what is going wrong



def withdrawal_operation(user):
    print("withdrawal")
    # get current balance
    print("Your available balance is $ %s " % (get_current_balance(user)))
    # get amount to withdraw
    withdrawl_amount = int(input("How much would you like to withdraw? \n"))
    # check if current balance > withdraw balance
    try:
        if int(withdrawl_amount) <= int(get_current_balance(user)):
    # deduct withdrawn amount form current balance in the account file
            new_balance = int(get_current_balance(user)) - int(withdrawl_amount)
            f = open(user_db_path + str(user[5]) + ".txt", "w")
            user[4] = (str(new_balance))
            user_data_string_updated = ",".join(user)
            # print(user_data_string_updated)
            f.write(user_data_string_updated)
            # display new balance
            print("You have withdrawn $%s. Your new balance is $%s" % (withdrawl_amount, new_balance))
            f.close()
        else:
            print("Your available balance is $ %s, which is less than what you are trying to withdraw: $%s " % (get_current_balance(user), withdrawl_amount))
            print("Insufficient funds")
    except TypeError():
        print("You must select an integer amount")
        #return to the bank_operation menu
    finally:        
        return bank_operation(user)



def deposit_operation(user):
    print("Deposit Operations")
    # get current balance
    # print(get_current_balance(user))
    # get amount to deposit
    deposit_amount = int(input("How much would you like to deposit? \n"))
    # add deposited amount to current balance in the account file
    # try:
    new_balance = int(get_current_balance(user)) + deposit_amount
    f = open(user_db_path + str(user[5]) + ".txt", "w")
    user[4] = (str(new_balance))
    user_data_string_updated = ",".join(user)
    # display new current balance
    f.write(user_data_string_updated)
    print("Your new balance is $" + (get_current_balance(user)))
#     # except TypeError():
#     #     print("You must select an integer amount")
#     # #return to the bank_operation menu
    # # finally:
    f.close()
    return bank_operation(user)



def get_current_balance(user):
    current_balance = user[4]
    return current_balance
    # return bank_operation(user)

#I want there to be zeros possible, but not as the first digit of the account number
def generation_account_number():
    potential_account_number = random.randrange(1000000000, 9999999999)
    #The below checks that the account is not already being used. We don't want to have multiple people with the same account numbers! In the very small chance that it does repeat, it just runs the function again until the account number that is randomly generated is different from any of the account numbers already in our database.
    #if accountNumber in list of all account numbers
    if database.does_account_number_exist(potential_account_number):
        generation_account_number()
    else:
        accountNumber= potential_account_number
        return accountNumber

#when the account is created the balance is automatically set to zero, so this is no longer useful
# def set_current_balance(user_details, balance):
#     user_details[4] = balance


def exit(user):
    database.delete_auth_session(user)
    print("You have been logged out. Have a great day")


def logout(user):
    database.delete_auth_session(user)
    print("You have been logged out.")
    init()

init()