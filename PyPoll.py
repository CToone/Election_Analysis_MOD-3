# The data we need to retrieve,
# 1. The total numbe of votes cast
# 2. A complete list of canidates who recieved votes 
# 3. The percentage of votes each canidate won
# 4. The toal number of votes each canidate won
# 5. The winner of the election based on popular vote.



# # Import the datetime class from the datetime module.
# import datetime
# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# # Print the present time.
# print("The time right now is ", now)



import csv

import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data)
        # Print each row in the CSV file.
         # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
        # print(row)

    # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# Use the open statement to open the file as a text file.


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    

    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson") 