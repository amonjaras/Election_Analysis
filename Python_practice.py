#3.2.2 Execute Python files
print("Hello World\n")
print("----------------------",'\n')

#3.2.3 Data Types
#integer
print("3 is ", type(3))
print("2019 is ", type(2019),'\n')
ballots=1,341
print("Ballots = ",ballots)
print("Ballots is ", type(ballots),'\n')

#floating-point
print("73.81 is ", type(73.81),'\n')

#strings
print("Hello World is ", type("Hello World"),'\n')

#Boolean
print("True is ", type(True),'\n')

#Creating Variables
num_candidates=3
winning_percentage=73.81
candidate="Diane"
won_election=True

#Variables/Order of precedence
print("5+2*3 =",5+2*3)
print("8//5-3 =",8//5-3)
print("8+22*2-4 =",8+22*2-4)
print("16-3/2+7-1 =",16-3/2+7-1)
print("3**3%5 =",3**3%5)
print("5+9*3/2-4 =",5+9*3/2-4,'\n')

#Grouping with parenthesis
print("(5+2)*3 =",(5+2)*3)
print("(8//5)-3 =",(8//5)-3)
print("8+(22*(2-4)) =",8+(22*(2-4)))
print("16-3/(2+7)-1 =",16-3/(2+7)-1)
print("3**(3%5) =",3**(3%5),'\n')
print("5+(9*3/2-4) =",5+(9*3/2-4), "vs 5+(9*3/(2-4)) =",5+(9*3/(2-4)),'\n')

print("----------------------",'\n')

#3.2.5 Lists
counties=["Arapahoe","Denver","Jefferson"]
print("Participant couties: ",counties,'\n')

#indexing
print("First Item uisng counties[0]:",counties[0])
print("using counties[2]:",counties[2],'\n')

#negative indexing
print("fining the last item with counties[-1]:",counties[-1],'\n')

#lenght of a list
print("total of counties in the list:",len(counties),'\n')

#slice lists
print("finding first and second items",counties[0:2],'\n')

#add items to alist
counties.append("El Paso")
print("Participant counties: ", counties,'\n')

#insert items to a list
counties.insert(2,"El Paso")
print("Countie duplicated while inserting: ",counties,'\n')

#removing items using .remove
counties.remove("El Paso")
print("Countie list after removal: ",counties,'\n')

#removing items using pop()
counties.pop(3)
print("Counties list after pop: ",counties,'\n')

#changing an element in a list
counties[2] = "El Paso"
print("Changing countie list: ",counties,'\n')

#Exercise performed on the original list
#going back to the original
counties[2] = "Jefferson"
print("Originla counties list: ",counties)
#inserting El Paso to second position
counties.insert(1,"El Paso")
print("Countie added on second position: ",counties)
#removing Arapahoe
counties.pop(0)
print("Removing Arapahoe from the list: ",counties)
#Denver on third and keeping Jefferson
counties.append("Denver")
counties.remove("Denver")
print("swapping counties order: ",counties)
#adding Arapahoe
counties.append("Arapahoe")
print("Final counties list for this exersice: ",counties,'\n')

print("----------------------",'\n')

#3.2.6 Tuples: once created can not be changed
counties_tuple = ("Arapahoe","Denver","Jefferson")
print("Counties list using Tuple: ",counties_tuple,'\n')
#lenght of tuple
print("lenght of tuple list: ",len(counties_tuple),'\n')
#Getting items
print("Getting item after 1: ",counties_tuple[1],'\n')
#Getting Arapahoe and Denver
print("Getting items 1 and 2: ",counties_tuple[:2],'\n')

print("----------------------",'\n')

#3.2.7 Dictionaries
#creating a dictionary
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
print(counties_dict,'\n')

#lenght of dictionary
print(len(counties_dict),'\n')

#getting all keys and values
print(counties_dict.items(),'\n')

#getting all keys
print(counties_dict.keys(),'\n')

#getting all values
print(counties_dict.values(),'\n')

#getting specific value
print(counties_dict.get("Denver"),'\n')

#list of dictionaries
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters":432438})
print(voting_data,'\n')
print(len(voting_data),'\n')
voting_data.insert(1,{"county":"El Paso", "registered_voters":461149})
print(voting_data,'\n')
voting_data.pop(0)
print(voting_data,'\n')
voting_data.remove({"county":"Denver", "registered_voters":463353})
print(voting_data,'\n')
voting_data.append({"county":"Denver", "registered_voters":463353})
print(voting_data,'\n')
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
print(voting_data,'\n')

print("----------------------",'\n')

#3.2.8 Decision statements
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
