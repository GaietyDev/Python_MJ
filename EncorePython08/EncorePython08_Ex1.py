total = 1
user_input = 0
while user_input != -1:
    user_input = int(input("Enter a positive integer(-1 to quit): "))
    if user_input >= 0:
        for factorial in range(user_input):
            total = total * (factorial+1)
        print(f"{user_input}! = {total}")
        total = 1
    else:
        print("You have quit the program")
