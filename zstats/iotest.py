import zstats.stats
import unittest


class TestIO(unittest.TestCase):

    @property
    def test_openfiles(self):
        # test_cases = [
        #     {'dataOne.csv': ([10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
        #                      [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74]),
        #      'dataThree.csv': ([8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0],
        #                        [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89]),
        #      'dataTwo.csv': ([10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
        #                      [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
        #      'dataZero.csv': ([10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
        #                       [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])}
        # ]

        path = zstats.openfiles.('python-basic-stats-deanastuart/dataTwo.csv')
        return path
        # with mock.patch("__builtin__.open", mock.mock)

        # for file_path, expected in test_cases:
        #     with self.subTest(f"{file_path}"):
        #         openfiles.reckless_file_reader(file_path)
        #         actual = mock_stout.getvalue()
        #         self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()