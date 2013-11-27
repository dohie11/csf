# Name: ...
# Evergreen Login: ...
# Programming as a Way of Life
# Homework 5: Election prediction

import csv
import os
import time

def read_csv(path):
    """
    Reads the CSV file at path, and returns a list of rows. Each row is a
    dictionary that maps a column name to a value in that column, as a string.
    """
    output = []
    for row in csv.DictReader(open(path)):
        output.append(row)
    return output


################################################################################
# Problem 1: State edges
################################################################################

def row_to_edge(row):
    """
    Given an election result row or poll data row, returns the Democratic edge
    in that state.
    """
    return float(row["Dem"]) - float(row["Rep"])  

def state_edges(election_result_rows):
    """
    Given a list of election result rows, returns state edges.
    The input list does has no duplicate states;
    that is, each state is represented at most once in the input list.
    """
    #TODO: Implement this function
    
dictionary={}
    for i in range(len(election_result_rows)):
        rowDictionary = election_result_rows[i]
        state = rowDictionary['State']
        edge = row_to_edge(rowDictionary)
        tempDictionary = {state : edge}
        dictionary = dict(tempDictionary.items()+dictionary.items())
    return dictionary

################################################################################
# Problem 2: Find the most recent poll row
################################################################################

def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if 
    date1 is after date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of poll data rows, returns the most recent row with the
    specified pollster and state. If no such row exists, returns None.
    """
    #TODO: Implement this function
	if len(stateSet)== 0:
            poll= None
        
  
    length= len(stateSet)-1
    if length==0:
        poll=stateSet[0]
    for i in range(length):
        rowDictionary= stateSet[i]
        date1= rowDictionary['Date']
        rowDictionary2= stateSet[i+1]
        date2= rowDictionary2['Date']
        checkDate= earlier_date(date1, date2)
        if checkDate== True:
           poll=rowDictionary2
        else:
           poll=rowDictionary
           stateSet[i+1]=stateSet[i]
    return poll



################################################################################
# Problem 3: Pollster predictions
################################################################################

def unique_column_values(rows, column_name):
    """
    Given a list of rows and the name of a column (a string), returns a set
    containing all values in that column.
    """
    #TODO: Implement this function
    

def pollster_predictions(poll_rows):
    """
    Given a list of poll data rows, returns pollster predictions.
    """
    #TODO: Implement this function
 # takes a list of dictionaries and creates a dictionary of {column_name: [values]}
    
    dictionary={}
    for i in range(len(rows)):
        rowDictionary=rows[i]
        dictionary.setdefault(column_name, set()).add(rowDictionary[column_name])
    return dictionary[column_name]

def pollster_predictions(poll_rows):
    """
    Given a list of poll data rows, returns pollster predictions.
    """

    # takes a list of dictionaries and creates a list of dictionaries
    # with only the most recent polls
    
    recentSet=[]
    for i in range(len(poll_rows)):
        rowDictionary=poll_rows[i]
        state=rowDictionary["State"]
        pollster=rowDictionary["Pollster"]
        recentDict=most_recent_poll_row(poll_rows, pollster, state)
        recentSet=recentSet + [recentDict]
    
    
    # takes recent set and creates a list of the unique Pollsters
    # in the set
    pollsterDict={}
    pollsterList=list(unique_column_values(recentSet, "Pollster"))
    
    # for every unique pollster it checks to make sure that the dictionary
    # in the list is of that pollster. If it is then the loop takes the
    # edge of that dictionary and compiles a dictionary of state edges.
    # then those state edges are put in a dictionary {Pollster: stateEdges}
    
    for i in range(len(pollsterList)):
        pollster=pollsterList[i]
        stateEdge={}
        for j in range(len(recentSet)):
            rowDictionary=recentSet[j]
            dictPollster=rowDictionary["Pollster"]
            if dictPollster == pollster:
                rowDictionary=[rowDictionary]
                stateEdge=dict(state_edges(rowDictionary).items()+stateEdge.items())
                pollsterDict[pollster]=stateEdge       
    return pollsterDict

            
################################################################################
# Problem 4: Pollster errors
################################################################################

def average_error(state_edges_predicted, state_edges_actual):
    """
    Given predicted state edges and actual state edges, returns
    the average error of the prediction.
    """
    #TODO: Implement this function
    pass

def pollster_errors(pollster_predictions, state_edges_actual):
    """
    Given pollster predictions and actual state edges, retuns pollster errors.
    """
    #TODO: Implement this function
def average_error(state_edges_predicted, state_edges_actual):
    """
    Given predicted state edges and actual state edges, returns
    the average error of the prediction.
    """
    count=0
    error=0
    averageError=0
    
    # takes the dictionary of predicted and the dictionary of edges and
    # checks if they are the same state. If they are the count increments
    # and the error is calculated. After all the states are checked the average
    # error is computed.
    
    for i in state_edges_predicted:
        for j in state_edges_actual:
            if i==j:
                count= count+1
                tempError=abs(state_edges_predicted[i]-state_edges_actual[j])
                error= error+tempError
    if count>0:
        averageError=error/count
    return averageError 
    
def pollster_errors(pollster_predictions, state_edges_actual):
    """
    Given pollster predictions and actual state edges, retuns pollster errors.
    """
    
    # takes two dictionaries and returns the average error by pollster in a dictionary
    errorDict={}
    for i in pollster_predictions:
            errorDict[i]=average_error(pollster_predictions[i], state_edges_actual)
    return errorDict


################################################################################
# Problem 5: Pivot a nested dictionary
################################################################################

def pivot_nested_dict(nested_dict):
    """
    Pivots a nested dictionary, producing a different nested dictionary
    containing the same values.
    The input is a dictionary d1 that maps from keys k1 to dictionaries d2,
    where d2 maps from keys k2 to values v.
    The output is a dictionary d3 that maps from keys k2 to dictionaries d4,
    where d4 maps from keys k1 to values v.
    For example:
      input = { "a" : { "x": 1, "y": 2 },
                "b" : { "x": 3, "z": 4 } }
      output = {'y': {'a': 2},
                'x': {'a': 1, 'b': 3},
                'z': {'b': 4} }
    """
     #TODO: Implement this function
    stateDict={}
    for i in nested_dict:
        dict2=nested_dict[i]
        for j in dict2:
            if j not in stateDict:
                stateDict[j] = {i: dict2[j]}
            else:
                stateDict[j][i] = dict2[j]
    return stateDict


################################################################################
# Problem 6: Average the edges in a single state
################################################################################

def average_error_to_weight(error):
    """
    Given the average error of a pollster, returns that pollster's weight.
    The error must be a positive number.
    """
    return error ** (-2)

# The default average error of a pollster who did no polling in the
# previous election.
DEFAULT_AVERAGE_ERROR = 5.0

def pollster_to_weight(pollster, pollster_errors):
    """"
    Given a pollster and a pollster errors, return the given pollster's weight.
    """
    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):
    """
    Returns the weighted average of a list of items.
    
    Arguments:
    items is a list of numbers.
    weights is a list of numbers, whose sum is nonzero.
    
    Each weight in weights corresponds to the item in items at the same index.
    items and weights must be the same length.
    """
    assert len(items) > 0
    assert len(items) == len(weights)
    #TODO: Implement this function
    pass


def average_edge(pollster_edges, pollster_errors):
    """
    Given pollster edges and pollster errors, returns the average of these edges
    weighted by their respective pollster errors.
    """
    #TODO: Implement this function
DEFAULT_AVERAGE_ERROR = 5.0

def pollster_to_weight(pollster, pollster_errors):
    """"
    Given a pollster and a pollster errors, return the given pollster's weight.
    """
    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):
    """
    Returns the weighted average of a list of items.
    
    Arguments:
    items is a list of numbers.
    weights is a list of numbers, whose sum is nonzero.
    
    Each weight in weights corresponds to the item in items at the same index.
    items and weights must be the same length.
    """
    assert len(items) > 0
    assert len(items) == len(weights)
    
    top=0.0
    botSum=0.0
    for i in range(len(items)):
        topProduct=float(items[i]*weights[i])
        botSum=float(botSum + weights[i])
        top= top + topProduct
    
    weightedAvg= top/botSum
    return weightedAvg       

def average_edge(pollster_edges, pollster_errors):
    """
    Given pollster edges and pollster errors, returns the average of these edges
    weighted by their respective pollster errors.
    """
    weights=[]
    items=[]
    for i in pollster_edges:
        items.append(pollster_edges[i])
        weights.append(pollster_to_weight(i, pollster_errors))
        
    avgEdge=weighted_average(items, weights)
    return avgEdge

    
################################################################################
# Problem 7: Predict the 2012 election
################################################################################

def predict_state_edges(pollster_predictions, pollster_errors):
    """
    Given pollster predictions from a current election and pollster errors from
    a past election, returns the predicted state edges of the current election.
    """
    #TODO: Implement this function
    pass
    

################################################################################
# Electoral College, Main Function, etc.
################################################################################

def electoral_college_outcome(ec_rows, state_edges):
    """
    Given electoral college rows and state edges, returns the outcome of
    the Electoral College, as a map from "Dem" or "Rep" to a number of
    electoral votes won.  If a state has an edge of exactly 0.0, its votes
    are evenly divided between both parties.
    """
    ec_votes = {}               # maps from state to number of electoral votes
    for row in ec_rows:
        ec_votes[row["State"]] = float(row["Electors"])

    outcome = {"Dem": 0, "Rep": 0}
    for state in state_edges:
        votes = ec_votes[state]
        if state_edges[state] > 0:
            outcome["Dem"] += votes
        elif state_edges[state] < 0:
            outcome["Rep"] += votes
        else:
            outcome["Dem"] += votes/2.0
            outcome["Rep"] += votes/2.0
    return outcome


def print_dict(dictionary):
    """
    Given a dictionary, prints its contents in sorted order by key.
    Rounds float values to 8 decimal places.
    """
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if type(value) == float:
            value = round(value, 8)
        print key, value


def main():
    """
    Main function, which is executed when election.py is run as a Python script.
    """
    # Read state edges from the 2008 election
    edges_2008 = state_edges(read_csv("data/2008-results.csv"))
    
    # Read pollster predictions from the 2008 and 2012 election
    polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
    polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))
    
    # Compute pollster errors for the 2008 election
    error_2008 = pollster_errors(polls_2008, edges_2008)
    
    # Predict the 2012 state edges
    prediction_2012 = predict_state_edges(polls_2012, error_2008)
    
    # Obtain the 2012 Electoral College outcome
    ec_2012 = electoral_college_outcome(read_csv("data/2012-electoral-college.csv"),
                                        prediction_2012)
    
    print "Predicted 2012 election results:"
    print_dict(prediction_2012)
    print
    
    print "Predicted 2012 Electoral College outcome:"
    print_dict(ec_2012)
    print    


# If this file, election.py, is run as a Python script (such as by typing
# "python election.py" at the command shell), then run the main() function.
if __name__ == "__main__":
    main()
