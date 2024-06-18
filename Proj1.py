import random

def number_guessing_game():
  while True:
    my_number = random.randint (1,100)
    guess = None

    print("Are you ready to test your luck?")
    print('Welcome to the Number Guessing Game!')
    print('I have selected a number between 1 and 100.')
    print('Try to guess it!')

    while guess != my_number:
      guess = int(input('Enter a number:'))

      if guess < my_number:
        print('Ops! Too low. Try again.')
      elif guess > my_number:
        print("Ops! Too high! Try again. ")
      else:
        print('Wow! You guess the correct number! CONGRATULATIONS!')
   
    print('\nDo you want to play again? (yes/no)')
    response = input().lower()
    if response!= 'yes':
      break
number_guessing_game()

    

