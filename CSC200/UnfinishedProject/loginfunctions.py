# Importing the sqlite3 library 
import sqlite3

# Main Class
class Login_Process:
    # Key variables
    connection = sqlite3.connect('userdatabase.db')
    cursor = connection.cursor()
    HasAcc = ""

    # Main part of the code
    def __init__(self):
        print("Welcome to Pychat! Please log into the server.")
        while Login_Process.HasAcc != "Y" and Login_Process.HasAcc != "N":
            Login_Process.HasAcc = input("Do you already have an account? Enter exactly Y or N.")
        # Creates an instance of the other 2 classes then ends the program
        self.create = Create_Account()
        self.enter = Login()
        self.end()
    
    # Closes the connection to the database
    def end(self):
        Login_Process.connection.close()
        print("Successfully Logged In!")


# Class defining functions if person needs to create an account
class Create_Account:
    def __init__(self):
        self.make_account()

    def make_account(self):
        if Login_Process.HasAcc == "N":
            self.Uname = str(input("Enter your username. It will be space sensitive."))
            self.Password = str(input("Enter your password. It will be space sensitive."))
            Login_Process.cursor.execute('INSERT INTO Users (Username, Password) VALUES (?, ?)', (self.Uname, self.Password))
            Login_Process.connection.commit()
            Login_Process.HasAcc = "Y"
            self.reload()
    
    # "Reloads" the database so that the new account is shown
    def reload(self):
        Login_Process.cursor = Login_Process.connection.execute("SELECT Username, Password from Users")


# Class defining functions for logging in
class Login:
    def __init__(self):
        self.login()

    def login(self):
        self.Signedin = False
        if Login_Process.HasAcc == "Y":
            while self.Signedin == False:
                self.Uname = str(input("What is your username? This is space sensitive."))
                self.Password = str(input("What is your password? This is also space sensitive."))
                self.accexist = False
                for row in Login_Process.cursor:
                    if (self.Uname, self.Password) == (row[0],row[1]):
                        self.Signedin = True
                        pass
                    if self.Uname == row[0]:
                        self.accexist = True
            if self.accexist != True:
                print("There is no user named " + self.Uname + " in this server.")
            if self.Signedin == False:
                print("Login failed. Please try again.")
            Login_Process.cursor = Login_Process.connection.execute("SELECT Username, Password from Users")


# Makes an instance of the main class
run = Login_Process()
