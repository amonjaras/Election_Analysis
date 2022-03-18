"""
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
"""
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
#my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.",'\n')

#using if
counties=["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1],'\n')
"""
if counties[3] != 'Jefferson':
    print(counties[2],'\n') #Error because the list index is out of range
"""
"""
#If-Else statements
temperature = int(input("what is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC.",'\n')
else:
    print("Open the windows",'\n')

#Nested If-Else
#what is the score?
score = int(input("What is your test score? "))
#determine the grade
if score >=90:
    print('your grade is an A')
else:
    if score >= 80:
        print('your grade is a B')
    else:
        if score >= 70:
            print('your grade is a C')
        else:
            if score >= 60:
                print('your grade is a D')
            else:
                print('your grade is an F','\n')

#using if-elif-else instead
#What is your score?
score = int(input("what is your test score? "))

#determine the grade
if score >= 90:
    print('your grade is an A','\n')
elif score >= 80:
    print('your grade is a B','\n')
elif score >= 70:
    print('your grade is a C','\n')
elif score >= 60:
    print('your grade is a D','\n')
else:
    print('your grade is an F','\n')

print("----------------------",'\n')
"""

#3.2.9 membership and logical operators
#Membership
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties",'\n')
else:
    print("El Paso is not in the list of counties",'\n')

#Logical operators
#AND
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties",'\n')
else:
    print("Arapahoe or El Paso is not in the list of counties",'\n')
#OR
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties",'\n')
else:
    print("Arapahoe and El Paso are not in the list of counties",'\n')
#NOT
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties",'\n')
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties",'\n')

print("----------------------",'\n')

#3.2.10 Repetition of statements
#While
"""
x=0
while x <= 5:
    print(x,'\n')
    x = x + 1

count = 7
while count < 1:
    print("Hello World",'\n')
"""

#For loops
for county in counties:
    print(county,'\n')

for i in range(len(counties)):
    print(counties[i],'\n')

"""
##Exercise
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
#Exercise A
for i in range(len(counties_tuple)):
    print("Option A: ",counties_tuple[i],'\n')

#Exercise B
#for i in len(counties_tuple):
    #print(counties_tuple[i],'\n') #TypeError: 'int' object is not iterable

#Exercise C
for county in counties_tuple:
    print("Option C: ",county, '\n')

#Exercise D
for county in counties_tuple:
    print("Option D: ",counties,'\n')
"""

#Iterate through a dictionary
for county in counties_dict:
    print(county,'\n')

for county in counties_dict.keys():
    print(county,'\n')

#Getting values of a dictionary
for voters in counties_dict.values():
    print(voters,'\n')
for county in counties_dict:
    print(counties_dict[county],'\n')
for county in counties_dict:
    print(counties_dict.get(county),'\n')

#Getting key-value pairs of a dictionary
for county, voters in counties_dict.items():
    print(county, voters)

#Print each county and registered voter from the counties dictionary
for county, voters in counties_dict.items():
    print(county, "county has ", voters, "registered voters.")

#get each dictionary in a list of dictionaries
for county_dict in voting_data:
    print(county_dict,'\n')

for i in range(len(voting_data)):
    print(voting_data[i]['county'],'\n')

#get the values from a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
print('\n')
#How would you retrieve the number of registered voters from each dictionary?
#Option A
print("Option A")
for county_dict in voting_data:
    print(counties_dict.values())
print('\n')
#Option B
print("Option B")
for county_dict in voting_data:
    for value in county_dict:
        print(value) # esta opcion no es
print('\n')
#Option C
print("Option C")
for county_dict in voting_data:
    print(county_dict['registered_voters']) #Esta es la opcion correcta
print('\n')
#Option D
print("Option D")
for county_dict in voting_data:
    for key in county_dict.items():
        print(value)
print('\n')
#Print the county name for each dictionary
for county_dict in voting_data:
    print(county_dict['county'])
print('\n')

#3.2.11 Printing formats
#this is the ORIGINAL code
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
print('\n')

#using F-strings with strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
print('\n')

#using F-strings with dictionaries
#using concatenation
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
print('\n')