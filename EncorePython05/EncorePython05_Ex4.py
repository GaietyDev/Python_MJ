while True:
    user_input = int(input("Enter a number(0-9): "))
    print()
    
    if user_input > 9:
        print("|! NUMBER CAN'T BE MORE THAN 9 !|\n")
    elif user_input < 0:
        print("|! NUMBER CAN'T BE LESS THAN 0 !|\n")
    else:
        break

with open("files\\EncorePython05_file3.txt", 'r') as file:
     for l in file:
         print(l.strip())
     
# File is closed
