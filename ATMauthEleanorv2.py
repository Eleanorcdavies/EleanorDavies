#register
# - first name, last name, password, email
# - generaten user account


#login
# - account number & password


#bank operations

#Initializing the system
import random

database = {} #dictionary
complaints = [] #This stores the complaints so that BankPHP retains the record and can address their customers' complaints

def init():

   
    print("Welcome to BankPHP")
 
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        
        register()
    else:
        print("You have selected an invalid option")
        init()


def login():
    
    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
               
       #I had this go back to the init function for the case that someone made a mistake and doesn't have an account and selected the wrong option or was just mistaken         
    print('Invalid account number or password')
    init()
    


def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )
#In the video and the previous iteration, we had a complaint option, but it was never put in this code. I have added complaint as an operation available
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit (5) Complaint\n"))

#Now, once any of the functions is completed (other than exit) you are brought back to the options. If you logged out, you are brought back to the login.
    if(selectedOption == 1):
        depositOperation()
        bankOperation(user)

    elif(selectedOption == 2):
        withdrawalOperation()
        bankOperation(user)

    elif(selectedOption == 3):
        logout()

    elif(selectedOption == 4):
        print("Thank you for using BankPHP. Have a wonderful day")
              

        #My complaint addition
    elif (selectedOption == 5):
        complaintOperation()
        bankOperation(user)

    else:
        print("Invalid option selected. Please select one of the following options:")
        bankOperation(user)

#The withdraw operatior is more user friendly
def withdrawalOperation():
    print("withdrawal")
    withdrawlAmount = input("How much would you like to withdraw?\n")
    print(withdrawlAmount + " has been withdrawn.")

#the deposit operator is more user friendly
def depositOperation():
    print("Deposit")
    depositAmount = input("How much would you like to deposit?\n")
    print(depositAmount + " has been deposited")

#I thought it was odd that there couldn't be any zeros in the account number, so now it is possible. However, I don't want the first digit to be a zero.
def generationAccountNumber():
    accountNumber = random.randrange(1000000000,9999999999)
    #The 2 lines below check that the account is not already being used. We don't want to have multiple people with the same account numbers! In the very small chance that it does repeat, it just runs the function again until the account number that is randomly generated is different from any of the account numbers already in our dictionary, called "database".
    if accountNumber in database:
        generationAccountNumber()
    else:
        return accountNumber

#This is my complaint function
def complaintOperation():
    complaint = input("What is your complaint?\n"  )
    complaints.append(complaint)
    #I used the line below to test that the complaints are stored in the complaints list
    #print(complaints)
    print("Your complaint is:\n %s \nThank you for sharing your experience with us. We will look into this and, if needed, send a follow up to your email address.\n" % (complaint))

def logout():
    print("You have been logged out")
    login()


if __name__ == '__main__':
    init() 

#### ACTUAL BANKING SYSTEM #####
