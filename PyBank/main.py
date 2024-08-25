# import modules
import csv
import os

# source to read budget_data file
fileLoad = os.path.join("budget_data.csv")

# file to hold the output of the budget analysis
outputFile = os.path.join("analysis.txt")

# variables
totalMonths = 0         # initialize the total months to 0
totalProfitLosses = 0   # inititalize the total profit/losses to 0
averageChanges = []     # initialize the list of average changes
months = []             # initialize the list of months
# read the csv file
with open(fileLoad) as budget_data:
    # create csv reader object
    csvreader = csv.reader(budget_data)

    # read the header row
    header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)
    
    # increment the count of the total months
    totalMonths += 1 # same as totalMonths = totalMonths + 1

    # add on to the total amount of profit/losses
        # profit/losses is in index 1
    totalProfitLosses += float(firstRow[1])

    #establish the previous revenue
        #revenue is in index 1
    previousRevenue = float(firstRow[1])

    for row in csvreader:
        # increment the count of the total months
        totalMonths += 1 # same as totalMonths = totalMonths + 1

        # add on to the total amount of profit/losses
            # profit/losses is in index 1
        totalProfitLosses += float(row[1])

        # calculate the net change
        netChange = float(row[1]) - previousRevenue
        # add on to the list of monthly changes
        averageChanges.append(netChange)

        # add the first month that a change occurred
            # month is in index 0
        months.append(row[0])

        # update the previous revenue
        previousRevenue = float(row[1])

# calculate the average net change per month
averageChangePerMonth = sum(averageChanges) / len(averageChanges)

greatestIncrease = [months[0],averageChanges[0]]  # holds the month and value of greatest increase
greatestDecrease = [months[0],averageChanges[0]]  # holds the month and value of greatest decrease

# use loop to calculate the index of the greatest and least monthly change
for m in range (len(averageChanges)):
    # calculate the greatest increase and decrease
    if (averageChanges[m] > greatestIncrease[1]):
        greatestIncrease[1] = averageChanges[m]
        greatestIncrease[0] = months[m]

    if (averageChanges[m] < greatestDecrease[1]):
        greatestDecrease[1] = averageChanges[m]
        greatestDecrease[0] = months[m]

# start generating the output
output = (
    f"\nBudget Data Analysis \n"
    f"---------------------------\n"
    f"Total Months = {totalMonths} \n"
    f"Total = ${totalProfitLosses:,.2f}\n"
    f"Average Change = ${averageChangePerMonth:,.2f}\n"
    f"Greatest Increase in Profits = {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f}\n"
    f"Greatest Decrease in Profits = {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f}\n"
    )

# print the output to console / terminal
print(output)

# export the output to the output text file
with open(outputFile, "w") as textFile:
    textFile.write(output)