from pprint import pprint
import psutil

# List of all running process
psutil.process_iter()

# Iterate over all running process
for process in psutil.process_iter():
    try:
        # Get process name & pid from process object
        processName = process.name()
        processID = process.pid
        print(processName , ' ::: ', processID)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# list(psutil.Process().as_dict().keys())

# Iterate over all running processes
AllProcesses = list()
for process in psutil.process_iter():
   # Get process detail as dictionary and append dict of process detail in list
   AllProcesses.append(process.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']))

pprint(AllProcesses)

print()