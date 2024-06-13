#Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for idx, day in enumerate(days_of_week):
    if idx % 2 == 0:
        print(days_of_week[idx])


