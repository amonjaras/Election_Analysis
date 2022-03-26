# **ELECTION AUDIT ANALYSIS**

## **INDEX**

[1. Overview of the Election Audit](#1-overview-of-election-audit)

[2. Resources](#2-Resources)

[3. Election Audit Results](#3-election-audit-results)

[4. Summary](#4-Summary)



## **1. Overview of Election Audit**
The Audit performed for the Colorado Board of Elections was successful. For this Project, the election commission requested to add additional data to complete the Audit.


1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## **2. Resources**

- Data Source: [Election Results](https://github.com/amonjaras/Election_Analysis/blob/main/Resources/election_results.csv)

- Software: Python 3.9.7, Visual Studion Code 1.65.2

```
(169)  f'* User current version: {sys_version}  *\n'

```

## **3. Election Audit Results**
The Election results show the following:

- There were **369,711** votes cast in the election.
- The counties were:

| County |
| :---: |
| Jefferson |
| Denver |
| Arapahoe |

- The county results were:

| County | Percentage | Total Votes|
| :---: | :---: | :---: |
| Jefferson | 10.5% | 38,855 |
| Denver | **82.8%** | **306,055** |
| Arapahoe | 6.7% | 24,801 |

- The county with largest number of votes was:

| Largest County Turnout |
| :---: |
| **Denver** |

- The candidates were:

| Candidate name |
| :---: |
| Charles Casper Stockman |
| Diana DeGette |
| Raymon Anthony Doane |

- The candidate results were:

| Candidate name | Percentage | Total of votes |
| :---: | :---: | :---: |
| Charles Casper Stockman | 23.0% | 85,213 |
| Diana DeGette | **73.8%** | **272,892** |
| Raymon Anthony Doane | 3.1% | 11,606 |

- The winner of the election was:
 - Candidate (**Diana DeGette**), who received "**73.8%**" of the vote and "**272,892**" number of votes.

- Printed results can be found in [Election Analysis](https://github.com/amonjaras/Election_Analysis/blob/main/analysis/election_analysis.txt)

### 3.1 Code used to determine the votes per county

<details><summary><b>The code used to obtain the information is as follows:</b></summary>
<p>

```
(27)    # 1: Create a county list and county votes dictionary.
        county_options = []
        county_votes = {}

(36)    # 2: Track the largest county and county voter turnout.
        winning_vote_county = ""
        winning_vote_count = 0
        winning_vote_percentage = 0

(57)    # 3: Extract the county name from each row.
        county_name = row[1]

(73)        # 4a: Write an if statement that checks that the
                # county does not match any existing county in the county list.
                if county_name not in county_options:

                    # 4b: Add the existing county to the list of counties.
                    county_options.append(county_name)

                    # 4c: Begin tracking the county's vote count.
                    county_votes[county_name] = 0

                # 5: Add a vote to that county's vote count.
                county_votes[county_name] += 1

(101)                # 6a: Write a for loop to get the county from the county dictionary.
                    for county_name in county_votes:
                        # 6b: Retrieve the county vote count.
                        cvotes = county_votes.get(county_name)
                        # 6c: Calculate the percentage of votes for the county.
                        county_vote_percentage = float(cvotes) / float(total_votes) * 100

                         # 6d: Print the county results to the terminal.
                        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({cvotes:,})\n")
                        print(county_results)

                         # 6e: Save the county votes to a text file.
                        txt_file.write(county_results)
                         # 6f: Write an if statement to determine the winning county and get its vote count.
                        if (cvotes > winning_vote_count) and (county_vote_percentage > winning_vote_percentage):
                            winning_vote_count = cvotes
                            winning_vote_county = county_name
                            winning_vote_percentage = county_vote_percentage

                    # 7: Print the county with the largest turnout to the terminal.
                    winning_county_summary = (
                        f"-------------------------\n"
                        f"Largest County Turnout: {winning_vote_county}\n"
                        f"-------------------------\n")
                    print(winning_county_summary)

                    # 8: Save the county with the largest turnout to a text file.
                    txt_file.write(winning_county_summary)
```
</p>
</details>

## **4. Summary**

This code has been implemented for Local Elections, and can be implemented for Presidential Elections, by including all the States inside the Country.

Taking into account that the information could be stored in separate Data Source, we will be able to modify our code to read the different sources and  return as an Output a Summary and Detailed Analysis of votes cast.

Example code:

```
# Creating a list and dictionary per State
state_options = []
state_votes = {}

# State with majority of votes
win_vote_state = ""
win_vote_count_state = 0
win_vote_percent_state = 0

```


This work belongs to [^1].
Course [^2].
[^note]:
[^1]: Author: Audrey MONJARAS :mexico: :canada:
[^2]: Data Analytics: Unit 3 Python :snake:
