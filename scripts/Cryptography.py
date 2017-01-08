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


    def __init__(self):
        '''
        Constructor
        '''

    def encode(self, key, clear):
        enc = []
        for i in range(len(clear)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        logging.info("Encoded value {}".format(enc))
        return base64.urlsafe_b64encode(''.join(format(ord(x), 'b') for x in enc))
    
    def decode(self, key, enc):
        dec = []
        enc = base64.urlsafe_b64decode(enc)
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        logging.info("Decoded value {}".format(dec))
        return "".join(dec)
