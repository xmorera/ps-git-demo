import csv
from pprint import pprint


# File used in this demo.
the_file = 'files/people.csv'

# Open file and read
with open(the_file, newline='') as csvfile:
    person = csv.reader(csvfile, delimiter=',', quotechar='"')
    # Skip header row
    next(person)
    # pprint the records
    for row in person:
        pprint(row)

print()