#!/Users/deana/Documents/projects/python-basics-stats-deanastuart/
from stats.py import *


data0 = [1.0, 2.0, 3.0, 4.0, 5.0]
data2 = [1.0, 2.0, 2.0, 4.0, 5.0]

try:
    assert zcount(data0) == 5
    assert zmean(data0) == 3.0
    assert zmode(data2) == 2.0
    assert zmedian(data2) == 2.0
    assert zmedian(data0) == 3.0
except AssertionError as e:
    print(e)


