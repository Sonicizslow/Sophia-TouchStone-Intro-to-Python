import random

#get user input, recursive if no valid input
def getInput(): 
  global userinput 
  userinput = input("rock, paper, or scissors? ")
  print('You picked: ' + userinput)
  if userinput == "rock":
    return userinput
  elif userinput == "paper":
    return userinput
  elif userinput == "scissors":
    return userinput
  else:
    print("Invalid choice, try again.")
    getInput()

#pick computers choice randomly using random.choice from the random module
def computerChoice():
  global computer 
  computer = random.choice(('rock', 'paper', 'scissors'))
  print('The computer picked: ' + computer)
  return computer


#compare user vs computer choice and declare winner
def compareinputs():
  if userinput == computer:
    print('Tie! Go again!')
    playGame() #restarts the game if tied
  elif userinput == 'rock':
    if computer == 'paper':
      print('You lost!')
    elif computer == 'scissors':
      print('You beat the computer!')
  elif userinput == 'paper':
    if computer == 'scissors':
      print('You lose!')
    elif computer == 'rock':
      print('You beat the computer!')
  elif userinput == 'scissors':
    if computer == 'paper':
      print('You beat the computer!')
    elif computer == 'rock':
      print('You lost!')
  else:
    print('your program failed lol')

#actual run of functions
def playGame():
  getInput()
  computerChoice()
  compareinputs()

#calling the function to run through the other functions 
playGame()
