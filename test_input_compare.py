import io
import random
from unittest.mock import patch
import unittest
from codingTest import *
from io import StringIO
import time
import sys
"""
NOTE : The types of the answer and the input are very important. 
"""
def percent(idx):
    return random.randint(1, 100) <= idx

def make_data():
    res = []
    N = 5000
    M = 50
    G = [str(random.randint(1, 9)) for _ in range(N)]
    res.append(f'{N}\n')
    res.append(' '.join(G) + "\n")
    res.append(f'{M}\n')
    for _ in range(M):
        if percent(50):
            a = 1
            b = random.randint(1, N)
            c = random.randint(b, N)
            d = random.randint(1, 9)
            res.append(f"{a} {b} {c} {d}\n")
        else:
            a = 2
            b = random.randint(1, N)
            c = random.randint(1, 9)
            res.append(f"{a} {b} {c}\n")
    return res

class MyTestCase(unittest.TestCase):
    def test_solution(self):
        for k in range(10000):
            lines = make_data()

            user_input1 = ''.join(lines)

            start_time = time.time()
            sys.stdin = io.StringIO(user_input1)
            res1 = solution()
            # cur_time = time.time()
            # print("res1", cur_time - start_time)
        #
        #     start_time = time.time()
            sys.stdin = io.StringIO(user_input1)
            res2 = solution2()
            # cur_time = time.time()
            # print("res1", cur_time - start_time)

            if res1 != res2:
                for i in lines:
                    print(i, end="")
                print(res1, res2)
                break
        else:
            print("Success")


if __name__ == '__main__':
    unittest.main()
