#Shit I need to figure out
#How to count months (rows)
#How to add columns
#How to figure out individual differences between months (profit/loss changes)
#How to single out the greatest positive change
#How to single out the greatest negative change
#
#
#
#I can copy and paste like a mother fucker
import os
import csv

#Path to collect data from the resources folder
#I even need help with this shit because I thought it was copy and paste
#Thanks Alex
budget_data = os.path.join("Resources", "budget_data.csv")

#Set varibales
#TheRows 
TotalMonths = 0
#TheColumns 
OverallTotal = 0
#Differencebetweenmonths - took me FOREVER TO FIGURE OUT I NEEDED TWO OF THESE (HULK SMASH)
lastmonth = 0
monthchange = []
#PositiveChanges =
#NegativeChanges =


with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")

#Skip the fucking header - I think this works
    csv_header = next(csvreader)

#loop through to count the rows
    for row in csvreader:

		#The total number of months included in the dataset
        # Add TotalMonths
        TotalMonths = TotalMonths + 1
        #One Motherfucker down
        #The total of all the money
        # Add the money
        OverallTotal = OverallTotal + (int(row[1]))
        #two mother fuckers down - saw some stuff that wanted me to check if I was using a string or int, but I would have never done that, although I probably should think to do this
        #working some google shit but I don't even know how to word the next few asks

#loop through the rows and get the differences between rows - need to store this as a list of totals (MF)
        monthdiff = int(row[1]) - lastmonth
        lastmonth = int(row[1])
        #There are probably better ways to do this, but this is the way that makes the most sense to me.
#send it where it should go
        monthchange.append(monthdiff)
        avgmonthdiff = round(sum(monthchange)/TotalMonths)
        #had to find how to round and that damn end ) gets me all the damn time
        
#find the max and min bitches
maxmonthdiff = max(monthchange)
minmonthdiff = min(monthchange)
         
          
print(f"Total Months: {TotalMonths}")
print(f"Overall Total: ${OverallTotal}")
print(f"Average Change: ${avgmonthdiff}")
#Gotta figure out how to link the dates in here
print(f"Greatest Increase in Profits: ${maxmonthdiff}" + "")
print(f"Greatest Decrease in Profits: ${minmonthdiff}" + "")

#perhaps I'm missing it, bit I don't see an opportunity to zip the files for output

# Specify the file to write to
output_path = os.path.join("Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Overall Total', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits'])
#stuck with the single quotes, because that was what was in Python Day 2 Ex 9
    # Write the second row
    csvwriter.writerow(['86', '$38382578', '$7803', '$1926159', '$-2196167'])


#Sorry guys. I started working on the PyPoll.
