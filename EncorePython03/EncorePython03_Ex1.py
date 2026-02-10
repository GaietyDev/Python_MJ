
for i in range(1, 11):
    number = i*5
    print(str(number).rjust(4, " "), end=" ")
    print(bin(number).rjust(10, " "), end=" ")
    print(hex(number).rjust(6, " "), end=" ")
    print()

