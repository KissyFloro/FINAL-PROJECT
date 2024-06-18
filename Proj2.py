import csv
import random

def play_game():
  print("Welcome to the quiz game!")
  print("Here's how the game works:")
  print("1. I'll ask you a series of questions.")
  print("2. You'll enter your answer, and I'll tell you if it's correct or not.")
  print("3. You can quit the game at any time by typing 'quit'.")
  print("4. After the game, you'll have the option to review your answers.")
  print("5. You can play again as many times as you want.")
  print()
  print("Let's get started!")
  print()
  
  with open('questions.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    questions = [row for row in reader]

  random.shuffle(questions)

  num_questions = len(questions)
  num_correct = 0

  for i, q in enumerate(questions, 1):
    print(f'Question {i}: {q["question"]}')
    user_answer = input('Your answer: ')
    if user_answer.lower() == q['answer'].lower():
        print('Correct!')
        num_correct += 1
    else:
        print(f'Wrong! The correct answer is {q["answer"]}.')

    cont = input('Press Enter to continue, or type "quit" to stop playing: ')
    if cont.lower() == 'quit':
        break
    
  percent_correct = num_correct / num_questions * 100
  print(f'\nYou got {num_correct}/{num_questions} questions correct ({percent_correct}%).')


  if input('Do you want to review your answers? (y/n) ').lower() == 'y':
    for q in questions:
        print(f'Question: {q["question"]}\nAnswer: {q["answer"]}\n')

  play_again = input('Do you want to play again? (y/n) ')
  if play_again.lower() == 'y':
    play_game()
  else:
   print('Thanks for playing!')
  
play_game()