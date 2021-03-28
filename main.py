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
import random
print("Welcome to Rock, Paper, Scissors.")

player1 = input("Would you like rock, paper, or scissors? ").lower()
if player1 == "rock":
  print(rock)
  rock = 0
elif player1 == "paper":
  print(paper)
  paper = 1
else:
  print(scissors)
  scissors = 2

player2 = random.randint(0, 2)
if player2 == 0:
  print(f"The computer chose rock\n", rock)
  if player1 == "rock":
    print("TIE! 2 rocks, no winner.")
  elif player1 == "paper":
    print("You WIN! Paper beats rock.")
  else:
      print("You LOSE! Rock beats scissors.")
elif player2 == 1:
  print(f"The computer chose paper\n", paper)
  if player1 == "rock":
    print("You LOSE! Paper beats rock.")
  elif player1 == "paper":
    print("TIE! 2 papers, no winner.")
  else:
    print("You WIN! Scissors beat paper.")
else:
  print(f"The computer chose scissors\n", scissors)
  if player1 == "rock":
    print("You WIN! Rock beats scissors.")
  elif player1 == "paper":
    print("You LOSE! Scissors beat paper.")
  else:
    print("TIE! 2 scissors, no winner.")