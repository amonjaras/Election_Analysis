# The data we need to retreive
# 1. The total number of voters cast
# 2. A complete list of candidates who receive votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# -----------------------

# Modules
import os
import csv

# Assign a variable for the file to load and the path
csvpath = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
txtcreate = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(csvpath) as election_data:

    #To do: read and analyze the date here

    # Read the file object with the reader function
    csvreader = csv.reader(election_data)

    # Print the header row
    headers = next(csvreader)
    print(headers)

    #Print each row in the csv file
    #for row in csvreader:
        #print(row)

    # Print the file object
    #print(election_data)


"""
# Using the open() function to open the file as a text file
outfile = open(txtcreate,"w")

# write some data to the file
#outfile.write("Hello World")

# write three countries to the file
#outfile.write("Arapahoe \nDenver\nJefferson")

# skill Drill
outfile.write("Counties in the election \n-----------------------\nArapahoe\nDenver\nJefferson")


# Close the file
outfile.close()

"""