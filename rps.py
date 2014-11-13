import random
tie = "You played the same thing.  TIE!"
win = "You win!"
lose = "You lose!"

player1 = raw_input("Pick one of (r, p, s):... ")


computer_answers = ['r', 'p', 's']
cpu = random.choice(computer_answers)
print "You play %s and the computer plays %s" % (player1, cpu)

def rps(player1, cpu):
	if player1 == cpu:
		print tie
	elif player1 == 'r' and cpu == 'p':
		print lose
	elif player1 == 'r' and cpu == 's':
		print win
	elif player1 == 's' and cpu == 'r':
		print lose
	elif player1 == 's' and cpu == 'p':
		print win
	elif player1 == 'p' and cpu == 'r':
		print win
	elif player1 == 'p' and cpu == 's':
		print lose
	else:
		print "Something went wrong, start over to play again!"

rps(player1, cpu)