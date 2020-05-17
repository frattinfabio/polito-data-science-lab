# LAB1 es.1

# 2.1.1

import csv

list_of_tuples = []
with open("iris.csv") as f:
    for cols in csv.reader(f):
        single_tuple = [float(cols[0]), float(cols[1]), float(cols[2]), float(cols[3]), cols[4]]
        list_of_tuples.append(single_tuple)

# 2.2.2

import statistics

list_sepal_length = []
list_petal_length = []
list_sepal_width = []
list_petal_width = []

for single_tuple in list_of_tuples:
    list_sepal_length.append(single_tuple[0])
    list_sepal_width.append(single_tuple[1])
    list_petal_length.append(single_tuple[2])
    list_petal_width.append(single_tuple[3])

mean_sepal_length = statistics.mean(list_sepal_length)
mean_sepal_width = statistics.mean(list_sepal_width)
mean_petal_length = statistics.mean(list_petal_length)
mean_petal_width = statistics.mean(list_petal_width)

stdev_sepal_length = statistics.stdev(list_sepal_length)
stdev_sepal_width = statistics.stdev(list_sepal_width)
stdev_petal_length = statistics.stdev(list_petal_length)
stdev_petal_width = statistics.stdev(list_petal_width)

print(f"Means: {mean_sepal_length:.2}, {mean_sepal_width:.2}, {mean_petal_length:.2}, {mean_petal_width:.2}")
print(f"Standard deviations: {stdev_sepal_length:.2}, {stdev_sepal_width:.2}, {stdev_petal_length:.2}, {stdev_petal_width:.2}")

# 2.2.3

list_types = ["setosa", "versicolor", "virginica"]

for flower_type in list_types:

    list_flowers = list_setosa = list(filter(lambda x: x[4]==("Iris-"+flower_type), list_of_tuples))

    mean_sepal_length = statistics.mean(map( lambda x: x[0], list_flowers))
    mean_sepal_width = statistics.mean(map( lambda x: x[1], list_flowers))
    mean_petal_length = statistics.mean(map( lambda x: x[2], list_flowers))
    mean_petal_width = statistics.mean(map( lambda x: x[3], list_flowers))
    stdev_sepal_length = statistics.stdev(map( lambda x: x[0], list_flowers))
    stdev_sepal_width = statistics.stdev(map( lambda x: x[1], list_flowers))
    stdev_petal_length = statistics.stdev(map( lambda x: x[2], list_flowers))
    stdev_petal_width = statistics.stdev(map( lambda x: x[3], list_flowers))
    print(f"Means {flower_type:10} : {mean_sepal_length:5.2} {mean_sepal_width:5.2} {mean_petal_length:5.2} {mean_petal_width:5.2}")
    print(f"Stdev {flower_type:10} : {stdev_sepal_length:5.2} {stdev_sepal_width:5.2} {stdev_petal_length:5.2} {stdev_petal_width:5.2}")


# 2.2.4
# the most characterizing measurement is the petal width since is the one with the lowest stdev

#2.2.5
# 5.2, 3.1, 4.0, 1.2 --> versicolor
# 4.9, 2.5, 5.6, 2.0 --> virginica
# 5.4, 3.2, 1.9, 0.4 --> setosa
