'''
Created on Jan 7, 2017

@author: cdacr
'''
import unittest
from scripts import CredentialController


class CredentialControllerTest(unittest.TestCase):
    
    def setUp(self):
        self.credentialController = CredentialController();

    def testAddCredential(self):
        self.assertTrue(self.credentialController.addCredential('admin', 'password'), 'Failed to add credential')
        
    def testDeleteCredential(self):
        self.assertTrue(self.credentialController.deleteCredential(12), 'Failed to delete credential')
        
    def testUpdateCredential(self):
        self.assertTrue(self.credentialController.updateCredential(12, 'user', 'none'), 'Failed to update credential')
        
    def testGetCredential(self):
        self.assertTrue(len(self.credentialController.getCredential('test')) == 1, 'Failed to get credential')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
