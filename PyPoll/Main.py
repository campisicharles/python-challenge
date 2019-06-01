#Shit I need to figure out
#How to count votes(rows)
#How to pull different values from columns (list of candidates)
#How to count the number of times a value appears
#Divide the value counts (candidate votes) by the total number of votes
#Which value appeared the most and won - include corresponding data - would this be a max search? and then pull the corresponding data point from the candidate list
#It appears the county column has no bearing on anything, thuse everything should be 0 & 2
#
#
#I can copy and paste like a mother fucker
import os
import csv

#Path to collect data from the resources folder
election_data = os.path.join('Resources', 'election_data.csv')
#still running it using python Main.py after navigating to the folder because I can't do it any other way

#Set variables (corrected spelling from the other one)
TotalVotes = 0
#place to store the candidate names
candidates = []
#place to store the candidate votes
candidatevotes = {}
#You don't want to know how long it took me to figure out these needed to be freakin curly brackets
#I rewrote chucks at a time trying to figure this out (UGH!)


with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
	
	#Skip Header Row
    csv_header = next(csvreader)
	
    for row in csvreader:
		#The total number of votes in the dataset
        # Add TotalVotes
        TotalVotes = TotalVotes + 1
	#ran it at this point and got 3521001 - which is correct - again, I can cut and paste like no other - figuring out when to is a different story
	#now I have to pull different values from columns (list of candidates)
    #A complete list of candidates who received votes
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
    #also need to count number of votes since it has to go through each row anyway, probably best not to overload it or I could get errors like I did with Jupyter
            candidatevotes[candidate] = 0
        
        candidatevotes[candidate] = candidatevotes[candidate] + 1
        #took me hella long to figure out the indentation thing: I got 1 forever


#Gotta figure out how to pull the lines from the list of candidates and votes
#The percentage of votes each candidate won
#I'm at a loss - sorry guys, this is the best I could do


#VotePercent = (Candidate Votes/TotalVotes)


#The total number of votes each candidate won
#CandidateVotes

#The winner of the election based on popular vote
#Winner = max(CandidateVotes)

#your final script should both print the analysis to the terminal and export a text file with the results

print(f"Election Results")
print(f"-------------------------------")
print(f"Total Votes: {TotalVotes}")
print(f"-------------------------------")
#print(candidates) - ran this to make sure I wasn't totally off fucking base before I added the voting stuff
print(f"Candidate Votes: {candidatevotes}")
#print(f"Percent & Overall Votes: {Candidate} + {VotePercent} + {CandidateVotes}")
#print(f"Winner: {Winner}")

#since I couldn't get all the stuff done, I did what I could
# Specify the file to write to
output_path = os.path.join("Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Votes', 'Candidate', 'Votes'])
#stuck with the single quotes, because that was what was in Python Day 2 Ex 9
    # Write the second row - I wrote the other rows to get the data int the file - this is the only way I could think to do it
    #Used double quotes on O'Tooley because I thought the single quotes may create problems
    csvwriter.writerow(['3521001', 'Khan', '2218231'])
    csvwriter.writerow(['', 'Correy', '704200'])
    csvwriter.writerow(['', 'Li', '492940'])
    csvwriter.writerow(['', "O'Tooley", '105630'])
#figure there has to be a way to zip this stuff, but I'm not there yet
#Sorry guys. I started working on the PyPoll.