# Rasheed's Project
# Programming in 5 days
import time
import random
def createBorder():
	print "______________________________"


def start():

	name=raw_input("Knock knock, who's there? ")	

	print name + " who?"
	time.sleep(1)
	print name + " is awesome."
	time.sleep(1)
	question=raw_input("what brings you here today? ")
	time.sleep(1)
	print question + ": is not an important reason but who cares."
	time.sleep(1)

	createBorder()

	print "To play, or not to play? That is the question."
	time.sleep(1.5)
	print "This game ensures only the survival of the fittest."
	time.sleep(1.5)
	print "You must answer 5 good riddles before you can claim the ultimate prize."
	time.sleep(1.5)
	createBorder()
	print "WARNING: first letter of answers must be capitalize."
	createBorder()

	print "Begin..."
	time.sleep(1.8)

	#First Riddle
	print "First Riddle:"
	time.sleep(1)
	first=raw_input("The more you take, the more you leave behind, What am I? ")
	if first!="Footsteps":
			print "You lost. Lucky numbers: 27, 5, 16, 34, 14, 8"
			return
	else:
		print "mmmhh... that was easy."

	createBorder()

	#Second Riddle 
	print "Second Riddle:"
	time.sleep(1)
	second=raw_input("What is harder to catch the faster you run? ")
	if second!="Your breath":
			print "You lost. Lucky numbers: 10, 13, 18, 31, 35, 36"
			return
	else:
		print "'oh my days!'"

	#Third Riddle
	print "Third Riddle:"
	time.sleep(1)
	third=raw_input("What disappears the moment you say its name? ")
	if third!="Silence":
			print "You lost. Lucky numbers: 55, 27, 14, 44, 15, 01"
			return
	else:
		print "'You are a lover of words, someday you should write a book'"
	time.sleep(1)
	#Fourth Riddle
	print "Fourth Riddle:"
	time.sleep(1)
	fourth=raw_input("What is big and yellow and comes in the morning, to brighten mom's day? ")
	if fourth!="School bus":
			print "You lost. Lucky numbers: 45, 21, 33, 17, 3, 20"
			return
	else:
		print "'You should be able to make money and hold on to it'"
	time.sleep(1)
	#Fifth Riddle
	print "Fifth Riddle:"
	time.sleep(1)
	fifth=raw_input("What belongs to you but others use it more than you do? ")
	if fifth!="Your name":
			print "You lost. Lucky numbers: 36, 47, 5, 27, 12, 42"
			return
	else:
		print "'Financial prosperity is coming your way'"

	createBorder()

	time.sleep(1.5)

	print "Not too fast..."
	print "You must be me in a game of Rock, Paper, Scissors"

	rps=raw_input("Enter rock, paper or scissors: ")
	if rps=="Rock":
		print "I chose scissors, you won."
	elif rps=="Scissors":
		print "I chose rock, you lose."
		return
	elif rps=="Paper":
		print " I chose scissors, you lose."
		return

	time.sleep(1.5)
	print "Oh, the places you'll go!"
	time.sleep(1.5)
	print "Please roll a dice"
	x=random.choice(["1","2","3","4","5","6"])
	print "You rolled a " + x
	time.sleep(1.5)
	print "You've won " + x + " dollars"
	time.sleep(1.5)

	print "Made by Rasheed Adewole"













