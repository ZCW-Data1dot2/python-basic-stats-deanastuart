import zstats.stats
import unittest

from zstats import stats


class TestIO(unittest.TestCase):

    def test_openfiles(self):
        # stats.openfiles('/Users/deana/Documents/Projects/python-basic-stats-deanastuart/dataOne.csv')

        self.assertEqual(stats.openfiles('/Users/deana/Documents/Projects/python-basic-stats-deanastuart/dataOne.csv'),([10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
                             [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74]))
        self.assertEqual(stats.openfiles('/Users/deana/Documents/Projects/python-basic-stats-deanastuart/dataThree.csv'),([8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0],
                            [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]))

if __name__ == '__main__':
    unittest.main()