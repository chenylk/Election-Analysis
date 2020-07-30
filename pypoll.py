#Add out dependencies
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
candidate_votes = {}

#Winning candidate and winning count tracker and winning percentage of votes
winning_candidate = ''
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
   
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
            
            #Add the different candidates to the dictionary as keys with 0 initial value
            candidate_votes[candidate_name] = 0

        #Add votes to the candidates count    
        candidate_votes[candidate_name] += 1

    #Save the results to our text file
    with open(file_to_save, "w") as txt_file:

        #Print the final vote count to the terminal
        
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total votes: {total_votes:,}\n"
            f"--------------------------\n")

        print(election_results, end="")
        #Save the final vote count to the text file
        txt_file.write(election_results)   
        
        for candidate_name in candidate_votes:
            
            #Retrieve vote count and percentages
            votes = candidate_votes[candidate_name]

            percentage_votes = float(votes)/float(total_votes) * 100

            candidate_results = (f'{candidate_name}: {percentage_votes:.1f}% ({votes:,})\n')

            #Print each candidate, their voter count, and percentage to the terminal
            print(candidate_results)

           

            #save the candidate results to our text file 
            txt_file.write(candidate_results)
            
            #Determine if the votes are greater than the winning count
            if (votes > winning_count) and (percentage_votes > winning_percentage):

                #if true then set the variables
                winning_count = votes 
                winning_percentage = percentage_votes
                winning_candidate = candidate_name

        #Print the winning candidates' results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n"
        )

        #save the winning candidate's results to the text file
        txt_file.write(winning_candidate_summary)

        print(winning_candidate_summary)



