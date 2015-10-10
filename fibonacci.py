#########################################
# Fibonacci Maker, by Matt Wang (2015)  #
#                                       #
# The goal of this program was to find  #
# the numbers in the Fibonacci sequence,#
# without the hassle of google. Enjoy!  #
#########################################
#imports
from math import *
#checks for number input
def numcheck (num):
	try:
		int(num)
		return True
	except ValueError:
		return False
#
#sketchy math that works, trust me


def fibo (num):
	#method one
	s = sqrt(5);
	a = (1 + s) / 2;
	b = 1/a;
	return int( (a**num + b**num) / s + 0.5 )
	#method two
	'''
	if n < 2:
        return num
    fibPrev = 1
    fibCur = 1
    for i in range(2, num):
        fibPrev, fibCur = fibCur, fibCur + fibPrev
    return fibCur
	'''
	



print ("Fibonacci Sequence Machine loaded.")

while True:
	inp = raw_input("How many numbers of the Fibonacci Sequence are you looking for? ")
	#checks if input is a number
	if numcheck(int(inp)) == False or int(inp) < 0:
		endclause = raw_input("Welp you entered a wrong type input! If you want to try again, type in \"cont\". Other inputs will start the program again.")
	else:
		#prints out what we get from the fibo function
		for i in range(1,int(inp)):
			print fibo(i)

		#goes through input check if the user wants to quit
		endclause = raw_input("Hope that helped! If you want to continue, type in \"cont\". Other inputs will start the program again.")
	#breaks mainloop if user wants to leave
	if endclause != ("cont"):
		break
	else:
		print("Restarting ...")
