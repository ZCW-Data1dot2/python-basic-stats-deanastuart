import math
import csv

def openfiles(path):
    data = []
    with open(path) as csvfile:
        lists = csv.reader(csvfile)
        for x in lists:
            data.append(x)
    data.pop(0)
    data2 = [[float(j) for j in i] for i in data]
    return data2

def count_x(openfiles):
    count = 0
    for i in openfiles:
        if i[0] is not None:
            count += 1
    return count

def count_y(openfiles):
    count = 0
    for i in openfiles:
        if i[1] is not None:
            count += 1
    return count

def mean_x(openfiles):
    list = []
    for i in openfiles:
        if i[0] is not None:
            list.append(i[0])
    list = sum(list)

    mean = round(list /count_x(openfiles),3)
    return mean

def mean_y(openfiles):
    list = []
    for i in openfiles:
        if i[1] is not None:
            list.append(i[1])
    list = sum(list)

    mean = round(list / count_y(openfiles), 3)
    print(mean)


openfiles('/Users/deana/documents/projects/python-basic-stats-deanastuart/dataOne.csv')
# count_x(openfiles('/Users/deana/documents/projects/python-basic-stats-deanastuart/dataOne.csv'))
mean_y(openfiles('/Users/deana/documents/projects/python-basic-stats-deanastuart/dataOne.csv'))
