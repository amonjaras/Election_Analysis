#!/usr/bin/env python
# Modules
import os, sys
import requests
import csv

print(sys.version)

__author__      = "Audrey Monjaras"
__credits__     = "Audrey Monjaras"
__version__     = "1.0.0"
__status__      = "Development"

# Assign a variable for the file to load and the path
csvpath = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
txtcreate = os.path.join("analysis", "election_analysis_practice.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options and Candidate Votes
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(csvpath) as election_data:

    # Read the file object with the reader function
    csvreader = csv.reader(election_data)

    # Read the header row
    headers = next(csvreader)
    
    # Print each row in the CSV file
    for row in csvreader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name for each row
        candidate_name = row[2]
              
        # Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add votes to each candidate
        candidate_votes[candidate_name] += 1

# Saving the results to a text file
with open(txtcreate, "w") as txt_file:

    # Print final count to terminal
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n"    )
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Percentage of votes for each candidate by looping though the counts
    # Iterate thorugh the candidate list
    for candidate_name in candidate_votes:
        # Retreive vote count of candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to the text file
        txt_file.write(candidate_results)

        # Determining wining vote
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true set the following
            winning_count = votes
            winning_percentage = vote_percentage
            # winning_candidate equal to candidate's name
            winning_candidate = candidate_name

    # Winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate results to txt file
    txt_file.write(winning_candidate_summary)
