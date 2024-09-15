# Setup
#Variables and lists can just be setup, no need for functions
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
#This will save you time entering lots of if else statements

#these definitions or functions are just planned, nothing runs until they are called
def setup():
  name = input("What is your name, adventurer?\n")
  print("Greetings, " + name + ". Let us go on a quest!")
  print("You find yourself on the edge of a dark forest.")
  print("Can you find your way through?\n")
  game_start()
  #this goes to the game_start function below
  #it makes it easier to plana nd change extra parts later on

def game_start():
  response = ""
  while response not in yes_no:
      response = input("Would you like to step into the forest?\nyes/no\n")
      if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
        entry_point()
      elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
      else:
        print("I didn't understand that. Try again\n")

def entry_point():
  response = ""
  while response not in directions:
    print("To your left, you see a bear.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The bear eats you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You head deeper into the forest.\n")
        the_warning()
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = ""
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that. Try again\n")

def the_warning():
  response = ""
  while response not in yes_no:
    response = input("Are you afraid?\nyes/no\n")
    if response == "yes":
        print("Good, only a fool wouldn't be...\n")
    elif response == "no":
        print("You shuold be " + name + " you should be...")
        quit()
    else:
        print("I didn't understand, you are clearly to afraid to type. Try again\n")

#now we can call the first fucntion to run the game
setup()