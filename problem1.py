#Name: Hien Do & Huong Le
#Evergreen Login: dohie11 & lethi17
#Computer Science Foundation
#Programming as a way of life
#Homework1



import math


def solver( a, b, c):
	delta = (b*b) - (4*b*c)

	if delta < 0 :
		print ("None")
	
	elif delta == 0 :
		x = -b / (2 * a)
		print(x)
	
	elif delta > 0 :
		x1 = ( -b + math.sqrt( delta )) / (2 * a)
		x2 = ( -b - math.sqrt( delta )) / (2 * a)
		print ( str(x1) + " " + str(x2) )
		
solver(1, -5.86, 8.5408)

