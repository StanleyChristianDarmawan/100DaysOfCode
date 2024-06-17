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

image = [rock, paper, scissors]
userHand = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n\t"))
computerHand = random.randint(0, 2)

if (userHand > 2):
    print("You typed an invalid number, you lose!")
else:
    print(image[userHand])
    print("Computer Chose:")
    print(image[computerHand])

    if (userHand == 0 and computerHand == 2):
        print("You win!")
    elif (userHand == 2 and computerHand == 0):
        print("You lose")
    elif (userHand > computerHand):
        print("You win!")
    elif (userHand < computerHand):
        print("You lose")
    elif (userHand == computerHand):
        print("draw")

