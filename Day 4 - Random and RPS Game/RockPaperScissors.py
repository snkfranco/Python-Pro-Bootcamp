import random

person_value = int(input('What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS:   '))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_value = random.randint(0,2)

choices = ['rock', 'paper', 'scissors']

if person_value == 0:
    print(f'Your choice: {rock}')
elif person_value == 1:
    print(f'Your choice: {paper}')
elif person_value == 2:
    print(f'Your choice: {scissors}')

if computer_value == 0:
    print(f'Computer choice: {rock}')
elif computer_value == 1:
    print(f'Computer choice: {paper}')
elif computer_value == 2:
    print(f'Computer choice: {scissors}')

if person_value == computer_value:
    print("\n It's a DRAW!")

elif person_value == 0 and computer_value == 1:
    print('\n Computer WINS!')

elif person_value == 0 and computer_value == 2:
    print('\n You WIN!')

elif person_value == 1 and computer_value == 0:
    print('\n You WIN!')

elif person_value == 2 and computer_value == 1:
    print('\n You WIN!')
    
elif person_value == 1 and computer_value == 2:
    print('\n Computer WINS!')

elif person_value == 2 and computer_value == 0:
    print('\n Computer WINS!')