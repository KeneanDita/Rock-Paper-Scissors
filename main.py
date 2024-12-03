import random
import math

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true if the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of():
    # Ask the user how many games they want to play
    while True:
        try:
            n = int(input("How many games would you like to play? Enter an odd number (e.g., 3, 5, 7): "))
            if n % 2 == 0:
                print("Please enter an odd number to ensure there is a winner.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid odd number.")

    # Play against the computer until someone wins best of n games
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n / 2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print(f"It is a tie. You and the computer have both chosen {user}.\n")
        # you win
        elif result == 1:
            player_wins += 1
            print(f"You chose {user} and the computer chose {computer}. You won!\n")
        else:
            computer_wins += 1
            print(f"You chose {user} and the computer chose {computer}. You lost :(\n")

    if player_wins > computer_wins:
        print(f"You have won the best of {n} games! What a champ :D")
    else:
        print(f"Unfortunately, the computer has won the best of {n} games. Better luck next time!")

if __name__ == '__main__':
    play_best_of()
