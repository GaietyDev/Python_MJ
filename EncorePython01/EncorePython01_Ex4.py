for row in range(10):
    for rjust in range(14):
         print(" ", end = " ")
   
    for col in range(10):
        #print("%4d    "%((1+row)*(1+col)), end="")
        output = (row + 1) * (col + 1)
        print(str(output).rjust(4, ' '), end = " ")
    print()
