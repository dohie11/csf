# Name: Hien Do
# Evergreen Login: dohie11
# Computer Science Foundations
# Programming as a Way of Life

import networkx as nx
import matplotlib.pyplot as plt
import operator
import random


###
### Problem 1a
###

practice_graph = nx.Graph()

#nodes
"""
practice_graph.add_node("A")
#practice_graph.add_node("B")
#practice_graph.add_node("C")
#practice_graph.add_node("D")
#practice_graph.add_node("E")
#practice_graph.add_node("F")
"""
practice_graph.add_nodes_from(["A","F"])

#edges
practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("D", "E")

assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

def draw_practice_graph():
    """Draw practice_graph to the screen."""
    nx.draw(practice_graph)
    plt.show()

# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
#draw_practice_graph()


###
### Problem 1b
###

rj=nx.Graph()

#nodes
rj.add_node("Nurse")
rj.add_node("Juliet")
rj.add_node("Tybalt")
rj.add_node("Capulet")
rj.add_node("Friar Laurence")
rj.add_node("Romeo")
rj.add_node("Benvolio")
rj.add_node("Montague")
rj.add_node("Mercutio")
rj.add_node("Escalus")
rj.add_node("Paris")

#edges
rj.add_edge("Nurse","Juliet")
rj.add_edge("Juliet","Tybalt")
rj.add_edge("Juliet","Capulet")
rj.add_edge("Juliet","Friar Laurence")
rj.add_edge("Juliet","Romeo")
rj.add_edge("Tybalt", "Capulet")
rj.add_edge("Romeo","Friar Laurence")
rj.add_edge("Romeo","Benvolio")
rj.add_edge("Romeo","Montague")
rj.add_edge("Romeo","Mercutio")
rj.add_edge("Benvolio","Montague")
rj.add_edge("Montague", "Escalus")
rj.add_edge("Mercutio", "Escalus")
rj.add_edge("Escalus", "Paris")
rj.add_edge("Paris", "Mercutio")
rj.add_edge("Capulet","Escalus")
rj.add_edge("Capulet", "Paris")

assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

def draw_rj():
    """Draw the rj graph to the screen and to a file."""
    nx.draw(rj)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
#draw_rj()


###
### Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    The parameter 'user' is the string name of a person in the graph.
    """
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given graph.
    The result does not include the given user nor any of that user's friends.
    """
    the_friends=friends(graph, user)
    friends_of_friends=set()
    for i in the_friends:
        friends_of_friends=friends_of_friends.union(friends(graph, i))
    
    #removes the user, and the users friends
    friends_of_friends.difference_update(the_friends)
    if user in friends_of_friends:
        friends_of_friends.remove(user)
   
    return friends_of_friends

assert friends_of_friends(rj, "Mercutio") == set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common."""
    
    return friends(graph, user1).intersection(friends(graph, user2))

assert common_friends(practice_graph,"A", "B") == set(['C'])
assert common_friends(practice_graph,"A", "D") == set(['B', 'C'])
assert common_friends(practice_graph,"A", "E") == set([])
assert common_friends(practice_graph,"A", "F") == set(['C'])

assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map from each user U to the number of friends U has in common with the given user.
    The map keys are the users who have at least one friend in common with the
    given user, and are neither the given user nor one of the given user's friends.
    Take a graph G for example:
        - A and B have two friends in common
        - A and C have one friend in common
        - A and D have one friend in common
        - A and E have no friends in common
        - A is friends with D
    number_of_common_friends_map(G, "A")  =>   { 'B':2, 'C':1 }
    """
    
    common_friends_map={i: None for i in friends_of_friends(graph,user)}
    
    #counts the number of friends in the set from common friends and
    #assigns that number to the friend 
    
    for keys in common_friends_map:
        common_friends_map[keys]=sum(1 for items in common_friends(graph, user, keys))
    
    
    return common_friends_map
    

assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}

