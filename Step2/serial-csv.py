#!/usr/bin/env python
import csv

# Read Vector A from Disk into Memory
csv_file_a = open('vector_a.csv','rb')
reader_a = csv.reader(csv_file_a, delimiter=',')
vector_a = reader_a.next()

# Read Vector B from Disk into Memory
csv_file_b = open('vector_b.csv','rb')
reader_b = csv.reader(csv_file_b, delimiter=',')
vector_b = reader_b.next()

# Add A[i] to B[i] and store in C[i]
vector_length = len(vector_a)
vector_c = list()
for i in range(0,vector_length):
	value_of_c_at_position_i = vector_a[i] + vector_b[i]
	vector_c.append(value_of_c_at_position_i)

# Print C[i]
print vector_c
