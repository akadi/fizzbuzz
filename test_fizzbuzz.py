#Test fizzbuzz function
#See http://content.codersdojo.org/code-kata-catalogue/fizz-buzz
#For lanch test:
#$python test_fizzbuzz

import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    """ Class for test get Fizz Buzz"""
    def test_get_romain_numerals(self):
        """
        Test FizzBuzz function
        """
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(3), u"fizz")
        self.assertEqual(fizzbuzz(4), 4)
        self.assertEqual(fizzbuzz(5), u"bizz")
        self.assertEqual(fizzbuzz(15), u"fizzbuzz")
        self.assertEqual(fizzbuzz(20), u"bizz")
        self.assertEqual(fizzbuzz(21), u"fizz")
        self.assertEqual(fizzbuzz(45), u"fizzbuzz")

if __name__ == '__main__':
    unittest.main()

