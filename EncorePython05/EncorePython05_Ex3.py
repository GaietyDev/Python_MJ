file_string = ''

with open("files\\EncorePython05_file3.txt", 'w') as file:
    for row in range(10):
        for col in range(10):
            number = (row+1) * (col+1)
            number_string = str(number)
            if number < 10:
                file_string += number_string + '  '
            else:
                file_string += number_string + ' '
        file_string += '\n'
    file.write(file_string)
    
print(file_string)
