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

# Open the election results and read the file
with open(csvpath) as election_data:

    # Print the file object
    print(election_data)

# Create a filename variable to a direct or indirect path to the file
txtcreate = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file
open(txtcreate,"w")

# Close the file
election_data.close()

