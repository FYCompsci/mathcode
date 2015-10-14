# -*- coding: utf-8 -*-
#Give two points in an xy plane
#Returns the line that those points are on
#By Zack Nathan

from time import sleep

class color:
    b = '\033[1m'
    e = '\033[0m'

#Insert any 2 points in the format (a,b) (x,y)
#This program will give you the line formula, and intercepts.

print '\nEnter in the format: (a,b) (x,y)'
print 'Example: (8,6) (3,7)'
print '         (2.8,-9) (-1,3.3)'
print '         (-2.22,34) (6,31.8)'
print 'Add spaces between the points, but not at the start'
print 'Add commas between the x and y values of each point, but not between the points'

q = 1
while True:

	while True:

		points = raw_input('\n\n%s. ' % q)
		if points.count('(') == 2 and points.count(')') == 2 and points.count(',') == 2:

			points = points.split(' ')
			points[0] = points[0].strip('()')
			points[1] = points[1].strip('()')
			points[0] = points[0].split(',')
			points[1] = points[1].split(',')

			if len(points[0][0]) > 0 and len(points[0][1]) > 0 and len(points[1][0]) > 0 and len(points[1][1]) > 0:
				break

		print color.b + 'Error: Invalid input format' + color.e

	try:
		x1 = float(points[0][0])
		y1 = float(points[0][1])
		x2 = float(points[1][0])
		y2 = float(points[1][1])

		changeinx = x1 - x2
		changeiny = y1 - y2

		if changeinx == 0:
			print '\nx = %s' % x1
			print '\nx intercept: %s' % y1

		elif changeiny == 0:
			print '\ny = %s' % y1
			print '\ny intercept: %s' % x1
		
		slope = changeiny/changeinx
		b = (-x1*slope)+y1
		xintercept = -b/slope

		if b >= 0:
			print '\ny = (%s)x + %s' % (slope, b)
		else:
			print '\ny = (%s)x - %s' % (slope, b)

		print '\ny intercept: %s' % b
		print 'x intercept: %s' % xintercept

		q += 1

	except TypeError:
		print color.b + 'Error: Invalid input format' + color.e

	except IndexError:
		print color.b + 'Error: Invalid input format' + color.e

	sleep(2)
