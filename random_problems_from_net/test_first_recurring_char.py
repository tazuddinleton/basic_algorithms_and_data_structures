import unittest
from first_recurring_char import *


class TestFirstRecurrChar(unittest.TestCase):
    def test_first_recurr_char(self):
        # str = 'ABCDA'
        test1 = 'ABCDA'
        self.assertEquals(first_recurr_char(test1), 'A')
        # str = 'AAAAAAAAAAA'
        test2 = 'AAAAAAAAAAA'
        self.assertEquals(first_recurr_char(test2), 'A')
        # str = 'ABCDEFGHIJKLMNOPQRSTUVWXX'
        test3 = 'ABCDEFGHIJKLMNOPQRSTUVWXX'
        self.assertEquals(first_recurr_char(test3), 'X')
        # str = 'ABCDEFGHIJKLMNOPQRSTUVWX'
        test4 = 'ABCDEFGHIJKLMNOPQRSTUVWX'
        self.assertEquals(first_recurr_char(test4), None)
