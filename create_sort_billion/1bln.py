import csv
import numpy as np
import os



f = open('/home/arman/Documents/Arman/Data Science - Code Republic/Computer Science/1bln_sort/csv_file', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
for i in range(200):
    writer.writerow(np.random.randint(low = 1,high=120,size=5000000))

# close the file
f.close()


# I created file with 1 bln integers from 1 to 120. The runtime process lasted 10 minutes.

file_size = os.path.getsize('/home/arman/Documents/Arman/Data Science - Code Republic/Computer Science/1bln_sort/csv_file')

print("File Size is :", file_size, "bytes")


















