from pprint import pprint
import os

print("- os.listdir")
if(os.name == 'nt'):
  # Windows 
  pprint(os.listdir("E:\\github\\xmorera\\ps-working-files-python\\demos"))
else:    
  # MacOS
  pprint(os.listdir("/Users/xavier/github/xmorera/ps-working-files-python/demos"))

# Print the file path and directory separator for the current OS
print(f"File path: {os.path.abspath('samples/demo_steps.txt')}")
print(f"Directory separator: {os.path.sep}")

# Print the file path and directory separator for Windows
print(f"File path (Windows): {os.path.abspath('samples/demo_steps.txt').replace(os.path.sep, '/')}")
print(f"Directory separator (Windows): {os.path.altsep}")

fileName = "file.txt"
file_path = os.path.join(os.getcwd(), fileName)
print(file_path)

print()