# import modules to read the budget data
# assign variable 

import os
import csv
csvpath = os.path.join('PyBank','Resources','budget_data.csv')
TotalMonths = 0
NetProfit = 0
profit = []
months = []
change = []
rowNumber = 0

# read file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    # create two lists of the columns to be able to interate through months and profits 
    # then count months and build net profit total
    for row in csvreader:
        months.append(str(row[0]))
        profit.append(int(row[1]))
        TotalMonths = TotalMonths + 1
        NetProfit = NetProfit + int(row[1])
    
    # create row number as an index for the profit list so that 
    # we can compare rows of profit amounts to hold a change value
    # and then create a list of the change values to zip with the months to make dictionary

    for amount in profit:
        if rowNumber == TotalMonths - 1:
            break
        else:
            firstProfit = int(profit[rowNumber])
            rowNumber = rowNumber + 1
            nextProfit = int(profit[rowNumber])
            dif = int(nextProfit - firstProfit)
            change.append(dif)
    print(TotalMonths)
    print(NetProfit)
    avgChange = round(sum(change)/TotalMonths, 2)
    print(avgChange)

 # month refers to month before or after the change? 
 # my code refers to the month before the change, 
 # but adding an element in the list "change" will increment the zip file 
 # so that the month reflects the month after the change

    changesDict = dict(zip(months, change))
    changemax = max(changesDict,key = changesDict.get)
    print(f'{changemax}: ${changesDict[changemax]}')
    changemin = min(changesDict,key = changesDict.get)
    print(f'{changemin}: ${changesDict[changemin]}')
    


# create file to write to 
output_file = os.path.join('PyBank','Analysis','PyBankOutput.txt')
with open(output_file, 'w') as txt_file:
    txt_file.write(f'Financial Analysis\n------------------\nTotal Months: {TotalMonths}\nNet Profit/Losses: ${NetProfit}\nAverage Change: ${avgChange}\nGreatest Increase in Profits: {changemax}: ${changesDict[changemax]}\nGreatest Decrease in Profits: {changemin}: ${changesDict[changemin]}')


