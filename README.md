# Credential Management

This is a standalone application to store user name and password. It provides following feature:

 - Add Credential
 - Update Credential
 - Get Credential by Title
 - Get All Credentials
 - Delete Credential by Title

The application has in-memory database with only one table with three columns: User Name, Password and Title. Title is a key which is used to differentiate the credentials.

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
 
