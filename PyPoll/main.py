# import the csv and os modules
import csv
import os

# load the file
inputFile = os.path.join("election_data.csv")

# file to hold the output of the voting analysis
outputFile = os.path.join("analysis.txt")

# variables
totalVotes = 0 
candidate = [] 
candidateList = []
candidateVotes = {}
winner = ""
winningCount = 0

# read the csv file
with open(inputFile) as electionData:
    # create the csv reader
    csvreader = csv.reader(electionData)

    # read the header
    header = next(csvreader)

    # rows will be lists
        # index 0 is the ballot id
        # index 1 is the county
        # index 2 is the candidate
    
    # for each row
    for row in csvreader:
        # add on to the total votes
        totalVotes += 1 # same as totalVotes = totalVotes + 1
        candidate = row[2]

        # check to see if the candidate is in the list of candidates
        if row[2] not in candidateList:
            candidateList.append(candidate)
            candidateVotes[candidate] = 0

        else:
            # if the candidate is on the list
            # add a vote to the candidate vote count
            candidateVotes[candidate] = candidateVotes[candidate]+1


for candidate in candidateVotes:
    #get the vote count and percentage of the votes
    votes = candidateVotes.get(candidate)
    votePct = (float(votes) / float(totalVotes)) * 100.00
    voteOutput = f"\t{candidate}: {votePct:.2f}% \n"

    print(voteOutput)


    #compare the votes to the winning count
    if votes > winningCount:
        # update the votes to be the new winning count
        winningCount = votes
        # update the winning candidate
        winner = candidate

winnerOutput = f"Winner: {winner}\n-----------------------"

    

# create an output variable to hold the output
output = (
    f"Election Results\n"
    f"-----------------------\n"
    f"Total Votes: {totalVotes:,}\n"
    f"-----------------------\n"
    f"{voteOutput}"
    f"------------------------\n"
    f"{winnerOutput}"
)

# diplay the output to the console / terminal
print(output)

# print the results and export the data to a text file
with open(outputFile, "w") as textFile:
    # write the output to the textfile
    textFile.write(output)
