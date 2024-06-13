# 4. Python's Random Game Night

import random

food_choices = ["donuts", "bagels", "pastry","cupcakes","pizza"]

while True:
    user_choice = input("Please guess one item from the list:")
    computer_choice = random.choice(food_choices)

    if user_choice == computer_choice:
        print("Amazing!! You guessed it right, You are a genius")
        break
    else:
        print("Sorry, It wasnt the right choice!! Try again!!")


