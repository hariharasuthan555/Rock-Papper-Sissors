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
user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("Your Choice:")
if user_choice==0:
  print(rock)
elif user_choice==1:
  print(paper)
elif user_choice==2:
  print(scissors)
else:
    print("Wrong Choice!")
    sys.exit()

print("computer chooses:\n")
computer_choice=random.randint(0,2)
if computer_choice==0:
  print(rock)
elif computer_choice==1:
  print(paper)
else:
  print(scissors)

if user_choice==0 and computer_choice==0:
    print("\nIt's a draw!")
elif user_choice==0 and computer_choice==1:
    print("\n Computer Won...")
elif user_choice==0 and computer_choice==2:
    print("\n You Won!")
elif user_choice==1 and computer_choice==0:
    print("\n You Won!")
elif user_choice==1 and computer_choice==1:
    print("\n It's a draw!")
elif user_choice==1 and computer_choice==2:
    print("\n Computer Won...")
elif user_choice==2 and computer_choice==0:
    print("\n Computer Won...")
elif user_choice==2 and computer_choice==1:
    print("\n You Won!")
else:
    print("\n It's a draw!")
