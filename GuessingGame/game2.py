# Don't forget your comments
import random
number = random.randint(1, 10)
game_limit = 4
player_name = input("Hello, What's your name? ")
number_of_guesses = 0
print("Okay, " + player_name + "! I am guessing a number between 1 and 10, you have " + str(game_limit) + " tries")

while number_of_guesses <= game_limit:
  guess = int(input())
  number_of_guesses += 1 #easy way to add numbers in a loop
  if number_of_guesses == game_limit +1: #still need to guess on the 4th go, so only break on the 5th
    print("Sorry, " + player_name + ", you did not guess the number. The number was " + str(number))
    break
  elif guess == number:
    print("Congratulations, " + player_name + "! You guessed the number in " + str(number_of_guesses) + " tries!")
    break
  elif guess < number:
    print("Your guess is too low.")
  elif guess > number:
    print("Your guess is too high.")
  else:
    break