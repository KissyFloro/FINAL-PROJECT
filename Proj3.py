import time
import random

text = [
    "Supercalifragilisticexpialidocious",
    "Pneumonoultramicroscopicsilicovolcanoconiosis",
    "Hippopotomonstrosesquippedaliophobia",
    "Floccinaucinihilipilification",
    "Thyroparathyroidectomized"
]

def typing_master():
    while True:
     print('Are you a keyboard master?')
     print('Well, let us test your skill in this typing master game.')
     print('Type the following text as quickly and accurately as you can')

     print('\nPress Enter when you are ready to start')
     input()

     texts = random.choice(text)
     print(texts)

     start_time = time.time()

     user_input = input("Type the text:")
     end_time = time.time()

     elapsed_time= end_time - start_time
     accuracy = len ([i for i, j in zip (texts, user_input) if i == j]) / len(texts)*100
     print('\nResults:')
     print(f"Elapsed time: {elapsed_time:.2f} seconds")
     print(f"Accuracy: {accuracy: .2f}%")
     print(f'Typed Text: {user_input}')
     print(f'Original Text: {texts}')

     print("Do you want to play again? (yes/no)")
     response = input().lower()
     if response != 'yes':
        break


typing_master()