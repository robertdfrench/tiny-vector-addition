#!/usr/bin/env python

vector_a = [1,1,1,1,1]
vector_b = [1,1,1,1,1]
vector_c = [0,0,0,0,0]
for i in range(0,len(vector_a)):
	vector_c[i] = vector_a[i] + vector_b[i]

print vector_c
