'''
Created on Jan 7, 2017

@author: cdacr
'''

import logging
from scripts.CredentialService import CredentialService

class CredentialController():
    '''
    CredentialController
    '''


    def __init__(self):
        '''
        Credential Controller constructor
        '''
        self.credentialService = CredentialService()
    
    def addCredential(self, key, userName, password, title):
        return self.credentialService.addCredential(key, userName, password, title)
        
    def deleteCredential(self, title):
        return self.credentialService.deleteCredential(title)
        
    def updateCredential(self, key, userName, password, title):
        return self.credentialService.updateCredential(key, userName, password, title)
        
    def getCredential(self, key, title):
        return self.credentialService.getCredential(key, title)
    def getAllCredentials(self, key):
        return self.credentialService.getAllCredentials(key)
    
