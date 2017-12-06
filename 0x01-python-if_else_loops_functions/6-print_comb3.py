#!/usr/bin/python3

print(", ".join(["%d%d" % (i, j) for i in range(10) for j in range(i+1, 10)]))

# Reference: http://www.diveintopython.net/native_data_types/joining_lists.html
