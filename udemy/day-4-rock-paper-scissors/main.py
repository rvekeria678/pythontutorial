# Day 4: Rock, Paper, Scissors

import random

move = {0: '''
    Scissors
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
''', 1:'''
    Rock
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
''', 2:'''
    Paper
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)
'''}

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

player = int(input())
computer = random.randint(0,2)

print(move[player])
print('Computer chose:')
print(move[computer])

if player == computer:
    print('Draw')
elif player == 0 and computer == 2:
    print('You win')
elif player == 1 and computer == 0:
    print('You win')
elif player == 2 and computer == 1:
    print('You win')
else:
    print('You lose')

