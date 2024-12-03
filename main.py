import random
from turtledemo.nim import computerzug


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "You and the computer have chosen {}. It's a Tie".format(computer)
    if isWin(user, computer):
        return "You have chosen {} and the computer has chosen {}. You Won".format(user, computer)
def isWin(player, opponent):
    if(player == 'r' and opponent=='s') or (player=='s'and opponent=='p') or (player=='p'and opponent=='r'):
        return True
    return False


if __name__ == '__main__':
    print(play())