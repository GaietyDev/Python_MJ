num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for row in range(10):
    for rjust in range(29):
         print(" ", end = " ")
         
    for col in range(3):
        if col == 0:
            output = num_list[row]
        elif col == 1:
            number = num_list[row]
            output = number * number
        else:
            number = num_list[row]
            output = number * number * number
            
        print(str(output).rjust(6, ' '), end = " ")
    print()
