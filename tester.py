import io
from unittest.mock import patch
import unittest
from codingTest import solution
from io import StringIO
import sys
"""
NOTE : The types of the answer and the input are very important. 
"""

class MyTestCase(unittest.TestCase):

    def test_solution(self):
        with open("input.txt", "r") as f:
            lines = f.readlines()

        user_input1 = ''.join(lines)

        sys.stdin = io.StringIO(user_input1)
        solution()




if __name__ == '__main__':
    unittest.main()
