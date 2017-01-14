'''
Created on Jan 8, 2017

@author: cdacr
'''
import base64
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
        logger.info('Total key_num {}'.format(key_num))
        key_num = key_num % self.MAX_UNICODE
        
        for i in range(len(clear)):
            enc_c = chr((ord(clear[i]) + key_num) % self.MAX_UNICODE)
            enc.append(enc_c)
        
        #encodedValue = base64.urlsafe_b64encode(bytes(''.join(enc), "utf-8"))
        logger.info('Encrypted pwd {}'.format(''.join(enc)))
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
        logger.info('decrypted : {}'.format(dec))
        return ''.join(dec)
