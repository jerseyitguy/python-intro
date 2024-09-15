# Don't forget your comments
import random
number = random.randint(1, 10)
player_name = input("Hello, What's your name? ")
print("Okay, " + player_name + "! I am guessing a number between 1 and 10, make your guess:")

while True: #while lets us loop indefinately, True must have a capital
  guess = int(input())
  if guess == number: # == is used to compare values, = is used to assign them
    print("Congratulations, " + player_name + "! You guessed the number!")
    break
    #without the break you will not end the game and have to reset it
    #you can only use break in a loop, or you use quit()
  elif guess < number:
    #elif means else if, you use this when you have more than two outcomes
    print("Your guess is too low.")
  elif guess > number:
    print("Your guess is too high.")
  else:
    break #this is used to break the game if you have something happens you didn't think of