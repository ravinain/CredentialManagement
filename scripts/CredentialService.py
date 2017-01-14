'''
Created on Jan 7, 2017

@author: cdacr
'''

import logging
from scripts.CredentialRepo import CredentialRepo
from scripts.Cryptography import Cryptography

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CredentialService():
    '''
    CredentialService
    '''


    def __init__(self):
        '''
        Credential Service constructor
        '''
        self.credentialRepo = CredentialRepo()
        self.cryptography = Cryptography()
    
    def addCredential(self, key, userName, password, title):
        logging.info('User name and password is: {} {} {}'.format(userName, password, title))
        enc_password = self.cryptography.encode(key, password)
        return self.credentialRepo.addCredential(userName, enc_password, title)
        
    def deleteCredential(self, title):
        logging.info('Credential id is {}'.format(title))
        return self.credentialRepo.deleteCredential(title)
        
    def updateCredential(self, key, userName, password, title):
        logging.info('update credential details: {} {} {}'.format(userName, password, title))
        enc_password = self.cryptography.encode(key, password)
        return self.credentialRepo.updateCredential(userName, enc_password, title)
        
    def getCredential(self, key, title):
        logging.info('get credential for {}'.format(title))
        credentials = self.credentialRepo.getCredential(title)
        for credential in credentials:
            credential.password = self.cryptography.decode(key, credential['password'])
        return credentials
    def getAllCredentials(self, key):
        credentials = self.credentialRepo.getAllCredentials()
        
        for credential in credentials:
            credential['password'] = self.cryptography.decode(key, credential['password'])
        return credentials
