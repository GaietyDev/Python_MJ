while True:
    user_input = int(input("Enter a number(0-9): "))
    print()
    
    if user_input > 9:
        print("|! NUMBER CAN'T BE MORE THAN 9 !|\n")
    elif user_input < 0:
        print("|! NUMBER CAN'T BE LESS THAN 0 !|\n")
    else:
        break

line_number = 1
with open("files\\EncorePython05_file3.txt", 'r') as file:
    for line in file:
        line = line.strip().split()
        line_number += 1
        print(f"Mutliples of {line_number-1}:", end=" ")
        
        for number in line:
            if str(user_input) == number[-1]:
                print(number, end=" ")
        print()
        
# File is closed
