'''
Created on Jan 7, 2017

@author: cdacr
'''
from CredentialController import CredentialController

class Main():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.credentialController = CredentialController()
        
    def processRequest(self):
        key = input("Please enter a key")
        while True:
            self.printOptions()
            option = int(input())
            
            if option == 1:
                print("Enter title: ")
                title = input()
                print("Enter user name: ")
                userName = input()
                print("Enter password: ")
                password = input()
                result = self.credentialController.addCredential(key, userName, password, title)
                print("Result : {}".format(result))
            elif option == 2:
                print("Enter title: ")
                title = input()
                print("Enter user name: ")
                userName = input()
                print("Enter password: ")
                password = input()
                password = key + password
                result = self.credentialController.updateCredential(key, userName, password, title)
                print("Result : {}".format(result))
            elif option == 3:
                print("Enter title: ")
                title = input()
                result = self.credentialController.getCredential(key, title)
                print("Result : {}".format(result))
            elif option == 4:
                result = self.credentialController.getAllCredentials(key)
                print("Result : {}".format(result))
            elif option == 5:
                result = self.credentialController.deleteCredential(key, title)
                print("Result : {}".format(result))
            elif option == 0:
                print("Good bye!!!")
                break
            else:
                print("Incorrect option")
                
    def printOptions(self):
        print("Please choose option:")
        print("1: Add new credential")
        print("2: Update new credential")
        print("3: Search credential")
        print("4: Search all credential")
        print("5: Delete credential")
        print("0: Exit")         
        
main = Main()
main.processRequest()