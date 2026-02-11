try:
    base16_input = input("Enter a number(base 16)")
    int(base16_input, 16)
except ValueError as e:
    print("Error:", e)

base10_input = int(base16_input, 16)
print("Your number in base 16 is:",base10_input)
