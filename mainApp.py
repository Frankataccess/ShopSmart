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


shopping_list = {}


def addCmdFunction(shopping_list):

    while True:

        # * accepts input for shopping item

        item_input = input("Enter an Item: ").title()

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

#! Function to handle >REMOVE command


def removeCmdFunction(shopping_list):
    while True:
        # * Accept input for the item to remove
        item_to_remove = input("Enter an item to remove: ").strip().title()

        # * Check if the item is in the shopping list
        if item_to_remove in shopping_list:
            del shopping_list[item_to_remove]
            print("Item removed (Type \"VIEW\"to view shopping)")
            return ""

        # * If statement to return an error if the item is in not the shopping list
        if item_to_remove not in shopping_list:
            print("Please enter an item that is in your shopping list")
            print()
            continue

# ! Function to handle commands


def handleCommands():

    allowed_commands = ("ADD", "REMOVE", "VIEW", "HELP", "QUIT", "TOTAL")

    # ** While true to keep accepting input from the user
    while True:
        user_cmd_input = input("> ").upper()

        # * if statement to check if the command the user typed is in the list
        if user_cmd_input not in allowed_commands:
            print("Command not recognised (Type \"HELP\" to see list of commands)")
            print("\n")

        # !if statement to activate the function that handles the "HELP" command (helpCmdFunction)

        if user_cmd_input == "HELP":
            print(helpCmdFunction())
            print("\n")

        # !if statement to activate the function that handles the "ADD" command (addCmdFunction)

        if user_cmd_input == "ADD":
            print(addCmdFunction(shopping_list))
            print("\n")

        # !if statement to activate the function that handles the "ADD" command (addCmdFunction)

        if user_cmd_input == "REMOVE":
            # * if statement to print an error message if the user tries to remove an item from an empty shopping list

            if not shopping_list:
                print(
                    "There's nothing in the shopping list to remove (Type \"ADD\" to add an item to the list)")
                print()
                continue
            print(removeCmdFunction(shopping_list))
            print("\n")

        # !if statement to activate the function that handles the "QUIT" command

        # * if statement to activate the function that handle the "QUIT" by calling sys.exit
        if user_cmd_input == "QUIT":
            sys.exit("Okay, until next time")


print(handleCommands())

"""
what if the user adds an item that's not in the shopping list?

"""
