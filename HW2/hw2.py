# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

n = 100

accumulator = 0

i = 1

while i <= n :
	
	accumulator = accumulator + i
	
	i = i + 1
	
print accumulator



###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"


l = range( 2, 11 )

for i in l:
	
	print 1.0/i
	
	

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10

accumulator = 0

for i in range ( 1, n + 1 ):

	accumulator = accumulator + i 

print accumulator

print (n * ( n + 1 )) / 2 


###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"
import math

math.factorial(10)

n = 10

accumulator = 1

for i in range ( 1 , n + 1 ) :

	accumulator = accumulator * i
	
print accumulator
	
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

import math

math.factorial(10)

n = 10

while n > 0:

	accumulator = 1
	
	for i in range ( 1 , n + 1 ) :

		accumulator = accumulator * i
	
	print accumulator
	n = n - 1
	
###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

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

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# its about 16 hours for me to complete the homework. The lecture is very helpful for me , however, I can not catch up all the information in class. 
# I used math skills to find out good way to finish the problem first, then come back with python right after that.
# There are some code I could not understand, the tutor have to spend 30-45 minutes to explain it for me.
# They explain what the different between "for" and " while" for me, which I could not understand clearly in class.