# Calma, Eugene Marie S.
# Calculator

while True:
    try:
        # Ask the user to input his name 
        username=input(f"Hi, Good day! Please enter your name.")
        if username.isnumeric():
            raise TypeError
        # Ask the user what kind of mathematical operation it would used. 
        print("Welcome to your Virtual Calculator! Enter the numbers and I'll solve it for you!")
        first_number = int(input("Please enter your first number."))
        second_number = int(input("Please enter your second number."))
        chosen_operation = input("Press 1 if you want to ADD the variables. Press 2 to SUBTRACT. Press 3 to MULTIPLY. Or press 4 to DIVIDE").upper().replace(" ", "")
        #input code for addition
        if chosen_operation == "1":
            print (f"Hey {username}! The sum for your problem is {first_number + second_number}")
        #input code for subtraction
        elif chosen_operation == "2":
            print(f"Hey {username}! The difference for your problem is {first_number - second_number}")
        #input code for multiplication
        elif chosen_operation == "3":
            print(f"Hey {username}! The product for your problem is {first_number * second_number}")
        #input code for division
        elif chosen_operation == "4":
            print(f"Hey {username}! The quotient for your problem is {first_number / second_number}")
        # wrong input
        else:
            raise ValueError
        askyesno = input("\n\33[36mDo you still want to continue? (yes/no):\33[0m ")
        if askyesno.lower() == 'no':
            print("\33[41mTerminating Program... ")
            exit()
        elif askyesno.lower() == 'yes':
            continue
        else:
            raise TypeError
    except TypeError:
        print("Please check your typings to avoid errors! ")
    except ValueError:
        print("Numbers Only!")
    except ZeroDivisionError:
        print("Undefined! Please Try Again!")
