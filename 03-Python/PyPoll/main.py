import os
import csv

# Directory path
csvpath = os.path.join('Resources', 'election_data.csv')

# Read CSV file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    rows = csv.reader(csvfile, delimiter=',')

    # Skip row with headers
    next(rows)

    total_votes =0
    countnames = {}
    for row in rows:
        total_votes += 1
        name = row[2]
        if name in countnames:
            countnames[name] += 1
        else:
            countnames[name] = 1
    winner_name = ''
    max_votes = 0
    for key, value in countnames.items():
        if value > max_votes:
            max_votes = value
            winner_name = key

    # Print data
    with open("output.txt", "a") as f:
        print('Election Results', file=f)
        print('-----------------------------', file=f)
        print('Total Votes: ' + str(total_votes), file=f)
        print('-----------------------------', file=f)

        for k in countnames:
            pctcount = float(countnames[k]) / float(total_votes) * 100
            print(str(k)+": " + "{0:0.3f}".format(pctcount) + "%" + " (" + str(countnames[k]) + ")", file=f)
        print('-----------------------------', file=f) 
        print('Winner: ' + str(winner_name), file=f) 
        print('-----------------------------', file=f) 