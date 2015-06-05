#Test fizzbuzz function
#See http://content.codersdojo.org/code-kata-catalogue/fizz-buzz
#For lanch test:
#$python test_fizzbuzz.py

import unittest
from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    """ Class for test get Fizz Buzz"""
    def test_get_romain_numerals(self):
        """
        Test FizzBuzz function
        """
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(2), 2)
        self.assertEqual(fizz_buzz(3), u"fizz")
        self.assertEqual(fizz_buzz(4), 4)
        self.assertEqual(fizz_buzz(5), u"bizz")
        self.assertEqual(fizz_buzz(15), u"fizzbuzz")
        self.assertEqual(fizz_buzz(20), u"bizz")
        self.assertEqual(fizz_buzz(21), u"fizz")
        self.assertEqual(fizz_buzz(45), u"fizzbuzz")

if __name__ == '__main__':
    unittest.main()

