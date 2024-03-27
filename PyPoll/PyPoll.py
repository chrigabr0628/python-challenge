#PLEASE NOTE: I recieved code source from AskBCS, Xpert Learning Assitant, and tutors.

#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup

import os
import csv
import pandas as pd
from pathlib import Path


# In[2]:


# Specify the new directory path
new_directory = 'C:\\Users\\chris\\Documents\\EdX_project'

# Change the current working directory
os.chdir(new_directory)

# Print the new current working directory
print("New Current Working Directory:", os.getcwd())


# In[3]:


# File to Load 

pypoll_csv = Path("Resources/election_data.csv")

# Read Data File and store into Pandas DataFrames

election_df = pd.read_csv(pypoll_csv)
election_df.head()


# In[4]:


# Create lists to store data

candidate_list = []
percentage_votes = []
total_votes_won = []
popular_vote = []
percentage_votes_won = []

# Create variable to output values

count = 0


# In[5]:


# Open the CSV using file path

with open(pypoll_csv) as pypoll_csv_file:
     pypollreader = csv.reader(pypoll_csv_file, delimiter=',')
    
     pybank_poll = next(pypollreader)
    
# Iterate through the rows
    
     for row in pypollreader:
        
        count = count + 1
        
        candidate_list.append(row[2])

# Calculations to output values
    
for names in set(candidate_list):
    popular_vote.append(names)
    total_votes = candidate_list.count(names)
    total_votes_won.append(total_votes)
    percentage_votes = round((total_votes/count) * 100, 3)
    percentage_votes_won.append(percentage_votes)

         
    winning_vote = max(total_votes_won)
    winner = popular_vote[total_votes_won.index(winning_vote)]

# Print the results
        
print("Election Results")   
print("-------------------------")
print("Total Votes: " + str(count))    
print("-------------------------")


for i in range(len(popular_vote)):
    print(popular_vote[i] + ": " + str(percentage_votes_won[i]) +"% (" + str(total_votes_won[i])+ ")")
    print("-------------------------")
print("Winner: " + winner)
print("-------------------------")


# In[6]:


# Export text file

with open('election_analysis.txt', 'w') as text:
    text.write("Election Results" + "\n")   
    text.write("-------------------------\n")
    text.write("Total Votes: " + str(count) + "\n")    
    text.write("-------------------------\n")
    for i in range(len(popular_vote)):
     text.write(popular_vote[i] + ": " + str(percentage_votes_won[i]) +"% (" + str(total_votes_won[i])+ ")\n")
     text.write("-------------------------\n")
     text.write("Winner: " + winner + "\n")
     text.write("-------------------------\n")

