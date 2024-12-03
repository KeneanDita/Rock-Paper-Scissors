import random
def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])
