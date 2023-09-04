
# * Function to read instructions from text file
def displayInstructions():
    with open("instructions.txt", "r", encoding="utf-8") as file:
        return file.read()


print(displayInstructions())

print()
