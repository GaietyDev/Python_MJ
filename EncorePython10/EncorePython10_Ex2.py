from images import Image

image_smokey = Image("smokey.gif")

def noOperation():
    pass

COMMANDS = {0:('QUIT', noOperation()),
            1:('Original', noOperation())}

def printMenu():
    print("Key  Operation")
    print("----------------")
    for key, value in COMMANDS.items():
        print(f" {key} : {value[0]}")
    print("----------------")

def acceptCommand():
    user_input = int(input("Enter the key of an operation: "))
    if user_input in COMMANDS.keys():
        return user_input
    else:
        print("|! INVALD INPUT >>> PLEASE ENTER A VALID KEY !|\n")
        acceptCommand()

def runCommand(command, image):
    (operation,_) = COMMANDS[command]
    print((operation,_))

printMenu()
command = acceptCommand()
runCommand(command, image_smokey)
