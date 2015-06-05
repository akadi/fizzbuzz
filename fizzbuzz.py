# -*- coding: utf-8 -*-
# Author(s): Abdelhalim Kadi <kadi.halim@gmail.com>
#FizzBuzz function

def fizz_buzz(number):
    """
    For a given number > 0:
    Return:
        - u"fizz" if number is diviable by 3.
        - u"bizz" if number is diviable by 5.
        - u"fuzzbuzz" if number is diviable by 15.
        - number else.
    """
    fizz = number % 3
    buzz = number % 5
    fizzbuzz = number % 15
    if not fizzbuzz:
        #is deviable by 15
        return u"fizzbuzz"
    if not buzz:
        #is diviable by 5
        return u"bizz"
    if not fizz:
        #is diviable by 3
        return u"fizz"
    else:
        return number
