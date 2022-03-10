import csv
import numpy as np
from csv import writer
import os


file = open("/home/arman/Documents/Arman/Data Science - Code Republic/Computer Science/1bln_sort/csv_file")
csvreader = csv.reader(file)

d = {}



for row in range(200):
    a = list(next(csvreader))

    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    del a



print(d)
file.close()

with open('/home/arman/Documents/Arman/Data Science - Code Republic/Computer Science/1bln_sort/sorted_file', 'a') as f_object:
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)

    # Pass the list as an argument into
    # the writerow()
    for key in sorted(d):
        writer_object.writerow([key]*d[key])

    # Close the file object
    f_object.close()


# I created file with 1 bln integers from 1 to 120. The runtime process lasted 10 minutes.

file_size = os.path.getsize('/home/arman/Documents/Arman/Data Science - Code Republic/Computer Science/1bln_sort/sorted_file')

print("File Size is :", file_size, "bytes")







