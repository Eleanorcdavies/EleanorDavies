omega_count={
    "2": 1,
    "3": 1,
    "4": 2,
    "5": 2,
    "6": 2,
    "7": 1,
    "8": 0,
    "9": -1,
    "10": -2,
    "J": -2,
    "Q": -2,
    "K": -2,
    "A": 0
}
#call dict values when given keys


def __init__(card_count=0):
    # asks if they want tostart count
    # print("\nThis is the test. The current card count is %s.\n" % (str(card_count)))
    operation_choice = int(input("\nWhat would you like to do with card count? 1) Start Card Count 2)Continue card count 3)Exit"))
    # yes, no(exit)
    if operation_choice == 1:
        # You can calculate the count, now you have to ask what the next card is and also give the option to exit. Print out the current count after every card
        print("\nYou have chosen to start the card count.")
        card_count = 0
        print("\nThe current card count is %s." % (str(card_count)))
        card_count = counting_cards_user_interface(card_count)
        print("\nThe new card count is %s." % (str(card_count)))
        __init__(card_count)        
        # Insert function to interface user with the card count calculation function
    
    elif operation_choice == 2:
        print("\nYou have chosen to continue the card count")
        print("\nThe current count is %s.\n" % str(card_count))
        card_count = counting_cards_user_interface(card_count)
        __init__(card_count)


    elif operation_choice == 3:
        return print("\nYou have chosen No, exit please. Thank you for using Card Counter. Goodbye!\n")
# If someone has a typo for their operation choice
    
    else:
        print("\nYou have entered an invalid choice. Please choose one of the three options.")
        return __init__(card_count)



def counting_cards_user_interface(current_count):
    card = str(input("\nWhat is the card that was just delt? Type F to finish count\n"))
    print("The card delt was %s." % str(card))
    if card == "F":
        return print("\nYou have chosen to finish the count. The final count is %s. Thank you for using Card Counter. Thank you and goodbye!\n" % (current_count))
    else:
        current_count += count_calculation_function(card)
        print("\nThe current card count is %s.\n" % (str(current_count)))
        return current_count



def count_calculation_function(card_value):
    count = 0
    try:
        count += omega_count.get(card_value)
    except:
        print("Error, pleas provide a card face value")
    return count

# To make this clearer, have the key:value pairs printed on seperate lines. Turn dictionary into a string and replace all commas with \n
print("The card values are as follows in the Omega II Count:\n%s" %omega_count)
__init__(0)
