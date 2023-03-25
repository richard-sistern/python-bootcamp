import math

def paint_calc(height, width, coverage):
    cans = math.ceil((height * width) / coverage) 
    print(f"You'll need {cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

paint_calc(height = test_h, width = test_w, coverage = 5)



# Tests
import unittest
from unittest.mock import patch
from io import StringIO

class MyTest(unittest.TestCase):
# Testing Print output
    def test_1(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(3, 6, 5)
            expected_print = "You'll need 4 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print) 

    def test_2(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(3, 9, 5)
            expected_print = "You'll need 6 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_3(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(7, 9, 2)
            expected_print = "You'll need 32 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_4(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(12, 45, 5)
            expected_print = "You'll need 108 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)


print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)