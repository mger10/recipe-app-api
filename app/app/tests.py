"""

Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        res = calc.subtract(56, 15)

        self.assertEqual(res, 41)
# This is a new line that ends the file.