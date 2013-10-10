
import math

math.factorial(10)

n = 1

accumulator2 = 1.0

while n <= 10:

	accumulator = 1
	
	for i in range ( 1 , n + 1 ) :

		accumulator = accumulator * i
	
	accumulator2 = accumulator2 + ( 1.0 / accumulator)
	n = n + 1

	
print accumulator2

	
	
	


