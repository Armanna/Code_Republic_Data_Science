import csv
from csv import writer
import os




# Create Cursor dictionary: keys -> k files each < 200MB, and values -> cursor index for each file (k1, k2, ...)
cursors = {}
k = 1
for i in range(200):
    cursors[k] = 0
    k += 1

sort_final = []

while len(sort_final) < 1000000000:
    print('next')
    s = {}

    file = open('/home/arman/Documents/Arman/Data Science - Code Republic/Computer Science/create_sort_4_billion/create')
    csvreader = csv.reader(file)
    for row in range(200):
        a = sorted(list(next(csvreader)))
        s[row + 1] = a[cursors[row + 1]]

    m = min(s.values())

    for key, value in s.items():
        if value == m:
            cursors[key] += 1
            sort_final.append(m)


    file.close()

    with open('/home/arman/Documents/Arman/Data Science - Code Republic/Computer Science/create_sort_4_billion/sorted', 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(sort_final)

        # Close the file object
        f_object.close()


# I created file with 1 bln integers from [-500;500]. The runtime process lasted 40 minutes.

file_size = os.path.getsize('/home/arman/Documents/Arman/Data Science - Code Republic/Computer Science/create_sort_4_billion/sorted')

print("File Size is :", file_size/1000000000, "GB")






