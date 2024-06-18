
import random

def roll_dice():
    return random.randint(1,6)

def game():
    you_wins = 0
    player2_wins = 0

    for i in range(3):
        print()
        print(f"ROUND {i+1}:")
        input("It`s YOUR turn to roll the dice. Press ENTER to roll...")
        your_roll = random.randint(1,6)
        print(f"YOU rolled number {your_roll}")
        print()
        print()
        input("It`s PLAYER 2 turn to roll the dice. Press ENTER to roll...")
        player2_roll = random.randint(1,6)
        print(f"Player 2 rolled number {player2_roll}")

        if your_roll > player2_roll:
            print("YOU win this round!")
            print()
        elif player2_roll > your_roll:
            print("PLAYER 2 wins this round!")
            print()
        else:
            print("It`s a TIE!")
            print()

        input("Are you ready for the next round? Press ENTER to continue...")
        print()
    print("FINAL SCORE:")
    you_wins = sum(1 for i in range(3) if random.randint(1,6)>random.randint(1,6))
    player2_wins = 3 - you_wins
    print(f"Your score: {you_wins}")
    print(f"Player 2 score: {player2_wins}")

    if you_wins > player2_wins:
        print("YOU WON THE GAME!")
    elif player2_wins > you_wins:
        print("PLAYER 2 WON THE GAME!")
    else:
        print("IT`S A TIE!")
game()
        