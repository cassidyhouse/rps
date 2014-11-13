import random

win = "You win!"
tie = "Tie! Try again!"
lose = "You lose!"

user = raw_input("R, P, or S?---> ")

choices = ['Rock', 'Paper', 'Scissors']
computer = random.choice(choices)

if user == "R" or "r":
	print "You play rock!"
elif user == "P" or "p":
	print "You play paper!"
elif user == "S" or "s":
	print "You play Scissors!"
else:
	print "What the heck did you pick? Pick a valid option, please!"

print "The computer plays %s" % computer


if (computer == 'Rock' and user == "R"):
	print tie
if (computer == 'Rock' and user == "P"):
	print win
if (computer == 'Rock' and user == "S"):
	print lose

if (computer == 'Paper' and user == "R"):
	print lose
if (computer == 'Paper' and user == "P"):
	print tie
if (computer == 'Paper' and user == "S"):
	print win


if (computer == 'Scissors'  and user == "R"):
	print win
if (computer == 'Scissors'  and user == "P"):
	print lose
if (computer == 'Scissors'  and user == "S"):
	print tie