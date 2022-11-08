import argparse
problem = 4485
import io
import unittest.mock
from codingTest import solution
import sys

# scrolling data
import crawling
input_lines, output_lines = crawling.get_input_output(problem=str(problem))

class MyTestCase(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, user_input1, expected_output, mock_stdout):
        sys.stdin = io.StringIO(user_input1)
        solution()
        self.assertEqual(mock_stdout.getvalue().replace('\r', ""),
                         expected_output.replace('\r', ""))

    for i in range(len(input_lines)):
        exec(f"def test_only_numbers_{i}(self):"
             f"    self.assert_stdout(input_lines[{i}], output_lines[{i}])")


if __name__ == '__main__':
    unittest.main()