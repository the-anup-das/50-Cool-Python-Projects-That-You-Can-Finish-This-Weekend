import random

#check https://ascii.co.uk for the pics
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

user_choice = int(input("What do you choose? \nType 0 for Rock\n1 for paper\n2 for scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid number, you lose!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer Chose:\n",game_images[computer_choice])

    #rock = scissors win
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice < user_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
    else:
        print("You lose")
    

