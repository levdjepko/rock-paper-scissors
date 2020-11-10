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

playerChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n' ))

if (playerChoice == 0):
  print (rock)
elif (playerChoice == 1):
  print (paper)
elif (playerChoice == 2):
  print (scissors)  

  # computer picks
computerChoice = random.randint(0,2)

print ('Computer chose:')
if (computerChoice == 0):
  print (rock)
elif (computerChoice == 1):
  print (paper)
elif (computerChoice == 2):
  print (scissors)  

if (playerChoice == 0):
  if (computerChoice == 0):
    print ('Draft')
  elif (computerChoice == 1):
    print ('Computer wins') 
  else:
    print ('You win!')  
if (playerChoice == 1):
  if (computerChoice == 1):
    print ('Draft')
  elif (computerChoice == 2):
    print ('Computer wins') 
  else:
    print ('You win!') 
if (playerChoice == 2):
  if (computerChoice == 2):
    print ('Draft')
  elif (computerChoice == 0):
    print ('Computer wins') 
  else:
    print ('You win!')      
