import art
import random

# Initializing variables
Game_count = 0
Choice_array = [0, 1, 2]
User_win = 0
Comp_win = 0

while Game_count <= 2:
    comp_choice = random.choice(Choice_array)
    user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
    print(
        f"\n Computer chose = {art.logo[comp_choice]}")
    print(
        f"You chose = {art.logo[user_choice]}")

    if (user_choice == 2 and comp_choice == 0):
        print("You lost this round\n")
        Comp_win += 1  # Append one win in the computer's varirable
    elif (
            user_choice > comp_choice):
        print("You won this round\n")
        User_win += 1
    elif (comp_choice == 2 and user_choice == 0):
        print("You won this round\n")
        User_win += 1
    elif (
            comp_choice > user_choice):
        Comp_win += 1
        print("You lost this round\n")
    else:
        print("This round is a draw\n")

    Game_count += 1

if (User_win > Comp_win):
    print("You won the tournament")
elif (User_win < Comp_win):
    print("You lost the tournament")
else:
    print("The tournament ended in a draw")
