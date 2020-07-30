import csv
import os 

#Assign a variable to load a file from a path
file_to_load = os.path.join("resources","election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#initialize total votes counter
total_votes = 0

#create a list of all possible candidates 
candidate_options = []

#Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    print(headers)
   
    # Print each row in the CSV file
    for row in file_reader:
        
        #Add to the total vote count
        total_votes += 1
        
        #Grab the candidates name from the row
        candidate_name = row[2]

        #If the candidate is not already added to the list
        if candidate_name not in candidate_options:

            #Add the candidates name to the list
            candidate_options.append(candidate_name)


print(total_votes)

print(candidate_options)





