'''
Created on Jan 8, 2017

@author: cdacr
'''
import unittest
from scripts.Cryptography import Cryptography


class Test(unittest.TestCase):


    def setUp(self):
        self.cryptography = Cryptography()
        pass


    def tearDown(self):
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEncode']
    unittest.main()