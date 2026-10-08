
import random

#Function 1
def get_player_choice():
    user_guess = input("Enter rock, paper, scissors: ").lower()

    while user_guess != "rock" and user_guess != "paper" and user_guess != "scissors":
        print(f"{user_guess} is an invalid choice. Try again!")
        user_guess = input("Enter rock, paper, scissors: ").lower()

    return user_guess


#Function 2
def determine_winner(user_guess, random_rock_paper_scissors):
    if user_guess == random_rock_paper_scissors:
        return "tie"
    if user_guess == "rock" and random_rock_paper_scissors == "scissors":
        return "win"
    if user_guess == "paper" and random_rock_paper_scissors == "rock":
        return "win"
    if user_guess == "scissors" and random_rock_paper_scissors == "paper":
        return "win"

    return "loss"


print("Welcome to Rock, Paper, Scissors!")

#Let them chose the number of rounds and the only limitation is that it is an integer that cant be even
number_of_rounds = 0

while number_of_rounds % 2 == 0:
    number_of_rounds = int(input("How many rounds would you like to play: "))
    if number_of_rounds % 2 == 0:
        print("Sorry, the number must be an odd number")


user_score = 0
computer_score = 0

while number_of_rounds != 0:
    user_guess = get_player_choice()

    random_number = random.randint(1, 3)

    if random_number == 1:
        random_rock_paper_scissors = "rock"
        print("The computer chose rock")
    if random_number == 2:
        random_rock_paper_scissors = "paper"
        print("The computer chose paper")
    if random_number == 3:
        random_rock_paper_scissors = "scissors"
        print("The computer chose scissors")

    result = determine_winner(user_guess, random_rock_paper_scissors)

    if result == "tie":
        print("Tie! Play again")

    if result == "win":
        print("You won!")
        user_score += 1
        number_of_rounds -= 1

    if result == "loss":
        print("You lose!")
        computer_score += 1
        number_of_rounds -= 1


win_loss_tie = "Win"

if user_score > computer_score:
    win_loss_tie = "won"
if computer_score > user_score:
    win_loss_tie = "lost"
if user_score == computer_score:
    win_loss_tie = "tied"

print()
print(f"Score --- You: {user_score} Computer: {computer_score}")
print(f"You {win_loss_tie}")
print("Thanks for playing")
