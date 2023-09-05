import sys
#! Function to Initially display instructions


def displayInstructions():

    # *opening and reading from the "instructions.txt" file
    with open("instructions.txt", "r", encoding="utf-8") as file:
        return file.read()


print(displayInstructions())


#! Function to handle >HELP command

def helpCmdFunction():

    # * code to print out instructions when the user types in "HELP"
    instructions_func = displayInstructions()
    print("\n")
    return instructions_func


shopping_list = {}

#! Function to handle >ADD command


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

    # * adding the shopping list item and price key-value pairs to the dictionary
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

#! Function to handle >TOTAL command


def totalCmdFunction(shopping_list):

    #! sum() function to add up the values
    total = sum(shopping_list.values())

    return (f"Total price: £{total}")

#!  Function to handle ALL commands


def handleCommands():

    allowed_commands = ("ADD", "REMOVE", "VIEW", "HELP", "QUIT", "TOTAL")

    # ** While true to keep accepting input from the user
    while True:
        user_cmd_input = input("> ").upper()

        #! if statement to check if the command the user typed is in the list
        if user_cmd_input not in allowed_commands:
            print("Command not recognised (Type \"HELP\" to see list of commands)")
            print("\n")

        #! if statement to call the function that handles the "HELP" command (helpCmdFunction)

        if user_cmd_input == "HELP":
            print(helpCmdFunction())
            print("\n")

        #! if statement to call the function that handles the "ADD" command (addCmdFunction)

        if user_cmd_input == "ADD":
            print(addCmdFunction(shopping_list))
            print("\n")

        #! if statement to call the function that handles the "REMOVE" command (removeCmdFunction)

        if user_cmd_input == "REMOVE":
            # * if statement to print an error message if the user tries to remove an item from an empty shopping list

            if not shopping_list:
                print(
                    "There's nothing in the shopping list to remove (Type \"ADD\" to add an item to the list)")
                print()
                continue
            print(removeCmdFunction(shopping_list))
            print("\n")

        #! if statement to Handle the "VIEW" command

        if user_cmd_input == "VIEW":

            # * if statement to handle print an error when the user types in view when there's nothing in the shopping list
            if not shopping_list:

                # todo: put this in a separate function

                print(
                    "There's nothing in the shopping list to view (Type \"ADD\" to add an item to the list)")
                print()
                continue

            print("Here are your items so far:")
            print()
            print(shopping_list)

        #! if statement to call the function that handles the "TOTAL" command

        if user_cmd_input == "TOTAL":

            if not shopping_list:
                print(
                    "There's nothing in the shopping list to add up (Type \"ADD\" to add an item and it's price to the list)")
                print()
                continue
            print(totalCmdFunction(shopping_list))

        #! if statement to call the function that handles the "QUIT" command
        if user_cmd_input == "QUIT":

            # * if statement to exit the program by calling sys.exit
            sys.exit("Okay, until next time")


print(handleCommands())
