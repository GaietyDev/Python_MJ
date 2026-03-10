fib_num1 = 0
fib_num2 = 1
fib_num3 = 0
user_input = 1

while user_input != 0:
    user_input = int(input("Enter a positive integer (0 to quit): "))
    if user_input >= 1:
        for fib in range(user_input):
            fib_num3 = fib_num1 + fib_num2
            fib_num1 = fib_num2
            fib_num2 = fib_num3        
        if user_input % 10 == 0:
            print(f"{user_input}th fibbonacci value = {fib_num3}")
        elif user_input % 10 == 1:
            print(f"{user_input}st fibbonacci value = {fib_num3}")
        elif user_input % 10 == 2:
            print(f"{user_input}nd fibbonacci value = {fib_num3}")
        elif user_input % 10 == 3:
            print(f"{user_input}rd fibbonacci value = {fib_num3}")
        else:
            print(f"{user_input}th fibbonacci value = {fib_num3}")
        fib_num1 = 1
        fib_num2 = 0
    else:
        print("You have quit the program")
