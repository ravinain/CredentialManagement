'''
Created on Jan 7, 2017

@author: cdacr
'''

import logging
from tinydb import TinyDB, Query

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CredentialRepo():
    '''
    CredentialRepo
    '''


    def __init__(self):
        '''
        Credential Repo constructor
        '''
        self.db = TinyDB('credentials_db.json')
        self.query = Query()
    
    def addCredential(self, userName, password, title):
        logging.info('User name and password is: {} {} {}'.format(userName, password, title))
        self.db.insert({'userName':userName, 'password':password, 'title':title})
        count = self.db.count(self.query.title == title)
        return True if count == 1 else False
        
    def deleteCredential(self, title):
        logging.info('Credential id is {}'.format(title))
        self.db.remove(self.query.title == title)
        count = self.db.count(self.query.title == title)
        return True if count == 0 else False
        
    def updateCredential(self, userName, password, title):
        logging.info('update credential details: {} {} {}'.format(userName, password, title))
        self.db.update({'userName':userName, 'password':password}, self.query.title == title)
        credentialAfterUpdate = self.db.search(self.query.title == title)
        logging.info('credentialAfterUpdate {}'.format(credentialAfterUpdate))
        return credentialAfterUpdate[0]['userName'] == userName and credentialAfterUpdate[0]['password'] == password 
        
    def getCredential(self, title):
        logging.info('get credential for {}'.format(title))
        return self.db.search(self.query.title == title) 
    
    def getAllCredentials(self):
        return self.db.all()