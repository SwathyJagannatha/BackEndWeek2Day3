# 2. Advanced Slicing Techniques
#Task 1: Given the list of temperatures:
#temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
#Extract the temperatures for the second week (7 days) of the month. Expected Outcome:
#83, 85, 86, 87, 88, 89, 90,

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
temp = temperatures[7:14]
print(temp)
#print(len(temp))

# Task 2: Extract all the temperatures above 100 (reminder: when slicing to the end of a list you don't need a stop index).

temp_list = temperatures[23:]
print(temp_list)

#Task 3: extract temperatures from the 5th to the 10th.

list_five = temperatures[4:10]
print(list_five)
