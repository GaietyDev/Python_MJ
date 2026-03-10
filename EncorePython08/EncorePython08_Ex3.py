import os

commands = ("1","2","3","4","5","6","7",)

def main():
    current_dir = os.getcwd()
    print(current_dir)
    print("1 List the current directory")
    print("2 Move up")
    print("3 Move down")
    print("4 Number of files in the directory")
    print("5 Size of the directory in bytes")
    print("6 Search for a filename")
    print("7 Quit the program")
    user_input = input("Enter the number of the command: ")

main()
