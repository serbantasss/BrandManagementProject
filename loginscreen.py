from tkinter import *


class LoginPage:
    def __init__(self,master,connection,univbg,univfg):
        self.root=master
        self.root.geometry('300x300')
        self.root.title('LOGIN SCREEN')
        self.univbg=univbg
        self.univfg=univfg
        self.root.config(bg='white')
        self.user='none'

        self.label1 = Label(self.root, text='Username:', bg='white', fg='black')
        self.label1.grid(row=0, column=0, sticky=W)
        self.username = StringVar()
        self.usrEntry = Entry(self.root, textvariable=self.username, bg='white', fg='black')
        self.usrEntry.grid(row=0, column=1, sticky=W)

        self.label2 = Label(self.root, text='Password:', bg='white', fg='black')
        self.label2.grid(row=1, column=0, sticky=W)
        self.password = StringVar()
        self.pasEntry = Entry(self.root, textvariable=self.password, bg='white', fg='black', show='*')
        self.pasEntry.grid(row=1, column=1, sticky=W)

        self.errorcode = StringVar()
        self.errorcode.set(" ")
        self.label3 = Label(self.root, textvariable=self.errorcode, bg='white', fg='red')
        self.label3.grid(row=2)

        self.checkButton = Button(self.root, text='LOGIN', bg='white', fg='black')
        self.checkButton.grid(row=3)
