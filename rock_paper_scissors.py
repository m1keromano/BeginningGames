import random


options = ["Rock", "Paper", "Scissors"]
#Computer makes a choice
computer_choice = random.choice(options)

#Player makes a choice
player_choice = input("Choose R, P, or S: ")

#Dictionary to convery player choice to word
choices = {
    "R" : "Rock", 
    "P" : "Paper",
    "S" : "Scissors"
}

converted_player_choice = choices.get(player_choice)

print(f"You chose {converted_player_choice}")
print(f"The computer chose {computer_choice}")


if computer_choice == converted_player_choice:
    print("It's a Tie!")

if computer_choice == "Rock" and converted_player_choice == "Scissors":
    print("Computer Wins!")

if computer_choice == "Scissors" and converted_player_choice == "Rock":
    print("You Win!")

if computer_choice == "Paper" and converted_player_choice == "Rock":
    print("Computer Wins!")

if computer_choice == "Rock" and converted_player_choice == "Paper":
    print("You Win!")

if computer_choice == "Scissors" and converted_player_choice == "Paper":
    print("Computer Wins!")

if computer_choice == "Paper" and converted_player_choice == "Scissors":
    print("You Win!")