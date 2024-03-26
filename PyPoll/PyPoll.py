#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv
import pandas as pd
from pathlib import Path


# In[5]:


# Specify the new directory path
new_directory = 'C:\\Users\\chris\\Documents\\EdX_project'

# Change the current working directory
os.chdir(new_directory)

# Print the new current working directory
print("New Current Working Directory:", os.getcwd())


# In[6]:


pypoll_csv = Path("Resources/election_data.csv")

election_df = pd.read_csv(pypoll_csv)
election_df.head()


# In[ ]:


candidate_list = []
percentage_votes = []
total_votes_won = []
popular_vote = []
percentage_votes_won = []

count = 0


# In[ ]:


with open(pypoll_csv) as pypoll_csv_file:
     pypollreader = csv.reader(pypoll_csv_file, delimiter=',')
    
     pybank_poll = next(pypollreader)
    

     for row in pypollreader:
        
        count = count + 1
        
        candidate_list.append(row[2])

    
     for names in set(candidate_list):
         popular_vote.append(names)
         total_votes = candidate_list.count(names)
         total_votes_won.append(total_votes)
         percentage_votes = round((total_votes/count) * 100, 3)
         percentage_votes_won.append(percentage_votes)

         
         winning_vote = max(total_votes_won)
         winner = popular_vote[total_votes_won.index(winning_vote)]
         
        
         print("Election Results")   
         print("-------------------------")
         print("Total Votes: " + str(count))    
         print("-------------------------")


for i in range(len(popular_vote)):
    print(popular_vote[i] + ": " + str(percentage_votes_won[i]) +"% (" + str(total_votes_won[i])+ ")")
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")


# In[ ]:


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

