from tkinter import *
class MainPage:
    def __init__(self,connection,user,univbg,univfg):
        self.root = Tk()
        self.univbg = univbg
        self.univfg = univfg
        x:int= 0
        self.bavailprod = Button(self.root, text="SHOW AVAILABE PRODUCTS", bg=self.univbg,fg=self.univfg)
        self.bavailprod.grid(row=x)
        x += 1
        self.bcrtord = Button(self.root, text="CREATE ORDER", bg=self.univbg, fg=self.univfg)
        self.bcrtord.grid(row=x)
        x += 1
        self.baddcl = Button(self.root, text="ADD CLIENT", bg=self.univbg, fg=self.univfg)
        self.baddcl.grid(row=x)
        x += 1
        self.baddpro = Button(self.root, text="ADD PRODUCT", bg=self.univbg, fg=self.univfg)
        self.baddpro.grid(row=x)
        x += 1