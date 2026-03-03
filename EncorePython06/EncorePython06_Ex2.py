import os

f= open("files\\dist1.txt", 'r')
number_list = []

for line in f:
    number_list.append(int(line))
f.close()

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
    
    for index in range(number_range):
        number_dictionary.update({index+1 : 0})

    for number in number_list:
        for index in number_dictionary.keys():
            if number == index:
                value = number_dictionary.get(index)
                value +=1
                number_dictionary[index] = value
    
    for key, count in number_dictionary.items():
        if count > high_count:
            high_count = count
            high_key = key
    return high_key

#file_name = input("Enter the name of the data file: ")

print(Median(number_list))
print(Mean(number_list))
print(Mode(number_list, 42))

