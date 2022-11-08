import argparse
import unittest
parser = argparse.ArgumentParser()
parser.add_argument("-p", dest="problem", action="store")  # extra value
args = parser.parse_args()



from test_all import a
a()

from test_all import MyTestCase
unittest.main()
