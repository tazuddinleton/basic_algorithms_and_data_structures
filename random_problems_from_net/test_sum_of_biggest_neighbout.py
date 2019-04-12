from sum_of_biggest_neighbour import *
import unittest


class TestSumOfBiggestNeighbour(unittest.TestCase):
    def test_sum_of_biggest_neighbour(self):
        # self.assertEqual(sum([1, 2, 1, 5, 5, 3, 3, 3, 4]), 10)
        self.assertEqual(sum([1, 6, 1, 2, 6, 1, 6, 6]), 12)
