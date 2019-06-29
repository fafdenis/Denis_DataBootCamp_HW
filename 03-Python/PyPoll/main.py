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


    # Print data
    with open("output.txt", "a") as f:
        print('Election Results', file=f)
        print('-----------------------------', file=f)
        print('Total Votes: ' + str(total_votes), file=f)
        print('-----------------------------', file=f)

        pct_list = []
        candidate_list = []
        for k in countnames:
            pctcount = float(countnames[k]) / float(total_votes) * 100
            pct_list.append(pctcount)
            candidate_list.append(k)

        max_pct = max(pct_list)
        rMax = pct_list.index(max(pct_list))
        winner = candidate_list[rMax]

        for k in countnames:
            pctcount = float(countnames[k]) / float(total_votes) * 100
            print(str(k)+": " + "{0:0.3f}".format(pctcount) + "%" + " (" + str(countnames[k]) + ")", file=f)
        print('-----------------------------', file=f) 
        print('Winner: ' + str(winner), file=f) 
        print('-----------------------------', file=f) 