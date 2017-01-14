'''
Created on Jan 8, 2017

@author: cdacr
'''
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Cryptography():
    '''
    classdocs
    '''
    MAX_UNICODE = 1114111

    def __init__(self):
        '''
        Constructor
        '''

    def encode(self, key, clear):
        enc = []
        key_num = 0
        for i in range(len(key)):
            key_num += ord(key[i])
        key_num = key_num % self.MAX_UNICODE
        
        for i in range(len(clear)):
            enc_c = chr((ord(clear[i]) + key_num) % self.MAX_UNICODE)
            enc.append(enc_c)
        
        return ''.join(enc)
    
    def decode(self, key, enc):
        dec = []
        key_num = 0

        for i in range(len(key)):
            key_num += ord(key[i])
        
        key_num = key_num % self.MAX_UNICODE
        
        for i in range(len(enc)):
            if(key_num <= ord(enc[i])):
                dec_c = chr(ord(enc[i]) - key_num)
            else:
                dec_c = chr(self.MAX_UNICODE + ord(enc[i]) - key_num)
            dec.append(dec_c)
        return ''.join(dec)
