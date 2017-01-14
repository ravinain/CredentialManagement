'''
Created on Jan 7, 2017

@author: cdacr
'''
from scripts.CredentialController import CredentialController

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
        key = input("Please enter a key : ")
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
                print('Credentials has been added successfully!') if result else print('An error occurred. This might be duplicate credential!')
            elif option == 2:
                print("Enter title: ")
                title = input()
                print("Enter user name: ")
                userName = input()
                print("Enter password: ")
                password = input()
                result = self.credentialController.updateCredential(key, userName, password, title)
                print('Credentials has been updated successfully!') if result else print('An error occurred. Please check whether credential exists or not!')
            elif option == 3:
                print("Enter title: ")
                title = input()
                result = self.credentialController.getCredential(key, title)
                self.printGetResult(result)
            elif option == 4:
                result = self.credentialController.getAllCredentials(key)
                self.printGetResult(result)
            elif option == 5:
                print("Enter title: ")
                title = input()
                result = self.credentialController.deleteCredential(title)
                print('Credentials has been deleted successfully!') if result else print('An error occurred. Please check whether credential exists or not!')
            elif option == 0:
                print("Good bye!!!")
                break
            else:
                print("Incorrect option")
            print('_'*90)
                
    def printOptions(self):
        print("Please choose option:")
        print("1: Add new credential")
        print("2: Update new credential")
        print("3: Search credential")
        print("4: Search all credential")
        print("5: Delete credential")
        print("0: Exit")         
        
    def printGetResult(self, data):
        print('_'*90)
        print("{0:30} {1:30} {2:30}".format("Title", "User Name", "Password"))
        print('-'*90)
        if len(data) == 0:
            print(repr('No credentials exists!').rjust(50, ' '))
        else:
            for d in data:
                print("{0:30} {1:30} {2:30}".format(d['title'], d['userName'], d['password']))
        print('_'*90)
        
main = Main()
main.processRequest()