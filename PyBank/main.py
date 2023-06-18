#importing necessary modules
import os
import csv

#the path to the file
path = os.path.join('Resources','budget_data.csv')

#reading through the CSV file
with open(path, 'r') as csvplik:
    csvreader = csv.reader(csvplik, delimiter=',')
    
    #storing the header row
    header = next(csvreader)

    #skipping the header from the loop
    next(csvreader, None)

    #setting variables: count for total months, total for sum of all profit/losses
    count = 0 
    total = 0
    previous_profit = None

    #list that will store all the dates
    dates = []
    #list that will store changes in Profit/Loss between two consecutif months
    changes=[]  
    
    #Looping through the CSV file
    for row in csvreader:
        count = count + 1
        total = total + int(row[1])
        dates.append(row[0])
        if previous_profit is not None:
            change = int(row[1]) - previous_profit
            changes.append(change)
        previous_profit = int(row[1])
        
    #First results visible on the Terminal
    print("Financial Analysis")
    print("----------------------------")
    print("Total months: " + str(count))        
    print("Total: $" + str(total))
    
    #Calculating Average of changes by setting a definition
    def average(changes):
        length = len(changes)
        sum = 0
        for number in changes:
            sum = sum + number
        return sum / length
    
    #Rounding average to two decimal points
    rounded_average = round((average(changes)),2)
    print("Average Change: $" + str(rounded_average))

    #Creating a list of changes that will have the same number of elements as dates' list
    zero_change_row1 = [0]     
    combined_changes = zero_change_row1 + changes

    #Zipping dates and changes into tuples and then transforming it into a dictionary    
    changes_dictionary = dict(zip(dates, combined_changes))
    
    #Finding Maximum(/Minimum) value and Maximum(/Minimum) date from the dictioniary 
    #Finding a key that is associated with the maximum(/minimum) value by using get() method

    max_date = max(changes_dictionary, key=changes_dictionary.get)
    max_value = changes_dictionary[max_date]
    min_date = min(changes_dictionary, key=changes_dictionary.get)
    min_value = changes_dictionary[min_date]
    print("Greatest Increase in Profits: " + max_date + ' ($' + str(max_value) + ')' )
    print("Greatest Decrease in Profits: " + min_date + ' ($' + str(min_value) + ')' )

#Creating a txt file with the results   
output_path = os.path.join('Analysis','budget_data_results.txt')
with open(output_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write("Total months: " + str(count) + "\n")       
    output_file.write("Total: $" + str(total) + "\n") 
    output_file.write("Average Change: $" + str(rounded_average) + "\n") 
    output_file.write("Greatest Increase in Profits: " + max_date + ' ($' + str(max_value) + ')' + "\n")     
    output_file.write("Greatest Decrease in Profits: " + min_date + ' ($' + str(min_value) + ')' + "\n")   
    