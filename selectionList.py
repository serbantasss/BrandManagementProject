from tkinter import *

def changeAvailableState( list):
    for x in list.buttons:
        if (x['state'] == NORMAL):
            x.config(state=DISABLED)
        else:
            x.config(state=NORMAL)

class List:
    def __init__(self,master,posx,posy,selectAllOption,ListForSelection,defaultState,defaultBackGround,defaultForeground):
        #super(List, self).__init__()
        self.master = master
        self.SAOption = selectAllOption
        self.ListForSelection = ListForSelection
        self.px=posx
        self.py=posy
        self.defaultState=defaultState
        self.bg=defaultBackGround
        self.fg=defaultForeground

        self.SelectedElements = []
        self.CheckVar = []
        self.buttons = []
        self.nr=0

        if self.SAOption == 1 :

            x=BooleanVar()
            self.CheckVar.append(x)

            b = Checkbutton(self.master, text="SELECT ALL", variable=self.CheckVar[self.nr],state=self.defaultState,bg=self.bg,fg=self.fg, command= self.selectall)
            self.buttons.append(b)

            self.buttons[self.nr].grid(row=self.px,column=self.py,sticky=W)

            self.nr=self.nr+1
            self.px=self.px+1
        for x in self.ListForSelection:
            self.createbutton(x)
    def createbutton(self,title) :
        x = BooleanVar()
        self.CheckVar.append(x)
        b = Checkbutton(self.master, text=title, variable=self.CheckVar[self.nr],state=self.defaultState,bg=self.bg,fg=self.fg)
        self.buttons.append(b)

        self.buttons[self.nr].grid(row=self.px, column=self.py,sticky=W)
        self.nr = self.nr + 1
        self.px = self.px + 1
    def selectall(self):
        if self.CheckVar[0].get() == 1:
            #print("selecting all")
            for x in range(1, self.nr):
                self.buttons[x].invoke()
        else:
            #print("deselecting all")
            for x in range(1,self.nr):
                self.buttons[x].invoke()