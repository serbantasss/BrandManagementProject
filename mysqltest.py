from tkinter import *
from tkcalendar import Calendar
from PIL import ImageTk
from selectionList import *

class ProductFilterPage:
    def __init__(self,master,connection):
        self.connection=connection
        self.Cities = self.getCITIES()
        self.InDoorTypes = self.getPLACEMENT_TYPE('INDOOR')
        self.OutDoorTypes = self.getPLACEMENT_TYPE('OUTDOOR')
        self.Malls = self.getLOCATION_NAME('MALL')
        self.Hipermarkets = self.getLOCATION_NAME('HIPERMARKET')
        self.BussinessCentres = self.getLOCATION_NAME('BUSSINESSCENTRE')
        # MAIN
        self.root=master
        self.root.geometry('600x750')
        self.root.title('test1')
        self.root.config(bg='white')
        self.paddings = {'padx': 5, 'pady': 2}
        self.univbg = 'white'
        self.univfg = 'black'
        framex: int = 0
        labelx: int = 0
        self.frames = [None] * 20
        self.labels = [None] * 20

        # LOGO
        self.Myimg = ImageTk.PhotoImage(file="logo.png")
        self.labels[labelx] = Label(self.root, image=self.Myimg, bg=self.univbg)
        self.labels[labelx].grid(row=framex, sticky=W)
        labelx += 1
        framex += 1
        # LOGO!

        # Calendar for dates<------------------------------------------------>
        self.frames[framex] = Frame(self.root, bg=self.univbg)
        self.frames[framex].grid(row=framex, **self.paddings, sticky=W)

        self.labels[labelx] = Label(self.frames[framex], text='Select Start Date:', bg=self.univbg, fg=self.univfg)
        self.labels[labelx].grid(row=0, column=0, **self.paddings)
        labelx += 1
        self.cal1 = Calendar(self.frames[framex], firstweekday="monday", foreground='black', background='#C0C0C0',
                        selectforeground='green',
                        font='Arial 12', date_pattern='y-mm-dd')
        self.cal1.grid(row=1, column=0, **self.paddings)

        self.labels[labelx] = Label(self.frames[framex], text='Select End Date:', bg=self.univbg, fg=self.univfg)
        self.labels[labelx].grid(row=0, column=1, **self.paddings)
        labelx += 1
        self.cal2 = Calendar(self.frames[framex], firstweekday="monday", foreground='black', background='#C0C0C0',
                        selectforeground='green',
                        font='Arial 12', date_pattern='y-mm-dd')
        self.cal2.grid(row=1, column=1, **self.paddings)
        framex += 1
        # Calendar for dates<------------------------------------------------>!

        # Client<------------------------------------------------>
        self.frames[framex] = Frame(self.root, bg=self.univbg)
        self.frames[framex].grid(row=framex, sticky=W, **self.paddings)

        self.labels[labelx] = Label(self.frames[framex], bg=self.univbg, fg=self.univfg, text='Client:')
        self.labels[labelx].grid(row=0, column=0, **self.paddings)
        labelx += 1
        self.client = StringVar()
        self.clientinputfield = Entry(self.frames[framex], bg=self.univbg, fg=self.univfg, textvariable=self.client, bd=1)
        self.clientinputfield.grid(row=0, column=1)
        framex += 1
        # Client<------------------------------------------------>!

        # Campaign Name<------------------------------------------------>
        self.frames[framex] = Frame(self.root, bg=self.univbg)
        self.frames[framex].grid(row=framex, sticky=W, **self.paddings)

        self.labels[labelx] = Label(self.frames[framex], bg=self.univbg, fg=self.univfg, text='Campaign Name:')
        self.labels[labelx].grid(row=0, column=0, **self.paddings)
        labelx += 1

        self.campain = StringVar()
        self.campaininputfield = Entry(self.frames[framex], bg=self.univbg, fg=self.univfg, textvariable=self.campain, bd=1)
        self.campaininputfield.grid(row=0, column=1)
        framex += 1
        # Campaign Name<------------------------------------------------>!

        # CITY <------------------------------------------------>
        self.frames[framex] = Frame(self.root, bg=self.univbg)
        self.frames[framex].grid(row=framex, **self.paddings, sticky=W)

        self.labels[labelx] = Label(self.frames[framex], text='City:', bg=self.univbg, fg=self.univfg)
        self.labels[labelx].grid(row=0, column=0, sticky=W, **self.paddings)
        labelx += 1
        selectionCITY = List(self.frames[framex], 0, 1, 1, self.Cities, NORMAL, self.univbg, self.univfg)

        framex += 1
        # CITY <------------------------------------------------>!

        # Location type<------------------------------------------------>
        self.frames[framex] = Frame(self.root, bg=self.univbg)
        self.frames[framex].grid(row=framex, **self.paddings, sticky=W)

        self.labels[labelx] = Label(self.frames[framex], text='Location Type:', bg=self.univbg, fg=self.univfg)
        self.labels[labelx].grid(row=0, column=0, sticky=W, **self.paddings)
        labelx += 1
        self.selectionLocation = List(self.frames[framex], 0, 1, 1, ['BUSSINES CENTRE', 'HIPERMARKET', 'MALL'], NORMAL, self.univbg, self.univfg)

        self.selectionMalls = List(self.frames[framex], 0, 2, 1, self.Malls, DISABLED, self.univbg, self.univfg)
        self.selectionHipermaket = List(self.frames[framex], 0, 3, 1, self.Hipermarkets, DISABLED, self.univbg, self.univfg)
        self.selectionBussinessCentre = List(self.frames[framex], 0, 4, 1, self.BussinessCentres, DISABLED, self.univbg, self.univfg)

        self.selectionLocation.buttons[1].config(command=lambda: changeAvailableState(self.selectionBussinessCentre))
        self.selectionLocation.buttons[2].config(command=lambda: changeAvailableState(self.selectionHipermaket))
        self.selectionLocation.buttons[3].config(command=lambda: changeAvailableState(self.selectionMalls))

        framex += 1
        # Location Type<------------------------------------------------>!

        # Exposure type<------------------------------------------------>
        self.frames[framex] = Frame(self.root, bg=self.univbg)
        self.frames[framex].grid(row=framex, **self.paddings, sticky=W)

        self.labels[labelx] = Label(self.frames[framex], text='Exposure type:', bg=self.univbg, fg=self.univfg)
        self.labels[labelx].grid(row=0, column=0, **self.paddings)
        labelx += 1
        self.selectionINOUT = List(self.frames[framex], 0, 1, 1, ['INDOOR', 'OUTDOOR'], NORMAL, self.univbg, self.univfg)
        self.selectionTYPEIN = List(self.frames[framex], 0, 2, 1, self.InDoorTypes, DISABLED, self.univbg, self.univfg)
        self.selectionTYPEOUT = List(self.frames[framex], 0, 3, 1, self.OutDoorTypes, DISABLED, self.univbg, self.univfg)

        self.selectionINOUT.buttons[1].config(command=lambda: changeAvailableState(self.selectionTYPEIN))
        self.selectionINOUT.buttons[2].config(command=lambda: changeAvailableState(self.selectionTYPEOUT))
        framex += 1
        # Exposure type<------------------------------------------------>!

        # Digital support<------------------------------------------------>
        self.frames[framex] = Frame(self.root, bg=self.univbg)
        self.frames[framex].grid(row=framex, **self.paddings, sticky=W)

        self.labels[labelx] = Label(self.frames[framex], text='Digital support:', bg=self.univbg, fg=self.univfg)
        self.labels[labelx].grid(row=0, column=0, sticky=W, **self.paddings)
        labelx += 1

        self.digital = BooleanVar()
        self.digitalButton = Checkbutton(self.frames[framex], variable=self.digital, bg=self.univbg, fg=self.univfg)
        self.digitalButton.grid(row=0, column=1, sticky=W)
        framex += 1
        # Digital support<------------------------------------------------>!

        # Print support<------------------------------------------------>
        self.frames[framex] = Frame(self.root, bg=self.univbg)
        self.frames[framex].grid(row=framex, **self.paddings, sticky=W)

        self.labels[labelx] = Label(self.frames[framex], text='Print support:', bg=self.univbg, fg=self.univfg)
        self.labels[labelx].grid(row=0, column=0, sticky=W, **self.paddings)
        labelx += 1

        self.printt = BooleanVar()
        self.printButton = Checkbutton(self.frames[framex], variable=self.printt, bg=self.univbg, fg=self.univfg)
        self.printButton.grid(row=0, column=1, sticky=W)
        framex += 1
        # Print support<------------------------------------------------>!

        # Price range<------------------------------------------------>
        self.frames[framex] = Frame(self.root, bg=self.univbg)
        self.frames[framex].grid(row=framex, **self.paddings, sticky=W)

        self.labels[labelx] = Label(self.frames[framex], text='Price Range:', bg=self.univbg, fg=self.univfg)
        self.labels[labelx].grid(row=0, column=0, sticky=W, **self.paddings)
        labelx += 1

        self.lowprice = IntVar()
        self.highprice = IntVar()
        self.lowprice.set(0)
        self.highprice.set(69000)
        self.lowinput = Entry(self.frames[framex], bg=self.univbg, fg=self.univfg, textvariable=self.lowprice, width=5)
        self.lowinput.grid(row=0, column=1, sticky=W)
        self.highinput = Entry(self.frames[framex], bg=self.univbg, fg=self.univfg, textvariable=self.highprice, width=5)
        self.highinput.grid(row=0, column=2, sticky=W, padx=10)
        framex += 1
        # Price Range<------------------------------------------------>!

        # Sort By<------------------------------------------------>
        self.frames[framex] = Frame(self.root, bg=self.univbg)
        self.frames[framex].grid(row=framex, **self.paddings, sticky=W)

        self.labels[labelx] = Label(self.frames[framex], text='Sort by:', bg=self.univbg, fg=self.univfg)
        self.labels[labelx].grid(row=0, column=0, sticky=W, **self.paddings)
        labelx += 1
        self.sorting = IntVar()
        self.b1 = Radiobutton(self.frames[framex], variable=self.sorting, value=0, text='Most Requested', bg=self.univbg, fg=self.univfg)
        self.b2 = Radiobutton(self.frames[framex], variable=self.sorting, value=1, text='Low->High', bg=self.univbg, fg=self.univfg)
        self.b3 = Radiobutton(self.frames[framex], variable=self.sorting, value=2, text='High->Low', bg=self.univbg, fg=self.univfg)
        self.b1.grid(row=0, column=1, sticky=W, **self.paddings)
        self.b2.grid(row=1, column=1, sticky=W, **self.paddings)
        self.b3.grid(row=2, column=1, sticky=W, **self.paddings)
        framex += 1
        # Sort By<------------------------------------------------>!

        # SEARCH BUTTON
        self.searchButton = Button(self.root, text='SEARCH', font=('calibre', 20, 'normal'), command=self.createquery)
        self.searchButton.grid(row=framex)
        framex += 1
        # SERACH BUTTON
    def getLOCATION_NAME(self,type):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT DISTINCT LOCATION_NAME FROM defaultscheme.Products WHERE LOCATION_TYPE = '{type}'")
        records = cursor.fetchall()
        ret=[]
        for x in records:
            ret.append(x[0])
        return ret
    def getCITIES(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT DISTINCT CITY FROM defaultscheme.Products;")
        records = cursor.fetchall()
        ret = []
        for x in records:
            ret.append(x[0])
        return ret
    def getPLACEMENT_TYPE(self, type):

        cursor = self.connection.cursor()
        cursor.execute(
            f"SELECT DISTINCT PLACEMENT_NAME FROM defaultscheme.Products WHERE PLACEMENT_TYPE = '{type}'")
        records = cursor.fetchall()
        ret = []
        for x in records:
            ret.append(x[0])
        return ret
    def createlist(lista: List, opt):
        if opt == 1:
            ret = ','
        else:
            ret = ''
        ok = True
        for x in range(1, lista.nr):
            if lista.CheckVar[x].get() == True:
                if (ok == True):
                    ret = ret + f' "{lista.ListForSelection[x - 1]}" '
                    ok = False
                else:
                    ret = ret + f' ,"{lista.ListForSelection[x - 1]}" '
        return ret
    def createquery(self):
        fmm = (f"\n"
               f"SELECT DISTINCT Products.NAME, Products.CITY, Products.LOCATION_NAME, Products.PLACEMENT_NAME, Products.COST, Products.SPECIAL_COST\n"
               f"FROM Products\n"
               f"LEFT JOIN Orders\n"
               f"ON Products.PRODUCTID=Orders.PRODUCTID\n"
               f"\n"
               f"WHERE\n"
               f"((GREATEST(\"{self.cal1.get_date()}\",\"{self.cal2.get_date()}\") < Orders.StartDate OR LEAST(\"{self.cal1.get_date()}\",\"{self.cal2.get_date()}\") > Orders.EndDate) AND Orders.Status = \"RESERVED\") OR (Orders.StartDate IS NULL)\n"
               f"AND\n"
               f"Products.COST BETWEEN {self.lowprice.get()} AND {self.highprice.get()}\n"
               )

        fmm = fmm + f"AND\n Products.LOCATION_TYPE in ({self.createlist(self.selectionLocation, 0)})\n"
        fmm = fmm + f"AND\n Products.LOCATION_NAME in ("
        if self.selectionLocation.CheckVar[1].get() == True:
            fmm = fmm + self.createlist(self.selectionMalls, 0)
        if self.selectionLocation.CheckVar[2].get() == True:
            fmm = fmm + self.createlist(selectionHipermaket, (self.selectionLocation.CheckVar[1].get() == True))
        if self.selectionLocation.CheckVar[3].get() == True:
            fmm = fmm + self.createlist(self.selectionBussinessCentre, (
                    self.selectionLocation.CheckVar[1].get() == True or self.selectionLocation.CheckVar[2].get() == True))
        fmm = fmm + ")\n"

        fmm = fmm + f"AND\n Products.PLACEMENT_TYPE in ({self.createlist(self.selectionINOUT, 0)})\n"
        fmm = fmm + "AND\n Products.PLACEMENT_NAME in ("
        if self.selectionINOUT.CheckVar[1].get() == True:
            fmm = fmm + self.createlist(self.selectionTYPEIN, 0)
        if self.selectionINOUT.CheckVar[2].get() == True:
            fmm = fmm + self.createlist(self.selectionTYPEOUT, (self.selectionINOUT.CheckVar[1].get() == True))
        fmm = fmm + ")\n"

        if self.digital.get() == True:
            fmm = fmm + "AND\n Products.DIGITAL_SUPPORT = YES\n"
        if self.printt.get() == True:
            fmm = fmm + "AND\n Products.PRINT_SUPPORT = YES\n"
        if self.sorting.get() == 0:
            fmm = fmm + "ORDER BY Products.DAILY_TRAFFIC DESC\n"
        elif self.sorting.get() == 1:
            fmm = fmm + "ORDER BY Products.COST ASC\n"
        else:
            fmm = fmm + "ORDER BY Products.COST DESC\n"
        return fmm

