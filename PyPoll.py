# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
#path = 'C:\users\Resources\election_results.csv'
#open("rC:\Users\memus\OneDrive\Desktop\Analysis Project\Module 3 - PyPoll with Python\Election_Analysis\Resources\election_results.csv")

file_variable = open("Resources/election_results.csv", "r")

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the ptresent time.
print("The time right now is ", now)

#Import the datetime class from the datetime module.
import datetime as dt
#use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
#Print the present time.
print("The time right now is ", now)

print("import csv")
print(dir(csv))

print(dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson':432438}))
print(dir(str))

#Assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'

#open the election results and read the file.
with open(file_to_load) as election_data:

#To do: perform analysis.
    print(election_data)

#Close the file.
#print("election_data.close()")

import os
dir(os)
print(dir(os))

print(dir(os.path))

# To declare a variable or the file to load = chaining
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the elction rsults and read the file.
with open(file_to_load) as election_data:

    #print the file object.
    print(election_data)

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")

#Write three counties to the file.
    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")
    txt_file.write("Counties in the Election\n--------------\nArapahoe\nDenver\nJefferson")

#Add our dependencies.
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_anaylsis.txt")

#Open the election results and read the fiel.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

#Print each row in the CSV file.
    for row in file_reader:
        #print('headers')
        print('Ballot ID', 'County', 'Candidate')

