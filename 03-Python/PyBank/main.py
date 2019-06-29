import os
import csv

# Directory path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read CSV file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    data = csv.reader(csvfile, delimiter=',')

    # Skip row with headers
    next(data)

    # Calculate Number of months and Total Profits
    total_months = 0
    total_profits = 0
    previous_profit = None
    profit_list = []
    month_list = []
    for row in data:
        #print(row[1])
        total_months +=1
        total_profits = float(total_profits) + float(row[1])
        current_profit = row[1]
        if previous_profit is not None:
            change_profit = float(current_profit) - float(previous_profit)
            profit_list.append(change_profit)
            month_list.append(row[0])
        previous_profit = current_profit

    # Calculate Average Profits    
    sum_change_profit = sum(profit_list)
    n_change_profit = len(profit_list)
    average_change = sum_change_profit // n_change_profit

    # Greatest Increase in Profits
    max_profit = max(profit_list)
    rMax = profit_list.index(max(profit_list))
    max_month = month_list[rMax]

    # Greatest Decrease in Profits
    min_profit = min(profit_list)
    rMin = profit_list.index(min(profit_list))
    min_month = month_list[rMin]

    # Print data
    with open("output.txt", "a") as f:
        print('Financial Analysis', file=f)
        print('-----------------------------', file=f)
        print('Total Months: ' + str(total_months), file=f)
        print('Total: $' + "{0:0.0f}".format(total_profits), file=f)
        print('Average Change: $' + "{0:0.2f}".format(average_change), file=f)
        print('Greatest Increase in Profits: ' + str(max_month) + ' ' + '($' + "{0:0.0f}".format(max_profit) + ')', file=f)
        print('Greatest Decrease in Profits: ' + str(min_month) + ' ' + '($' + "{0:0.0f}".format(min_profit) + ')', file=f)


