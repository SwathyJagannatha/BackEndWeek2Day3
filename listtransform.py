#1. Python List Transformation
#Task 1: Given the list of grades:
#grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
#Sort the grades in descending order and display the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
#in-place sorting
grades.sort(reverse=True)
print(grades)

# Alternate method:

#sorted_grades = sorted(grades,reverse=True)
#print(sorted_grades)

#Task 2: Calculate the average grade from the list above and display it 
# (reminder: The average is calculated by dividing the sum of all grades by the length of the grades list).

total_sum = 0
for score in grades:
    total_sum += score
avg_grade = total_sum / len(grades)
    
print(avg_grade)

# Another way:

#avg_grade = sum(grades) / len(grades)
#print(avg_grade)