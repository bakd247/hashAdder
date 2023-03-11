import time
import csv

t = time.perf_counter()
for i in range(10,100):
    with open("%s.csv" % i, "w"):
        pass
print("Finished...")
elapsed_time = time.perf_counter()
print(elapsed_time-t)
exit()