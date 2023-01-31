import random

# list of possible moves
moves = ["rock", "paper", "scissors"]

while True:
    # get user move
    user_move = input("Enter your move (rock, paper, scissors): ")
    user_move = user_move.lower()

    # check if the move is valid
    if user_move not in moves:
        print("Invalid move, please enter rock, paper or scissors.")
        continue

    # get computer move
    computer_move = random.choice(moves)
    print("Computer move: " + computer_move)

    # compare moves
    if user_move == computer_move:
        print("It's a tie!")
    elif (user_move == "rock" and computer_move == "scissors") \
            or (user_move == "scissors" and computer_move == "paper") \
            or (user_move == "paper" and computer_move == "rock"):
        print("You win!")
    else:
        print("You lose!")

    # ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no) ")
    play_again = play_again.lower()
    if play_again != "yes":
        break
