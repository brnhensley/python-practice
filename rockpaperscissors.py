from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
game_choice = options[randint(0, 2)]

results = {
  "PAPER" : "PAPER COVERS ROCK, YOU %s",
  "ROCK" : "ROCK CRUSHES SCISSORS, YOU %s",
  "SCISSORS" : "SCISSORS CUTS PAPER, YOU %s"}

user_choice = raw_input("""
      ROCK ~ PAPER ~ SCISSORS \n
  CHOOSE ROCK, PAPER, OR SCISSORS
""").upper()

def RPS(user_choice, game_choice):
  outcome = ""
  winner = ""
  print "YOU CHOSE %s, I CHOSE %s" % (user_choice, game_choice)
  if user_choice == game_choice:
    print "\nIT'S A DRAW!"
    choose_again()
    return
  elif user_choice == "ROCK":
    if game_choice == "PAPER":
      outcome, winner = "LOSE", game_choice
    else:
      outcome, winner = "WIN", user_choice
  elif user_choice == "PAPER":
    if game_choice == "SCISSORS":
      outcome, winner = "LOSE", game_choice
    else:
      outcome, winner = "WIN", user_choice
  elif user_choice == "SCISSORS":
    if game_choice == "ROCK":
      outcome, winner = "LOSE", game_choice
    else:
      outcome, winner = "WIN", user_choice
  else:
    print "%s IS NOT AN OPTION, CHEATER" % user_choice
    choose_again()
    return
  print results[winner] % outcome

def choose_again():
  user_choice = raw_input("CHOOSE AGAIN! \n").upper()
  game_choice = options[randint(0, 2)]
  RPS(user_choice, game_choice)

RPS(user_choice, game_choice)