# Calma, Eugene Marie S.
# Calculator

while True:
# Ask the user to input his name 
    username=input("Hi, Good day! Please enter your name.")
# Ask the user what kind of mathematical operation it would used. 
    print("Welcome to your Virtual Calculator! Enter the numbers and I'll solve it for you!")
    first_number = input("Please enter your first number.").upper().replace(" ", "")
    second_number = input("Please enter your second number.").upper().replace(" ", "")
    chosen_operation = input("Press 1 if you want to ADD the variables. Press 2 to SUBTRACT. Press 3 to MULTIPLY. Or press 4 to DIVIDE").upper().replace(" ", "")
    if chosen_operation == 1:
        print ("The sum is" + {first_number} + {second_number})
        #input code for addition
    elif chosen_operation == 2:
        print("")
        #input code for addition
    elif chosen_operation == 3:
        print("")
        #input code for addition
    elif chosen_operation == 4:
        print("")
        #input code for addition
    else:
        print("INVALID SYSNTAX")