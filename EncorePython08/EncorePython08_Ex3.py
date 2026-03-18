import os

commands = ("1","2","3","4","5","6","7",)

def main():
    current_directory = os.getcwd()
    print(current_directory)
    print("1 List the current directory")
    print("2 Move up")
    print("3 Move down")
    print("4 Number of files in the directory")
    print("5 Size of the directory in bytes")
    print("6 Search for a filename")
    print("7 Quit the program")
    valid_command = acceptCommand()
    if valid_command == "7":
        return 7
    runCommand(valid_command)
    print()

def acceptCommand():
    user_input = input("Enter the number of the command: ")
    if user_input in commands:
        return user_input
    else:
        print("|! INVALD INPUT PLEASE ENTER A NUMBER OF A COMMAND !|")
        return acceptCommand()
    
def runCommand(command):
    match command:
        case "1":
            listCurrentDir()
        case "2":
            moveUp()
        case "3":
            moveDown()
        case "4":
            file_count = countFiles()
            print(f"Total number of files: {file_count}")
        case "5":
            byte_count = countBytes()
            print(f"Total number of bytes: {byte_count}")
        case "6":
            file_name = input("Enter the file name: ")
            file_list = findFiles(file_name)
            for file in file_list:
                print(file)

def listCurrentDir():
    current_directory = os.getcwd()
    directory_list = os.listdir(current_directory)
    for list_object in directory_list:
        print(list_object)


def moveUp():
    os.chdir("..")
    print(os.getcwd())


def moveDown():
    directory_input = input("Enter the name of the directory: ")
    current_directory = os.getcwd()
    destination_directory = current_directory + os.sep + directory_input
    directory_list = os.listdir(current_directory)
    if os.path.isdir(destination_directory):
        os.chdir(destination_directory)
    else:
        print("|! DIRECTORY DOES NOT EXIST OR IT IS A FILE !|")


def countFiles():
    count = 0
    current_directory = os.getcwd()
    directory_list = os.listdir(current_directory)
    for file in directory_list:
        if os.path.isfile(file):
            count += 1
        else:
            subdirectory = current_directory + os.sep + file
            os.chdir(subdirectory)
            count += countFiles()
            os.chdir("..")
    return count


def countBytes():
    count = 0
    current_directory = os.getcwd()
    directory_list = os.listdir(current_directory)
    for file in directory_list:
        if os.path.isfile(file):
            count += os.path.getsize(file)
        else:
            subdirectory = current_directory + os.sep + file
            os.chdir(subdirectory)
            count += countBytes()
            os.chdir("..")
    return count


def findFiles(file_name):
    file_names_list = []
    current_directory = os.getcwd()
    directory_list = os.listdir(current_directory)
    for file in directory_list:
        if os.path.isfile(file):
            if file_name in file:
                file_path = current_directory + os.sep + file
                file_names_list.append(file_path)
        else:
            subdirectory = current_directory + os.sep + file
            os.chdir(subdirectory)
            recursive_list = findFiles(file_name)
            file_names_list.extend(recursive_list)
            os.chdir("..")
    
    return file_names_list

while True:
    if main() == 7:
        print("The program has stopped")
        break

