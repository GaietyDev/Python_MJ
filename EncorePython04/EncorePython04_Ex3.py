base10_input = int(input("Enter a number(base 10)"))

base = int(input("Enter a base:"))
base_input = base10_input % base
if base_input >= 0 and base_input <= 9:
    value = str(base_input)
elif base_input == 10:
    value = 'a'
elif base_input == 11:
    value = 'b'
elif base_input == 12:
    value = 'c'
elif base_input == 13:
    value = 'd'
elif base_input == 14:
    value = 'e'
elif base_input == 15:
    value = 'f'

rem = base10_input // base

value = str(rem) + value
print("Your number in base 16 is: s%",value)
