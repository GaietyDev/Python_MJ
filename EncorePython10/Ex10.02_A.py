from images import Image

image_list = ['smokey', 'moon', 'EagleNebula']

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
    
    if operation == 'Original':
        print('Close the image to continue')
        image.draw()

def main():
    while True:
        image_name_input = input("Enter the name of the image file: ")
        image_name = image_name_input.strip('.gif')
        if image_name not in image_list:
            print("|! IMAGE NOT FOUND !|\n")
            continue
        
        image_name = image_name + '.gif'
        print(image_name)
        break
    try:
        while True:
            image = Image(image_name)
            printMenu()
            command = acceptCommand()
            if command == 0:
                print("\nDone")
                break
            runCommand(command, image)
    except KeyboardInterrupt:
        print("\nProgram Closed")
        
main()
