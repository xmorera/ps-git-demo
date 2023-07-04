from pprint import pprint 


# 1. Use open and close functions to work with a file.

# File used in this demo.
the_file = 'files/people.csv'

# Open the file for reading.
file = open(the_file, "r")
 
# 2. Read the entire file. 
all_lines = file.read()
# Print out the resulting string that contains the entire file.
print(all_lines)

# Do it again. 
# When the entire file has been read, an empty string is returned.
all_lines = file.read()
print(all_lines)

# Use seek() to move the file's current position
file.seek(0)

# 3. Read one line and print it (header)
line = file.readline()
print("Header: " + line)

# And again (record 1)
line = file.readline()
print("Record 1: " + line)

# And one more time (record 2)
line = file.readline()
print("Record 2: " + line)

# And again (record 3)
line = file.readline()
print("Record 3: " + line)

# And there are no more records
line = file.readline()
print("No more records: " + line)

# Let's seek back to the start of the file
file.seek(0)

# 4. And read the file using readlines
lines_array = file.readlines()

# Print line 2
print("Line 2: " + lines_array[2])

# Pretty-print the array
pprint(lines_array)

# Seek to start
file.seek(0)

# 5. Iterate over the file
for each_line in file:
    print(each_line)


# Always close the file, or else bad things may happen
file.close()
print()
