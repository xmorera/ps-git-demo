import os
from os.path import exists 

print(os.getcwd())

the_file = "file.txt"

if exists(the_file):
    print(the_file + " exists")
else: 
    print(the_file + " does not exist")

# Creates a file, mode is set to create
file = open(the_file, "x")

# Try to create an already existing file with mode x
try:
    second_file = open(the_file, "x")
except:
    print("You cannot create a file that already exists")

# Open for writing an existing file
third_file = open(the_file, "w", encoding="utf-8")

print()


