# LAB1 es.3

# 2.3.1

import csv

all_the_tuples = []
with open("mnist_test.csv")as f:
    for cols in csv.reader(f):
        single_tuple = {"value": 0, "matrix": []}
        single_tuple["value"] = int(cols[0])
        for i in range (1, len(cols)):
            single_tuple["matrix"].append(int(cols[i]))
        all_the_tuples.append(single_tuple)

# 2.3.2

converter = lambda x: " " if x < 64 else "." if x < 128 else "*" if x < 192 else "#"
def plot_number(k):
    converted_number = list(map(converter, all_the_tuples[k-1]["matrix"]))
    for i in range (0, 28):
        for j in range(0, 28):
            print(converted_number[i*28 + j], end = "")
        print("");

plot_number(9900)
# 2.3.3

import math

interesting_positions = [26, 30, 32, 35]

def euclidean_dinstance(v1, v2):
    dist = 0
    for i in range(0, len(v1)):
        dist += (v1[i] - v2[i]) ** 2
    return math.sqrt(dist)

for i in range (0, len(interesting_positions) - 1):
    for j in range(i + 1, len(interesting_positions)):
        first_index = interesting_positions[i]
        second_index = interesting_positions[j]
        print(f"Euclidean dinstance between the {first_index}th and the {second_index}th digits: {euclidean_dinstance(all_the_tuples[first_index-1]['matrix'], all_the_tuples[second_index-1]['matrix']):.6}")

# 2.3.4
# according to the results, the digits should be [0,1,1,7]

# 2.3.5
import numpy

zeros = list(map(lambda x: x["matrix"], filter(lambda x: x["value"] == 0, all_the_tuples)))
ones = list(map(lambda x: x["matrix"], filter(lambda x: x["value"] == 1, all_the_tuples)))

z = numpy.zeros(784, dtype = int)
o = numpy.zeros(784, dtype = int)

for i in range (0, len(zeros)):
    for j in range (0, 784):
        if(zeros[i][j] > 128):
            z[j] = z[j] + 1

for i in range (0, len(ones)):
    for j in range (0, 784):
        if(ones[i][j] > 128):
            o[j] = o[j] + 1

difference = list(abs(o-z))
max_difference = max(difference)
index =  difference.index(max_difference)
print(f"Position : ({index//28}, {index%28})")

# the pixel with the highest value of the difference is exactly located at the centre of the grid
