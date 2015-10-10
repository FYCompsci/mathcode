#########################################
#  Prime Checker, by Matt Wang (2015)   #
#                                       #
# The goal of this program was to find  #
# whether or not a number is prime, not #
# having 500 error messages. ;), Enjoy! #
#########################################
#import
import math

#function that checks if the input is a number
def numcheck (num):
	try:
		int(num)
		return True
	except ValueError:
		return False
print("Prime Number checker loaded.")
'''
Boring way to check if number is prime
#function that checks if a number is prime
def checkprime (num):
	if (number <= 1):
		return False
	for i in range(2,num):
		if num % (i) == 0 and num != i:
			return False
	return True
'''
#super cool way to check for prime-ness
def checkprime (num):
	if num == 2 or num == 3:
		return True
	elif num % 2 == 0 or num % 3 == 0:
		return False;
	else:
		int counter = 5
		while counter*counter <= num:
			if num % counter == 0 or num % (counter+2) == 0:
				return False
			counter += 6
		return True
#main loop for the program
while True:
	inp = raw_input("Enter an positive integer: ")
	#checks if input is a number
	if numcheck(int(inp)) == False or int(inp) < 0:
		endclause = raw_input("Welp you entered a wrong type input! If you want to exit, type in \"esc\". Other inputs will start the program again.")
	else:
		# 0 and 1 are special cases, neither prime nor composite
		if int(inp) == 0 or int(inp) == 1:
			print("Ooh, this is a tricky one. " + inp + " isn't prime or composite!")
		#if num aint prime, its composite
		elif checkprime(int(inp)) == False:
			print("Composite")
		#if num is prime, its prime
		else:
			print("Prime")
		#goes through input check if the user wants to quit
		endclause = raw_input("Hope that helped! If you want to continue, type in \"cont\". Other inputs will start the program again.")
	#breaks mainloop if user wants to leave
	if endclause != ("cont"):
		break
	else:
		print("Restarting ...")
