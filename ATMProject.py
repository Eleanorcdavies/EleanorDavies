#Coding along with the video
import datetime

name = input("What is your name? \n")
allowedUsers = ["Seyi", "Mike", "Love"]
allowedPassword = ["passwordSeyi", "passwordMike", "passwordLove"]


if (name in allowedUsers):
    password = input("What is your password? \n")
    userID = allowedUsers.index(name)
    if (password == allowedPassword[userID]):
        accountBalance = 0
        while True:
            print(datetime.datetime.now())
            print("Welcome %s" % name)
            print("These are the available options:")
            print("1. Withdrawl")
            print("2. Cash Deposit")
            print("3. Complaint")
            selectedOption = int(input("Please select an option"))
            if (selectedOption == 1):
              print ("you selected %s" % selectedOption)
              withdrawRequest = int(input("How much would you like to withdraw?"))
              accountBalance -= withdrawRequest
              print ("take your cash")              
            elif (selectedOption == 2):
              print ("you selected %s" % selectedOption)
              depositAmount = int(input("How much would you like to deposit?"))
              accountBalance += depositAmount
              print("Your current balance is %s" % depositAmount)              
            elif (selectedOption == 3):
              print ("you selected %s" % selectedOption)
              complaint = input("What issue will you like to report?")
              print ("Thank you for contacting us")
            else:
              print ("Invalid Option selected, please try again")
    else:
        print("Password Incorrect, please try again")
else:
    print("Name not found, please try again")
