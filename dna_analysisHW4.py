# Name: Hien Do
# Evergreen Login: dohie11
# Computer Science Foundations
# Programming as a Way of Life
# Homework 4: DNA analysis 

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line

        


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
g_count = 0
c_count = 0
a_count = 0
t_count = 0
invalidcount = 0


### Got bored want to change this to function and see if it works
### but cant get it to work then Alex came over and said we are not suppose
### to change it to a function.
#def bps(n)
#    if bp == 'n'
#    n = n + 1
#    return n


#g_count  = bps(g)
#c_count  = bps(c)
#a_count  = bps(a)
#t_count  = bps(t)

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1
    # next, if the bp is a G or a C,
    if bp == 'G':
        g_count += 1
    elif bp == 'C':
        c_count += 1
    elif bp == 'A':
        a_count += 1
    elif bp == 'T':
        t_count += 1
    else:
        invalidcount += 1
        
    
        


# reduced a few lines by moving gc_content. G+C and A+T is the same as GC and AT alone
gc_content = float(g_count+c_count) / total_count
at_content = float(a_count+t_count) / total_count

# GC/AT Ratio using the counts 
## Float give decimals. Without it it doesnt. I forgot about this.
## too many hours
gcat_ratio = float(g_count+c_count) / (a_count+t_count)

# Calculate if high, low , or moderate using else if statements.
if gc_content >= 0.6:
	gclowhigh = 'High GC content'
elif gc_content < 0.4:
	gclowhigh = 'Low GC content'
else:
	gclowhigh = 'Moderate GC content'

# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G: ', g_count
print 'C: ', c_count
print 'A: ', a_count
print 'T: ', t_count
print 'Sum:', (a_count + c_count + g_count + t_count)
print 'Invalid Count:', invalidcount
print 'Total Count (sum & invalids):', total_count
print 'AT-GC Ratio:', gcat_ratio
print 'Seg Length', len(seq)
print 'GC Classification: ', gclowhigh


