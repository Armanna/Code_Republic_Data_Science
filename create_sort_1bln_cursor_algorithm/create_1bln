import csv
import numpy as np
import os
import sys

f = open('/home/arman/Documents/Arman/Data Science - Code Republic/Computer Science/create_sort_4_billion/create', 'w')

# create the csv writer
writer = csv.writer(f)

min = -500
max = 500


row_size = sys.getsizeof(np.random.randint(low = min,high=max,size=5000000))
print("Single row Size is :", row_size/1000000, "MB")


# write a row to the csv file
for i in range(200):
    writer.writerow(np.random.randint(low = min,high=max,size=5000000))

# close the file
f.close()




# I created file with 1 bln integers from [-500;500]. The runtime process lasted 10 minutes.

file_size = os.path.getsize('/home/arman/Documents/Arman/Data Science - Code Republic/Computer Science/create_sort_4_billion/create')

print("File Size is :", file_size/1000000000, "GB")
