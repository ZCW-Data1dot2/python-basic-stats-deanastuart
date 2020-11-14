import math
import csv

def openfiles(path):
    x = []
    y = []
    with open(path) as csvfile:
        lists = csv.reader(csvfile)
        for row in lists:
            x.append(row[0])
            y.append(row[1])
    x.pop(0)
    y.pop(0)
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    return x, y

def zcount(data):
    count = 0
    for i in data:
        count += 1
    return count

def zmean(data):
    list = []
    for i in data:
        list.append(i)
    list = sum(list)

    mean = round(list /zcount(data), 3)
    print(mean)

def zvariance(data):
    n = zcount(data)-1
    mean = sum(data)/n
    deviations = []
    for i in data:
        deviations.append((mean-i)**2)
    return (round(sum(deviations)/n),2)

def zmode()

def zmedian():
    pass

def zmode():
    pass

def zstdev():
    pass

def zstderr():
    pass

def zcorr(lista,listb)




x,y = openfiles('/Users/deana/documents/projects/python-basic-stats-deanastuart/dataOne.csv')
zcount(x)
zmean(x)
zvariance(x)
