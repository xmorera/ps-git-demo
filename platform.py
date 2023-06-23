import os
import shutil
from pathlib import Path

# Get current working directory
current_dir = os.getcwd()
print(current_dir)

# os contains path-specific functionality
# Can get an absolute path from a relative one
print(os.path.abspath('./..'))
# Backslashes require escaping
print(os.path.abspath('.\\..'))

# List contents of current directory
files_in_dir = os.listdir(current_dir)
print(files_in_dir)

# Create a new directory (can create multiple with mkdirs)
os.mkdir("pluralsight")

# Copy files using shutil
shutil.copytree("./code", "./pluralsight/code")
# Can rename with shutil.move or os.rename
shutil.move("./pluralsight/code", "./pluralsight/my_code")

# Change directory and confirm change
os.chdir("pluralsight")
current_dir = os.getcwd()
print(current_dir)
print(os.listdir("./my_code"))