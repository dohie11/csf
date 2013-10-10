
import math

math.factorial(10)

n = 10

while n > 0:

	accumulator = 1
	
	for i in range ( 1 , n + 1 ) :

		accumulator = accumulator * i
	
	print accumulator
	n = n - 1
	
	


