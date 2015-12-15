###############################
# Physics Equations Done Easy #
# By Matthew Wang, 2015       #
# This program does Physics   #
# Equations for you. :D       #
###############################

import math
end = False
while (end == False):
	print("What kind of equation are you looking for? Speed, Velocity or Acceleration?")
	type = m_rawinput("Type in [S], [V], or [A] respectively.")
	if (type == "[S]"):
		print("You've chosen speed.")
	elif (type == "[V]"):
		print("You've chosen velocity.")
	elif (type == "[A]"):
		print("You've chosen acceleration.")
	else:
		print("Uh oh. Seems like you've entered an unacceptable input.")
		ifend = m_rawinput("Enter [Q] to end the program. Any other inputs will restart the program.")
	if (ifend == [Q]):
		break