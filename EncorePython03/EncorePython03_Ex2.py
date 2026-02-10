import random

while True:
    print(">>> Choose Your Numeral System <<<")
    print("b for Binary")
    print("h for Hexadecimal")
    print(">>>>>>>>> Enter  Below <<<<<<<<<<<")
    option = input("Option: ")
    print()

    if option == 'b' or option == 'h':
        break
    else:
        print("|! INVALID INPUT !|")
        print()
# End of Loop

attempt_counter = 0
while True:
    random_number = random.randint(0, 255)

    if option == 'b':
        print(bin(random_number))
    else:
        print(hex(random_number))

    while True:
        answer = int(input("Enter your answer(Base 10): "))
        print()
    
        if answer == random_number:
            print("Correct! It took you %d attempts" % (attempt_counter))
            break
            
        else:
            print("Incorrect! ", end=" ")
            attempt_counter += 1
    break






