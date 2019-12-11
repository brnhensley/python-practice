# dice roll guessing game

from random import randint
from time import sleep

def get_user_guess(max_value):
#   odds = (1. / (max_value - 2)) * 100
  guess = int(raw_input("""
    TRY TO GUESS THE DICE ROLL (2-%d)
  """ % max_value))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_value = 2 * number_of_sides
  guess = get_user_guess(max_value)
  total_roll = first_roll + second_roll
  odds = calc_odds(number_of_sides, guess) * 100

  if guess < 2 or guess > max_value:
    print "\n YOUR GUESS HAS TO BE BETWEEN 2 AND %d \n" % max_value
  else:
    print "\nYOUR ODDS OF ROLLING A %d IS %.3f %% \n" % (guess, odds)
    print "ROLLING...\n"
    sleep(.75)
    print "FIRST ROLL IS A %s \n" % str(first_roll)
    sleep(.75)
    print "SECOND ROLL IS A %s \n" % str(second_roll)
    sleep(.75)
    print "TOTAL ROLL IS A %s \n" % str(total_roll)
    sleep(.5)
    if guess == total_roll:
      print "       YOU RULE DUDE!\n"
    else:
      print "       ANOTHER LOSER\n"

def calc_odds(sides, guess):
    possible_outcomes = sides ** 2
    combos = 1.
    if guess > 2:
        for i in range(1, sides + 1):
            for j in range(1, sides + 1):
                if i + j == guess:
                    combos += 1
    return float(combos / possible_outcomes)

die = int(raw_input("""
            DICE SIMULATOR, I WILL ROLL 2 DICE

     HOW MANY SIDES ARE ON THE DICE YOU WANT TO PLAY WITH?\n\n"""))

roll_dice(die)