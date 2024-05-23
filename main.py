# paper rock scissors game by ben - https://github.com/benyaminamiri
import random

import pics

# choose number between 0 to 2 to simulate rock, paper and scissors
user_choice = int(input("what do you choose? 0 for Rock, 1 for scissors and 2 for paper:\n"))
print("Your choice:")
if user_choice == 0:
    print(pics.rock)
elif user_choice == 1:
    print(pics.scissors)
elif user_choice == 2:
    print(pics.paper)   

# use random to choose randomly for computer choice.
computer_choice = random.randint(0,2)
print("Computer choice:")
if computer_choice == 0:
    print(pics.rock)
elif computer_choice == 1:
    print(pics.scissors)
elif computer_choice == 2:
    print(pics.paper)


# logic for winner and looser
if user_choice == 0 and computer_choice == 1:
    print("You wine!")
elif user_choice == 1 and  computer_choice == 2:
    print("You wine!")
elif user_choice == 2 and computer_choice == 0:
    print("You wine!")
elif user_choice == computer_choice:
    print("Draw")
else:
    print("You lose!")
