

n = 19

series = "Fibonacci"

if series == "Fibonacci":
   a = 0
   b = 1
   for i in range( n - 1 ):
		a = b
		b = a+b
		print a
elif series == "sum":
    i = 0
    l = 0
    while i < ( 3 * n ):
       x = 3
       i =+ (i+x)
       l = i + l
       print l
else:
    print "Invalid String"
