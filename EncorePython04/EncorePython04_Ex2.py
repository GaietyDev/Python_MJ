full_name = input("Enter your full name(first & last): ")

name_split = full_name.split(" ")
first_name = name_split[0]
last_name = name_split[1]
print("Last name, First name: %s, %s" % (last_name, first_name))
