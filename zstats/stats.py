#!/Users/deana/Documents/projects/python-basics-stats-deanastuart/zstats/
from math import sqrt
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
    return mean

def zvariance(data):
    n = zcount(data) -1
    # mean = sum(data)/n
    deviations = []
    for i in data:
        deviations.append((zmean(data)-i) ** 2)
    variance = (sum(deviations) / n)
    return round(variance,3)

def zmedian(data):
    sorted_list = []

    while data:
        minimum = data[0]
        for x in data:
            if x < minimum:
                minimum = x
        sorted_list.append(minimum)
        data.remove(minimum)

    n= len(sorted_list)
    if zcount(sorted_list) % 2 == 0:
        median1 = sorted_list[n//2]
        median2 = sorted_list[n//-1]
        median = (median1 + median2)/2
    else:
        median = sorted_list[n//2]
    return median

def zmode(data):
    mode = max(data, key = data.count)
    return mode
def zstdev(data):
    return sqrt(zvariance(data))

def zstderr(data):
    return zstdev(data)/sqrt(zcount(data))

def cov(lista, listb):
    sum=0
    if zcount(lista) == zcount(listb):
        for i in range(0,zcount(lista)):
            sum += ((lista[i] - zmean(lista)) * (listb[i] - zmean(listb)))
        cov = sum/(zcount(lista) - 1)
        return cov

def zcorr(lista,listb):
    correlation = cov(lista,listb) / (zstdev(lista) * zstdev(listb))

    return round(correlation,3)

if __name__ == '__main__':
    x,y = openfiles('/Users/deana/documents/projects/python-basic-stats-deanastuart/dataZero.csv')
    x1,y1 = openfiles('/Users/deana/documents/projects/python-basic-stats-deanastuart/dataOne.csv')
    x2,y2 = openfiles('/Users/deana/documents/projects/python-basic-stats-deanastuart/dataTwo.csv')
    x3,y3 = openfiles('/Users/deana/documents/projects/python-basic-stats-deanastuart/dataThree.csv')

    print("dataOne.csv\n" + " " + str(zmean(x1)) +" "+ str(zvariance(x1)) + " "+str(zmean(y1)) +" " + str(zvariance(y1)) +" "+ str(zcorr(x1,y1)))
    print("dataTwo.csv\n" + " " + str(zmean(x2)) +" "+ str(zvariance(x2)) + " "+str(zmean(y2)) +" " + str(zvariance(y2)) +" "+ str(zcorr(x2,y2)))
    print("dataThree.csv\n" + " " + str(zmean(x3)) +" "+ str(zvariance(x3)) + " "+str(zmean(y3)) +" " + str(zvariance(y3)) +" "+ str(zcorr(x3,y3)))
    print("dataZero.csv\n" + " " + str(zmean(x)) +" "+ str(zvariance(x)) + " "+str(zmean(y)) +" " + str(zvariance(y)) +" "+ str(zcorr(x,y)))

