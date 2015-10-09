'''
Leibniz created the following formula for pi:
pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) ...
'''

from __future__ import division
import sys

pi = 0
denominator = 1
add = True

# I know that this shows the value of pi, but it is only being used so that the program does not loop forever
# The program does not need to know this value to find the value of pi
while pi != 3.14159265359:

    if add:
        pi += 4 / denominator
        add = False
    else:
        pi -= 4 / denominator
        add = True

    sys.stdout.write('\rpi = ' + str(pi))
    sys.stdout.flush()

    denominator += 2