assert number_of_common_friends_map(rj, "Mercutio") == { 'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1, 'Juliet': 1, 'Montague': 2 }


def number_map_to_sorted_list(map):
    """Given a map whose values are numbers, return a list of the keys.
    The keys are sorted by the number they map to, from greatest to least.
    When two keys map to the same number, the keys are sorted by their
    natural sort order, from least to greatest."""
    
    newmap=map
    
    #sorts the dictionary by key in ascending order and turns it into a list of tuples
    newmap=sorted(newmap.iteritems(), key=operator.itemgetter(0))
    
    #sorts the list of tuples in descending order by its value
    newmap=sorted(newmap, key=operator.itemgetter(1), reverse=True)
    
    newmap= [i for i,j in newmap]
    
    return newmap
    
    
assert number_map_to_sorted_list({"a":5, "b":2, "c":7, "d":5, "e":5}) == ['c', 'a', 'd', 'e', 'b']


def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names of people in the graph
    who are not yet a friend of the given user.
    The order of the list is determined by the number of common friends.
    """
    
    friend_rec=number_of_common_friends_map(graph,user)
    ordered_rec=number_map_to_sorted_list(friend_rec)
    return ordered_rec


assert recommend_by_number_of_common_friends(practice_graph,"A") == ['D', 'F']

assert recommend_by_number_of_common_friends(rj, "Mercutio") == ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 3
###

def influence_map(graph, user):
    """Returns a map from each user U to the friend influence, with respect to the given user.
    The map only contains users who have at least one friend in common with U,
    and are neither U nor one of U's friends.
    See the assignment for the definition of friend influence.
    """
    common_friends_map={i: None for i in friends_of_friends(graph,user)}
        
    for keys in common_friends_map:
        sums=0.0
        for i in common_friends(graph, user, keys):
            sums=sums+1.0/sum(1 for items in friends(graph, i))
            common_friends_map[keys]=sums
    
    return common_friends_map

assert influence_map(rj, "Mercutio") == { 'Benvolio': 0.2, 'Capulet': 0.5833333333333333, 'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45 }


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names of people in the graph
    who are not yet a friend of the given user.
    The order of the list is determined by the influence measurement.
    """
    friend_rec=influence_map(graph,user)
    ordered_rec=number_map_to_sorted_list(friend_rec)
    return ordered_rec

assert recommend_by_influence(rj, "Mercutio") == ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 4
###

users = ["Nurse","Juliet","Tybalt","Capulet","Friar Laurence","Romeo","Benvolio",
            "Montague","Mercutio","Escalus","Paris"]

unchanged_recommendations=[]
changed_recommendations=[]

for i in users:
    influence=recommend_by_influence(rj, i)
    number=recommend_by_number_of_common_friends(rj, i)
    if influence==number:
        unchanged_recommendations.append(i)
    else:
        changed_recommendations.append(i)
        
unchanged_recommendations.sort()
changed_recommendations.sort()
        
print "Unchanged recommendations: " + str(unchanged_recommendations)
print "Changed recommendations: " + str(changed_recommendations)
print 

###
### Problem 5
###

# (There is no code to write for this problem.)


###
### Problem 6
###

# (There is no code to write for this problem.)


###
### Problem 7
###

def recommendation_averages(graph):
    infl_average=0.0
    common_average=0.0
    infl_count=0.0
    common_count=0.0

    for i in range(100):
        f1=random.choice(graph.nodes())
        f2=random.choice(list(friends(graph, f1)))
        graph.remove_edge(f1, f2)
    
        #influence method
        f2_inf_friends=recommend_by_influence(graph, f2)
        f1_inf_friends=recommend_by_influence(graph, f1)
        f1_rank=0
        for i in f2_inf_friends:
            if f1 not in f2_inf_friends:
                break
            f1_rank= f1_rank+1
            if i==f1:
                break
            
        f2_rank=0
        for i in f1_inf_friends:
            if f2 not in f1_inf_friends:
                break
            f2_rank=f2_rank+1
            if i==f2:
                break
   
        if f1_rank>0 and f2_rank>0:      
            infl_method= float(f1_rank+f2_rank/2.0)
            infl_count= infl_count+1.0
            infl_average= infl_average+infl_method
    
        #friends in common method
        f2_common_friends=recommend_by_number_of_common_friends(graph, f2)
        f1_common_friends=recommend_by_number_of_common_friends(graph, f1)
        f1_rank=0
        for i in f2_common_friends:
            if f1 not in f2_common_friends:
                break
            f1_rank=f1_rank+1
            if i==f1:
                break
    
        f2_rank=0
        for i in f1_common_friends:
            if f2 not in f1_common_friends:
                break
            f2_rank=f2_rank+1
            if i==f2:
                break
    
        if f1_rank>0 and f2_rank>0:
            common_method=float(f1_rank+f2_rank/2.0)
            common_average=common_average+common_method
            common_count=common_count+1.0
        
        graph.add_edge(f1, f2)
    
    infl_average=infl_average/infl_count
    common_average=common_average/common_count

    if common_average<infl_average:
        better="Number of friends in common"
    else:
        better="Influence"
    
    print "Average rank of influence method: " + str(infl_average)
    print "Average rank of number of friends in common method: " +str(common_average)
    print better + " method is better."
    print
    
recommendation_averages(rj)

###
### Problem 8
###

facebook=nx.Graph()

facebookFile=open("facebook-links.txt", "r")
facebookLines=facebookFile.readlines()

for line in facebookLines:
    data=line.split()
    facebook.add_node(int(data[0]))
    facebook.add_node(int(data[1]))
    facebook.add_edge(int(data[0]),int(data[1]))


assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090

print "Facebook nodes: " + str(len(facebook.nodes()))
print "Facebook edges: " + str(len(facebook.edges()))
print

###
### Problem 9
###

nodes = facebook.nodes()
nodes.sort()

common_friends_dict={} #used in problem 11
for i in nodes:
    if i%1000==0:
        allFriends=recommend_by_number_of_common_friends(facebook, i)
        print str(i)+ " " + str(allFriends[:10])
        common_friends_dict[i]= allFriends[:10]
print
       
###
### Problem 10
###

infl_friends_dict={} #used in problem 11
for i in nodes:
    if i%1000==0:
        allFriends=recommend_by_influence(facebook, i)
        print str(i)+ " " + str(allFriends[:10])
        infl_friends_dict[i]=allFriends[:10]
print

###
### Problem 11
###

same=[]
different=[]
for key in common_friends_dict:
    if common_friends_dict[key]==infl_friends_dict[key]:
        same.append(key)
    else:
        different.append(key)

print "Same: " + str(len(same)) + ", " + "Different: " + str(len(different))
print 
        
###
### Problem 12
###

recommendation_averages(facebook)