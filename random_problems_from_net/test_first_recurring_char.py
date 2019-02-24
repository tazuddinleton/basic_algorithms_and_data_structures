import unittest
from first_recurring_char import *


class TestFirstRecurrChar(unittest.TestCase):
    def test_first_recurr_char(self):
        self.assertEquals(first_recurr_char('ABCDA'), 'A')
        self.assertEquals(first_recurr_char('AAAAAAAAAAA'), 'A')
        self.assertEquals(first_recurr_char('ABCDEFGHIJKLMNOPQRSTUVWXX'), 'X')
        self.assertEquals(first_recurr_char('ABCDEFGHIJKLMNOPQRSTUVWX'), None)
