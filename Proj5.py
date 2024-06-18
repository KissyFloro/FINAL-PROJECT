
import random
def game():
    choices = ["rock", "paper","scissor"]
    player_wins = 0
    computer_wins = 0

    while True:
        user_choice = input('Enter your choice (rock, paper, scissor):').lower()
        while user_choice not in choices:
            user_choice = input('Invalid choice. Try again (rock, paper, scissor):')

        computer_choice = random.choice(choices)
        print(f'\nComputer chose {computer_choice}.\n')

        if user_choice == computer_choice:
            print(f"It`s a tie! Both players selected {user_choice}")
        elif user_choice == 'rock':
            if computer_choice == "scissors":
                print('Rock smashes scissors! You win!')
                player_wins += 1
            else:
                print("Paper covers rock! You lose.")
                computer_wins += 1
        elif user_choice == 'paper':
              if computer_choice == "rock":
                print('Paper covers rock! You win!')
                player_wins += 1
              else:
                print("Scissor cuts paper! You lose.")
                computer_wins += 1
        elif user_choice == 'scissor':
              if computer_choice == "paper":
                print('Scissor cuts paper! You win!')
                player_wins += 1
              else:
                print("Rock smashed scissor! You lose.")
                computer_wins += 1
        print(f"Score - You: {player_wins}, Computer: {computer_wins}\n")
        if player_wins == 2:
              print("You win the game!")
              break
        elif computer_wins == 2:
              print("Computer wins the game!")
              break

game()

   


