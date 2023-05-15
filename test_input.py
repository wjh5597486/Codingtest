import io
import unittest
from codingTest import *
import sys


class MyTestCase(unittest.TestCase):
    def test_solution(self):
        with open("input.txt", "r") as f:
            lines = f.readlines()

        user_input1 = ''.join(lines)

        sys.stdin = io.StringIO(user_input1)

        res = solution2()
        print(res)


if __name__ == '__main__':
    unittest.main()
