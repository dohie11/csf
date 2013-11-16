# Name:  Group 16: Hien Do, Travis Goodroad, Amber Hare
# Evergreen Login: dohie11 , gootra28, hartra06
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

"""
Problem 3
First let's take a look at how nested data structures function so we can understand how best to utilize them
What kind of data structures do we already know about?
Create one of each and assign them all do a different value.
How can we combine these different kinds of data structures to create nested data structures?
Create a list of tuples, a list of dictionaries and one other nested data structure of your choice.
"""

#put your data structures here

"""
Problem 4
Let's take a closer look at how dictionaries work.
A dictionary is a data structure that maps keys to values, much in the same way that physical dictionaries match words to definitions.
Create an dictionary called Hamburger with key & value pairs Condiment:Ketchup, Meat:Beef, Bun:Sesame.
"""

#put the dictionary here

"""
Problem 5
Now that we have our basic hamburger dictionary, we can begin to add more things to it.
Adding to dictionaries does not use the add() or append() functions used in lists.
To add a key & value pair to a dictionary called "okay" we have to use the function okay['key'] = value
Add 3 of your favorite toppings to the hamburger dictionary, assigning them all to different keys (i.e. Lettuce:Romaine, Cheese:Cheddar)

"""

#put your code here

"""
Problem 6
Our hamburger is now almost done but you suddenly realized that you would like to change a few of the items on the burger.
We first have to know how to index and locate items in the dictionary.
Fortunately, python makes this very easy for us.
All we have to do is enter the name of the dictionary and then index it with the key.
For example, say you want to find the value of the key "Cereal" in the dictionary "Breakfasts".
All we have to do is enter Breakfast[Cereal] (which in this case would return "Not a real breakfast").
We can use this to change the value assigned to a key in the same way we can reassign values to variables.
If we want to change the value of the "Cereal" key from "Not a real breakfast" to "Delicious" we can enter Breakfast[Cereal] = "Delicious"
Change the "Bun" on your "Hamburger" to "Toasted" and the "Condiment" to "Ketchup and Mustard".

"""

#put your code here

"""
Problem 7
Let's now think about how this applies to the problem in hw5.
We are given a large list of states to assign edge values to.
The formula for finding the values of the edge is already given to us so we just need to figure out a way to assign a bunch of values to keys in a given list.
For loops can be very helpful but figuring out what to iterate them over can be tricky.
What would a for loop used for problem 1 in hw5 iterate over?
"""

#put your for loop here, add a pass keyword inside the loop