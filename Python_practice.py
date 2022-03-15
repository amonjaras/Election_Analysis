#3.2.2 Execute Python files
print("Hello World\n")

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