import numpy as np


# Import a list using np.array
sample_array = np.array([0,0,7])
print(type(sample_array))
print("Size: %d" % sample_array.size)
print("Shape: %d" % sample_array.shape)
print(sample_array, "\n")

nested_array = np.array( [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(nested_array))
print("Size: %d" % nested_array.size)
print("Shape: %s" % str(nested_array.shape))
print(nested_array, "\n")

# Creates a 2D array filled with zeros
all_zeroes = np.zeros((2, 3))   
print(all_zeroes, "\n")

# Creates a 2D array filled with ones
all_ones = np.ones((3, 2))    
print(all_ones, "\n")

# Creates a 2D array with uninitialized values
unitialized = np.empty((2, 2)) 
print(unitialized, "\n")  

# Flatten an array
print(nested_array)
print(nested_array.flatten(), "\n")

# Creates a 1D array with values from 0 to 9
range_values = np.arange(10)  
print(range_values, "\n") 

# Creates a 1D array with values from 1 to 10
ranged_values_two = np.arange(1, 11)  
print(ranged_values_two, "\n")

# Creates a 1D array with values from 0 to 1 in increments of 0.1
arranged_increment = np.arange(0, 1, 0.1)
print(arranged_increment, "\n") 

# Import a NumPy text file
badges_saved_np = np.loadtxt('files/badges-five-numpy.txt')
print(badges_saved_np, "\n")

# Import a comma separated file
# It is required to specify delimiter, else an exception is raised
try:
    badges_comma = np.loadtxt('files/badges-five.txt') # error
except Exception as e:
    print(str(e))

badges_comma = np.loadtxt('files/badges-five.txt', delimiter=',')
print(badges_comma, "\n")

# Import a comma separated file that has a header row
# Error occurs, unless I skip the header row
try:
    badges_header = np.loadtxt('files/badges-five-header.txt', delimiter=',')
except Exception as e:
    print(str(e))

badges_header = np.loadtxt('files/badges-five-header.txt', delimiter=',', skiprows=1) 
print(badges_header, "\n")

# Import a comma separated file with header row and convert values to string (Hint: view Locals)
badges_str = np.loadtxt('files/badges-five-header.txt', delimiter=',', skiprows=1, dtype=str)

### 'usecols' specifies which columns should be loaded (Hint: view Locals)
badges_str = np.loadtxt('files/badges-five-header.txt', delimiter=',', usecols=(0, 2), dtype=str) 

# Import and apply a function to one of the values
def Increase(the_id):
    return int(the_id) + 1000

badges_increased = np.loadtxt('files/badges-five.txt', delimiter=',', dtype=int, converters={1: Increase})
print(badges_increased, "\n")

# Import with a missing value, but still with loadtxt which raises an error
try:
    badges_missing_value = np.loadtxt('files/badges-five-missing-value.txt', delimiter=',', skiprows=1)
except Exception as e:
    print(str(e))

# Import with a missing value using genfromtxt
badges_missing_value = np.genfromtxt('files/badges-five-missing-value.txt', delimiter=',')
print(badges_missing_value, "\n")

# We need to skip the header 
badges_missing_value = np.genfromtxt('files/badges-five-missing-value.txt', delimiter=',', skip_header=1)
print(badges_missing_value, "\n")

# And you can specify what to do with missing values, i.e. fill with another value
badges_missing_value = np.genfromtxt('files/badges-five-missing-value.txt', delimiter=',', skip_header=1, filling_values=0)
print(badges_missing_value, "\n")

### Read CSV file using recfromcsv 
people = np.recfromcsv('files/people.csv', delimiter=',')
# Access column values using column names
print(people['name'])
print(people['email'])
print()