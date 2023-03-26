#Write your code below this line 👇
def prime_checker(number):
    prime = True

    # The range(start, stop, step) function returns a sequence of numbers
    # start	Optional. An integer number specifying at which position to start. Default is 0
    # stop	Required. An integer number specifying at which position to stop (not included).
    # step	Optional. An integer number specifying the incrementation. Default is 1
    for i in range(2, number):
        if number % i == 0:
            prime = False

    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# Tests
import unittest
from unittest.mock import patch
from io import StringIO

class MyTest(unittest.TestCase):
# Testing Print output
    def test_1(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            prime_checker(87)
            expected_print = "It's not a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print) 

    def test_2(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            prime_checker(97)
            expected_print = "It's a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_3(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            prime_checker(66)
            expected_print = "It's not a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_4(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            prime_checker(47)
            expected_print = "It's a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)


print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)