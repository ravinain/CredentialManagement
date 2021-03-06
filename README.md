# Credential Management

This is a standalone application to store user name and password. It provides following feature:

 - Add Credential
 - Update Credential
 - Get Credential by Title
 - Get All Credentials
 - Delete Credential by Title

The application is using in-memory database which has only one table and columns are: User Name, Password and Title. Title is a key which is used to differentiate the credentials. The password is stored in encryted format. The encryption and decryption logic is available in Cryptography.py file.

Sample Data:

| Title | User Name | Password |
| ----- | --------- | -------- |
| Gmail Account | Abc.gmail.com | MyPassword |
| Yahoo Account | xyz.yahoo.com | NewPassword |

This project can directly be imported into PyDev(Eclipse) or run on command prompt.
To run it from command prompt: 
 - Go to the path of the project
 - Execute 'python -m scripts.Main.py'
 
 *Note: Python version 3.6.0 must be installed on the system.
 
