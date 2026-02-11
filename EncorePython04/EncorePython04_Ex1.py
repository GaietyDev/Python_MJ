name = input("Enter your name: ")
name_length = len(name)

print("Name reversed: ", end="")
for i in range(name_length, 0, -1):
    print(name[i-1], end="")
