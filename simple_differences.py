from pprint import pprint
import os

print("- os.listdir")
if(os.name == 'nt'):
  # Windows 
  pprint(os.listdir("E:\\github\\xmorera\\ps-working-files-python\\demos"))
else:    
  # MacOS
  pprint(os.listdir("/Users/xavier/github/xmorera/ps-working-files-python/demos"))
