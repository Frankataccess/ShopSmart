import sys
#! Function to Initially display instructions


def displayInstructions():

    # *opening and reading from the "instructions.txt" file
    with open("instructions.txt", "r", encoding="utf-8") as file:
        return file.read()


#! Function to handle >HELP command

def helpCmdFunction():

    # * code to print out instructions when the user types in "HELP"
    instructions_func = displayInstructions()
    print("\n")
    return instructions_func

#! Function to handle >ADD command


def addCmdFunction():

    while True:

        shopping_list = {}

        # * accepts input for shopping item

        item_input = input("Enter an Item: ")

        # * if statement to check if the number of characters entered is more than 30
        if len(item_input) > 30:
            print("You can't have more than 30 characters per item")

            # ? The continue statement in Python is used to skip the current iteration of a loop (usually a for or while loop) and move to the next iteration.
            print()
            continue
        break

    while True:

        # * try block to handle a valueError incase we get one
        try:
            # * accepts input for price of item

            item_price_input = float(input("Enter the price of the item: £"))
            print()
            break  # Exit the loop if a valid price is entered

        # * except block which handles the value error

        except ValueError:
            print("Please enter a valid numeric price.")
            print()

    shopping_list[item_input] = item_price_input

    print("See your shopping list below")
    print()

    return shopping_list


# ! Function to handle commands

def handleCommands():

    allowed_commands = ("ADD", "REMOVE", "VIEW", "HELP", "QUIT")

    # ** While true to keep accepting input from the user
    while True:
        user_cmd_input = input("> ").upper()

        # * if statement to check if the command the user typed is in the list
        if user_cmd_input not in allowed_commands:
            print("Command not recognised (Type \"HELP\" to see list of commands)")
            print("\n")

        # * if statement to activate the function that handles the "HELP" command (helpCmdFunction)

        if user_cmd_input == "HELP":
            print(helpCmdFunction())
            print("\n")

        # * if statement to activate the function that handles the "ADD" command (helpCmdFunction)

        if user_cmd_input == "ADD":
            print(addCmdFunction())
            print("\n")

        # * if statement to activate the function that handle the "QUIT" by calling sys.exit
        if user_cmd_input == "QUIT":
            sys.exit("Okay, until next time")


print(handleCommands())
