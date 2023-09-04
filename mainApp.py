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
    return "addCmdFunction works!"


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
