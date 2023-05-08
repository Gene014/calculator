# Calma, Eugene Marie S.
# Calculator

while True:
    try:
            # ask the user to input his name 
        username=input(f"\n\33[33mHi, Good day! Please enter your name.\n\33[0m")
        if username.isnumeric():
            raise TypeError
            # ask the user for the given. 
        print(f"\n\33[35mWelcome to your Virtual Calculator {username} ! Enter the numbers and I'll solve it for you!\33[35m")
        first_number = int(input("\n\33[96mPlease enter your first number.\33[96m" ))
        second_number = int(input("\n\33[90mPlease enter your second number. "))
            # ask the operation to be used
        chosen_operation = input("\n\33[1mPress \33[32m1\33[0m\33[1m if you want to \33[32mADD\33[0m\33[1m the variables. Press \33[32m2\33[0m\33[1m to \33[32mSUBTRACT\33[0m\33[1m. Press \33[32m3\33[0m\33[1m to \33[32mMULTIPLY\33[0m\33[1m. Or press \33[32m4\33[0m\33[1m to \33[32mDIVIDE\33[0m\33[1m. ")
            #input code for addition
        if chosen_operation == "1":
            print (f"\n\33[43mHey {username}! The sum for your problem is {first_number + second_number}")
            #input code for subtraction
        elif chosen_operation == "2":
            print(f"\n\33[43mHey {username}! The difference for your problem is {first_number - second_number}")
            #input code for multiplication
        elif chosen_operation == "3":
            print(f"\n\33[43mHey {username}! The product for your problem is {first_number * second_number}")
            #input code for division
        elif chosen_operation == "4":
            print(f"\n\33[43mHey {username}! The quotient for your problem is {first_number / second_number}")
            # wrong input
        else:
            raise ValueError
            # try again
        askyesno = input("\n\33[46mDo you still want to continue? (yes/no):\33[0m ")
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
        print("Numbers Only or Check your typings to avoid errors! ")
    except ZeroDivisionError:
        print("Undefined! Please Try Again!")