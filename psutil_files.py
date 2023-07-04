from pprint import pprint
import psutil

print("- Disk partitions")
pprint(psutil.disk_partitions())
print("---\n")

print("- Disk usage")
pprint(psutil.disk_usage('/'))
print("---\n")

print("- Disk IO counters")
pprint(psutil.disk_io_counters(perdisk=False, nowrap=True))
pprint(psutil.disk_io_counters(perdisk=True))
print("---\n")


