#importing necessary modules
import os
import csv

#the path to the file
path = os.path.join('Resources','election_data.csv')

#reading through the CSV file
with open(path, 'r') as csvplik:
    csvreader = csv.reader(csvplik, delimiter=',')
    
    #skipping the header from the loop
    next(csvreader, None)

    #Setting variables: votes_number for total amount of votes, names_list - to see all the names, 
    #raymon_counts for total votes amount for Raymon etc.
    votes_number = 0
    names_list = []
    raymon_counts = 0
    charles_counts = 0 
    diana_counts = 0
          
    #Going through the loop: finding unique names, counting total votes, total votes for Raymon, Charles and Diana
    for row in csvreader:
        if row[2] not in names_list:
            names_list.append(row[2])    
        votes_number = votes_number + 1
        if row[2] == "Raymon Anthony Doane":
            raymon_counts = raymon_counts + 1
        elif row[2] == "Charles Casper Stockham":
            charles_counts = charles_counts + 1
        elif row[2] == "Diana DeGette":
            diana_counts = diana_counts + 1

    #Calculating the percentage of a person's votes from the totals
    raymon_percentage = raymon_counts / votes_number * 100
    charles_percentage = charles_counts / votes_number * 100
    diana_percentage = diana_counts / votes_number * 100

    print(names_list)

    
    print("Election Results")
    print("-------------------------")
    print("Total votes: " + str(votes_number))
    print("-------------------------")       
    print(names_list[0] + ": " + f"{charles_percentage: .3f}%" + ' (' + str(charles_counts) + ')' )
    print(names_list[1] + ": " + f"{diana_percentage: .3f}%" + ' (' + str(diana_counts) + ')' )
    print(names_list[2] + ": " + f"{raymon_percentage: .3f}%" + ' (' + str(raymon_counts) + ')' )
    print("-------------------------")   
    
    
    #Creating a dictionary with candidates and their counts
    votes = {
    "Raymon Anthony Doane": raymon_counts,
    "Charles Casper Stockham": charles_counts,
    "Diana DeGette": diana_counts
    }

    #Selecting a winner based on the biggest amount of votes
    winner = max(votes, key=votes.get)
    print("Winner: " + winner)
    print("-------------------------") 
    
output_path = os.path.join('Analysis','election_data_results.txt')
with open(output_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write("Total votes: " + str(votes_number) + "\n")       
    output_file.write(names_list[0] + ": " + f"{charles_percentage: .3f}%" + ' (' + str(charles_counts) + ')' + "\n") 
    output_file.write(names_list[1] + ": " + f"{diana_percentage: .3f}%" + ' (' + str(diana_counts) + ')' + "\n")
    output_file.write(names_list[2] + ": " + f"{raymon_percentage: .3f}%" + ' (' + str(raymon_counts) + ')' + "\n")
    output_file.write("-------------------------" + "\n") 
    output_file.write("Winner: " + winner + "\n")
    output_file.write("-------------------------" + "\n")
 
    

