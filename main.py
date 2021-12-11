import os
import sqlite3
import mysql.connector
from filterpage import *
from loginscreen import *
from tkinter import messagebox
from mainpage import *

class NewWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text="This is a new Window")
        label.pack()

connection = mysql.connector.connect(host='localhost', database='defaultscheme',user='root',password='Ioana2503')
univbg='white'
univfg='black'

#LOGIN
def login(self):
        if self.username.get() == 'root':
            if self.password.get() == '1234':
                self.user='root'
                loginroot.withdraw()
                mainwidget.root.deiconify()
            else:
                self.errorcode.set("Wrong password.")
        else:
            self.errorcode.set("Invalid username.")
loginroot=Tk()
loginwidget=LoginPage(loginroot,connection,univbg,univfg)
loginwidget.checkButton.config(command=lambda : login(loginwidget))
#LOGIN
mainwidget=MainPage(connection,1,univbg,univfg)
mainwidget.root.withdraw()
mainwidget.bavailprod.config(command=lambda : ProductFilterPage(mainwidget.root,connection,1,univbg,univfg))


mainloop()