"""Logic game, you must guess a secret 5digit number based on clues.
Pico = you have guessed a correct digit, but in the wrong place
Fermi = you have guessed a correct digit in the correct place
Bagels = you have not guessed any correct digits at all
You have 15 tries! """

#TODO: use Django template? 
import random
import datetime

number_of_digits = 2
max_number_of_guesses = 6
currentTime = datetime.datetime.now()
currentTime.hour


def main():
      while True:
            secret_number = getSecretNum()
            if currentTime.hour < 12:
                  print("Good morning my player! I wish you a beautiful day, let's play with me!")
            elif 12 <+ currentTime.hour < 18:
                  print("Good afternoon my player! I wish you a lovely rest of your day, so let's play with me!")
            else:
                  print("Good evening my favorite player! Did you have a wonderful day? Let's play with me")
            name_of_player = input("What's your name? I'm Bagy Bagel. ")
            print("Nice to meet you {}. Lets play Bagels!\
            I'm thinking of a {}-digit number with no repeated digits.".format(name_of_player, number_of_digits))
            print("You have to guess it. You will tell me the number and I will answer you: \
a) Pico = one digit is correct but in the wrong position \
b) Fermi = one digit is correct and in the right position \
c) Bagels = no digit is correct ")
            print("I have thought up a number. You have {} guesses to get it".format(max_number_of_guesses))

            numGuesses = 1
            while numGuesses <= max_number_of_guesses:
                  guess = ""
                  while len(guess) != number_of_digits or not guess.isdecimal():
                        print("what is your {} guess? Tell me these {} numbers.".format(numGuesses, number_of_digits))
                        guess = input("> ")
                  
                  clues = getClues(guess, secret_number)
                  print(clues)
                  numGuesses +=1
                  
                  if guess == secret_number:
                        break
                  if numGuesses > max_number_of_guesses:
                        print("Oh no, {}.You ran out of guesses.".format(name_of_player))
                        print("The answer was: {}".format(secret_number))
            
                  print("Do you want to play again? (yes or no)")
                  if not input("> ").lower().startswith("y"):
                        break
            print(" Thanks for playing. Hope to see you soon! ")

def getSecretNum():
      numbers = list("0123456789")
      random.shuffle(numbers)
      secret_number = ""
      for i in range(number_of_digits):
            secret_number += str(numbers[i])
      return secret_number

def getClues(guess, secret_number):
      if guess == secret_number:
            return "You got it!"
      
      clues = []
      
      for i in range(len(guess)):
            if guess[i] == secret_number[i]:
                  clues.append("Fermi! ")
            elif guess[i] in secret_number:
                  clues.append("Pico ")
      if len(clues) == 0:
            return "Bagels :( "
      else:
            clues.sort()
            return "".join(clues)

if __name__=="__main__":
      main()
