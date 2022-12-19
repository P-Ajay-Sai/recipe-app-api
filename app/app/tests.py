""""
Sample test 
"""
from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    def test_add_number(self):
        res=calc.add(4,99)
        self.assertEqual(res,103)

    def test_subtract_numbers(self):
        res=calc.subtract(10,2)
        return self.assertEqual(res,8)