import os
import csv
from pathlib import Path

filepath = Path('PyPoll/Resources/election_data.csv')


# Opening the CSV
with open(filepath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    candidate_list = [candidate[2] for candidate in csvreader]
    
# Calculating the number of total votes
total_votes = len(candidate_list)

canditates_info = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

# Sorting the list 
canditates_info = sorted(canditates_info, key=lambda x: x[1], reverse=True)

# Printing the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in canditates_info:
    percent_votes = (candidate[1] / total_votes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print("-------------------------")
print(f"Winner: {canditates_info[0][0]}")
print("-------------------------")


#  Printing the  election results to text file 

filepath = os.path.join('PyPoll/Analysis/PyPoll_Results.txt')

with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)

    for candidate in canditates_info:
        percent_votes = (candidate[1] / total_votes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {canditates_info[0][0]}", file=text_file)
    print("-------------------------", file=text_file)