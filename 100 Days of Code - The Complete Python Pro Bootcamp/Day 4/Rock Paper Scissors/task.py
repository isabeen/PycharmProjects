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

game_images = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
print(game_images[your_choice])
comp_choice = random.randint(0, 2)
print(game_images[comp_choice])
if your_choice == comp_choice:
    print("It's a Draw!")
elif your_choice == 0 and comp_choice != 0:
    print("You Win!")
elif comp_choice == 0 and your_choice != 0:
    print("You Lose!")
elif your_choice == 1 and comp_choice == 2:
    print("You Lose!")
else:
    print("You Win!")
