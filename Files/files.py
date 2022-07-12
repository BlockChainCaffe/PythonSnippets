""" Files I/O """

## Regular file
file = open("filename","w")

# Or
with open(filename, 'r') as f:
    l = f.readline()



## CSV

import csv
w = csv.writer(file)
w.writerow( (tuple, of, values) )

with open(csvfile, 'r') as csvof:
    csvreader = csv.reader(csvof)
    for row in csvreader:
        a = row


## Read JSON file into dictionary

with open('file.json') as json_file:
    dictionary = json.load(json_file)


