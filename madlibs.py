# Madlib from freecodecamp

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "It's madlib time, stupid"

name = raw_input("Enter a name: ")
adj1 = raw_input("Enter an adjective: ")
adj2 = raw_input("Enter another adjective: ")
adj3 = raw_input("Enter another adjective: ")
verb = raw_input("Enter a verb: ")
noun1 = raw_input("Enter a noun: ")
noun2 = raw_input("Enter another noun: ")

animal = raw_input("Enter a animal: ")
food = raw_input("Enter an food: ")
fruit = raw_input("Enter a fruit: ")
superhero = raw_input("Enter a superhero: ")
country = raw_input("Enter a country: ")
desert = raw_input("Enter a dessert: ")
year = raw_input("Enter another year: ")

print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, desert, name, year, noun2)
