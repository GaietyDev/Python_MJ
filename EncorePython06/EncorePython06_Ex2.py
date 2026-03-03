import os

#path = os.path.join(os.getcwd, "files")
number_list = [1, 2, 2, 3, 3, 3, 4, 4, 5,]

def Median(number_list):
    length = len(number_list)
    even_median_position = int(length / 2)
    odd_median_position = int((length + 1) / 2)
    number_list.sort()

    if length % 2 == 0:
        first_mid = number_list[even_median_position - 1]
        second_mid = number_list[even_median_position]
        median = (first_mid + second_mid) / 2
    else:
        median = number_list[odd_median_position - 1]
    return median  

def Mean(number_list):
    num_of_values = len(number_list)
    total = 0
    
    for number in number_list:
        total += number

    mean = total / num_of_values
    return mean

def Mode(number_list, number_range : int):
    number_dictionary = {}
    high_count = 0
    mode = 0
    
    for index in range(number_range):
        number_dictionary.update({index+1 : 0})

    for number in number_list:
        for index in number_dictionary.keys():
            if number == index:
                value = number_dictionary.get(index)
                value +=1
                number_dictionary[index] = value
    print(number_dictionary)
    for count in number_dictionary.values():
        if count > high_count:
            high_count = count

    #return mode
#file_name = input("Enter the name of the data file: ")

print(Mode(number_list, 5))

