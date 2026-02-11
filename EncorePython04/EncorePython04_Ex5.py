user_input = input("Enter two words: ")
input_split = user_input.split(" ")

sorted_input = sorted(input_split)

first_word = sorted_input[0]
second_word = sorted_input[1]

print("Alphabetically sorted: %s, %s" % (first_word, second_word))
