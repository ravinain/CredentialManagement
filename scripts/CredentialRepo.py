'''
Created on Jan 7, 2017

@author: cdacr
'''

import logging
from tinydb import TinyDB, Query
import os

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
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        self.db = TinyDB('{}/credentials_db.json'.format(dir_path))
        self.query = Query()
    
    def addCredential(self, userName, password, title):
        insertObj = {'userName':userName, 'password':password, 'title':title}
        self.db.insert(insertObj)
        count = self.db.count(self.query.title == title)
        return True if count == 1 else False
        
    def deleteCredential(self, title):
        self.db.remove(self.query.title == title)
        count = self.db.count(self.query.title == title)
        return True if count == 0 else False
        
    def updateCredential(self, userName, password, title):
        self.db.update({'userName':userName, 'password':password}, self.query.title == title)
        credentialAfterUpdate = self.db.search(self.query.title == title)
        return credentialAfterUpdate[0]['userName'] == userName and credentialAfterUpdate[0]['password'] == password 
        
    def getCredential(self, title):
        return self.db.search(self.query.title == title) 
    
    def getAllCredentials(self):
        return self.db.all()