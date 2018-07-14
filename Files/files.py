""" Files I/O """


## CSV

import csv
w = csv.writer(file)
w.writerow( (tuple, of, values) )


file = open("filename","w")

# Or

with open(filename, 'r') as f:
    l = f.readline()
