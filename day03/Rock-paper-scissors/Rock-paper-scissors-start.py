import random


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

print("Welcome to the game rock paper and scissors")
Player1 = input("What is your name?")

player_choice = input("What do you want to put Rock(R), Paper(P), or Scissor(S) ?")
if player_choice == "P":
    player_choice = paper
elif player_choice == "R":
    player_choice = rock
else:
    player_choice = scissors

shapes = [rock,paper,scissors]

computer_choice = random.choice(shapes)

if player_choice == paper and computer_choice == rock:    
    print(f"Player: \n {paper} \n Computer \n {computer_choice}")
    print(f"**** {Player1} won !! ******")

elif player_choice == rock and computer_choice == scissors:
    print(f"Player: \n {rock} \n Computer \n {computer_choice}")
    print(f"**** {Player1} won!! *****")
elif player_choice == scissors and computer_choice == paper:
    print(f"Player: \n {scissors} \n Computer \n {computer_choice}")
    print(f"**** {Player1} won!! *****")
elif computer_choice == player_choice:
    print(f"Player: \n {player_choice} \n Computer \n {computer_choice}")
    print("EMpate")
else:
    print("****Computer won*****")