import unittest
from zstats.stats import *

data0 = [1.0, 2.0, 3.0, 4.0, 5.0]
data2 = [1.0, 2.0, 2.0, 4.0, 5.0]

class TestStats(unittest.TestCase):

    def test_zcount(self):
        self.assertEqual(zcount(data2), 5)

    def test_mean(self):
        self.assertEqual(zmean(data0), 3)

    def test_mode(self):
        self.assertEqual(zmode(data2), 2.0)

    def test_median(self):
        self.assertEqual(zmedian(data2), 2.0)

    def test_median(self):
        self.assertEqual(zmedian(data0), 3.0)


if __name__ == '__main__':
    unittest.main()

