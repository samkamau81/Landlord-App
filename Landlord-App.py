from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
from PIL import Image, ImageTk

today = datetime.date.today ().strftime ('%d/%m/%Y')

# THE PROGRAMS DATABASE
'''creating the Tenants details table'''
conn = sqlite3.connect ("Landlords.db")
c = conn.cursor ()
c.execute ('''CREATE TABLE IF NOT EXISTS Tenants_Details(
            ID INTEGER PRIMARY KEY,
            House_No  TEXT  ,
            Name TEXT,
            Years INTEGER,
            Month TEXT,
            Rent REAL,
            Electricity REAL, 
            Garbage REAL                    
            )''')
conn.commit ()
conn.close ()


# INSERT DETAILS

def update_info(House_No, Name, Years, Month, Rent, Electricity, Garbage):
    conn = sqlite3.connect ("Landlords.db")
    cur = conn.cursor ()
    cur.execute ("INSERT INTO Tenants_Details VALUES (NULL,?,?,?,?,?,?,?)", (House_No, Name, Years, Month, Rent, Electricity, Garbage))
    conn.commit ()
    conn.close ()


def extract_det():
    conn = sqlite3.connect ("Landlords.db")
    cur = conn.cursor ()
    cur.execute ("SELECT * FROM Tenants_Details")
    row = cur.fetchall ()
    conn.close ()
    return row


def deleteRec(ID):
    conn = sqlite3.connect ("Landlords.db")
    cur = conn.cursor ()
    cur.execute ("DELETE FROM Tenants_Details WHERE ID=?", (ID,))
    conn.commit ()
    conn.close ()


def searchData(House_No="", Name="", Years="", Month="", Rent="", Electricity="", Garbage=""):
    conn = sqlite3.connect ("Landlords.db")
    cur = conn.cursor ()
    cur.execute ("SELECT * FROM Tenants_Details WHERE House_No=? OR Name=? OR Years=? OR Month=? OR Rent=? OR Electricity=? OR Garbage=?",
                 (House_No, Name, Years, Month, Rent, Electricity, Garbage))
    rows = cur.fetchall ()
    conn.close ()
    return rows


def dataUpdate(ID, House_No="", Name="", Years="", Month="", Rent="", Electricity="", Garbage=""):
    conn = sqlite3.connect ("Landlords.db")
    cur = conn.cursor ()
    cur.execute ("UPDATE Tenants_Details SET House_No=? OR Name=? OR Years=? OR Month=? OR Rent=? OR Electricity=? OR Garbage=?",
                 (House_No, Name, Years, Month, Rent, ID, Electricity, Garbage))
    conn.commit ()
    conn.close ()



def exit():
    ex = tkinter.messagebox.askyesno ("Landlord Application", "Confirm if you want to exit")
    if ex > 0:
        home.quit ()
        return


# GRAPHICAL USER INTERFACE
# VIEW PG

def view_pg():
    view = Toplevel (home)
    view.title ("Landlord App")
    photo = PhotoImage (file="Landlord icon.ico")
    view.iconphoto (False, photo)


    view.geometry ("1400x750+0+0")
    House_No = StringVar ()
    Name = StringVar ()
    Years = StringVar ()
    Month = StringVar ()
    Rent = StringVar ()
    Electricity=StringVar ()
    Garbage=StringVar ()


    image = Image.open ('C:\\Users\\BEATRICE\\Desktop\\sams\\SERENE APPARTMENTS\\images.jpg')
    newImage = image.resize ((1500, 1500))
    newImage.save ('image1200.jpg')
    render = ImageTk.PhotoImage (newImage)
    l0 = Label (view, image=render, bd=0)
    l0.image = render

    l0.place (x=0, y=0, relwidth=1, relheight=1, relx=.5, rely=.5, anchor='center')
    l0.lower ()
    def caps(event):
        House_No.set(House_No.get().upper())
        Name.set(Name.get().upper())
        Month .set(Month.get().upper())

    def searchDb():
        Tenantlist.delete (0, END)
        for row in searchData (House_No.get (), Name.get (), Years.get (), Month.get (), Rent.get (),Electricity.get(), Garbage.get()):
            Tenantlist.insert (END, row, str (""))

    def DisplayData():
        Tenantlist.delete (0, END)
        for row in extract_det ():
            Tenantlist.insert (END, row, str (""))

    def TenantsRec(event):
        global sd
        searchtent = Tenantlist.curselection ()[0]
        sd = Tenantlist.get (searchtent)

        try:
            e1.delete (0, END)
            e1.insert (END, sd[1])
            e2.delete (0, END)
            e2.insert (END, sd[2])
            e3.delete (0, END)
            e3.insert (END, sd[3])
            e4.delete (0, END)
            e4.insert (END, sd[4])
            e5.delete (0, END)
            e5.insert (END, sd[5])
            e6.delete (0, END)
            e6.insert (END, sd[6])
            e7.delete (0, END)
            e7.insert (END, sd[7])

        except IndexError:
            pass

    def clearData():
        e1.delete (0, END)
        e2.delete (0, END)
        e3.delete (0, END)
        e4.delete (0, END)
        e5.delete (0, END)
        e6.delete (0, END)
        e7.delete (0, END)

    def addData():
        if (len (e1.get ())) != 0:
            update_info (House_No.get (), Name.get (), Years.get (), Month.get (), Rent.get (),Electricity.get(), Garbage.get())
            Tenantlist.delete (0, END)
            Tenantlist.insert (END, (House_No.get (), Name.get (), Years.get (), Month.get (), Rent.get (),Electricity.get(), Garbage.get()))

    def deleteData():
        global sd
        if (len (e1.get ())) != 0:
            deleteRec (sd[0])
            clearData ()
            DisplayData ()

    def update():
        global sd
        if (len (e1.get ())) != 0:
            deleteRec (sd[0])
        if (len (e1.get ())) != 0:
            update_info (House_No.get (), Name.get (), Years.get (), Month.get (), Rent.get (),Electricity.get(), Garbage.get())
            Tenantlist.delete (0, END)
            Tenantlist.insert (END, House_No.get (), Name.get (), Years.get (), Month.get (), Rent.get (),Electricity.get(), Garbage.get())
    def Total_Rent():
        try:
            Total=float(e7.get())+float(e6.get())+float(e5.get())
            l11= Label (view, text=Total, font=("Lucida calligraphy", 14, "bold"), bd=15,bg='grey')
            l11.grid (row=7, column=1)
        except ValueError:
            pass
    l1 = Label (view, text="House Number:", font=("lucida calligraphy", 15, "bold"), bd=15,bg='grey')
    l1.grid (row=0, column=0 ,sticky='e')
    e1 = Entry (view, bd=10, textvariable=House_No)
    e1.grid (row=0, column=1)
    e1.bind("<KeyRelease>",caps)

    l2 = Label (view, text="Tenant:", font=("Lucida calligraphy", 15, "bold"), bd=15,bg='grey')
    l2.grid (row=1, column=0 ,sticky='e')
    e2 = Entry (view, bd=10, textvariable=Name)
    e2.grid (row=1, column=1)
    e2.bind ("<KeyRelease>", caps)
    l3 = Label (view, text="Year:", font=("Lucida calligraphy", 15, "bold"), bd=15,bg='grey')
    l3.grid (row=2, column=0,sticky='e')
    e3 = Entry (view, bd=10, textvariable=Years)
    e3.grid (row=2, column=1)
    l4 = Label (view, text="Month:", font=("Lucida calligraphy", 15, "bold"), bd=15,bg='grey')
    l4.grid (row=3, column=0,sticky='e')
    e4 = Entry (view, bd=10, textvariable=Month)
    e4.grid (row=3, column=1)
    e4.bind ("<KeyRelease>", caps)
    l5 = Label (view, text="Rent:", font=("Lucida calligraphy", 15, "bold"), bd=15,bg='grey')
    l5.grid (row=4, column=0,sticky='e')
    e5 = Entry (view, bd=10, textvariable=Rent)
    e5.grid (row=4, column=1)
    l6 = Label (view, text="Electicity Bill:", font=("Lucida calligraphy", 15, "bold"), bd=15,bg='grey')
    l6.grid (row=5, column=0,sticky='e')
    e6 = Entry (view, bd=10, textvariable=Electricity)
    e6.grid (row=5, column=1)
    l7 = Label (view, text="Garbage Bill:", font=("Lucida calligraphy",15, "bold"), bd=15,bg='grey')
    l7.grid (row=6, column=0,sticky='e')
    e7 = Entry (view, bd=10, textvariable=Garbage)
    e7.grid (row=6, column=1)
    b8 = Button (view, text="TOTAL RENT =", relief=RAISED, bd=10, command=lambda: Total_Rent ())
    b8.grid (row=7, column=0, padx=10, pady=5)


    f1=Frame(view,bd=10)
    f1.grid(row=1,column=7, rowspan=5,columnspan=6,padx=5, pady=5)
    scrollbar = Scrollbar (f1)
    scrollbar.grid (row=0, column=1, sticky='ns')
    Tenantlist = Listbox (f1, width=50, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
    Tenantlist.bind ('<<ListboxSelect>>', TenantsRec)
    Tenantlist.grid (row=0, column=0, padx=8)
    scrollbar.configure (command=Tenantlist.yview)

    b1 = Button (view, text="EXTRACT", relief=RAISED, bd=10, command=lambda: DisplayData ())
    b1.grid (row=9, column=2, padx=10, pady=5)
    b2 = Button (view, text="BACK", relief=RAISED, bd=10, command=lambda: view.destroy ())
    b2.grid (row=9, column=4, padx=10, pady=5)
    b4 = Button (view, text="INSERT", relief=RAISED, bd=10, command=lambda: addData ())
    b4.grid (row=8, column=1, padx=10, pady=5)
    b5 = Button (view, text="UPDATE", relief=RAISED, bd=10, command=lambda: update ())
    b5.grid (row=8, column=2, padx=10, pady=5)
    b6 = Button (view, text="DELETE", relief=RAISED, bd=10, command=lambda: deleteData ())
    b6.grid (row=9, column=1, padx=10, pady=5)

    b7 = Button (view, text="SEARCH", relief=RAISED, bd=10, command=lambda: searchDb ())
    b7.grid (row=8, column=3, padx=10, pady=5)
    b8 = Button (view, text="CLEAR", relief=RAISED, bd=10, command=lambda: clearData ())
    b8.grid (row=9, column=3, padx=10, pady=5)

    l9 = Label (view, text=('Today:''\t'+today), fg='black', font=('arial', 15, 'bold'),bg='grey')
    l9.grid (row=0, column=7)


# home page
home = Tk ()
home.title ("Landlord App")



image=Image.open('C:\\Users\\BEATRICE\\Desktop\\sams\\SERENE APPARTMENTS\\images.jpg')
newImage=image.resize((1500,1500))
newImage.save('image1200.jpg')
render = ImageTk.PhotoImage(newImage)
l1=Label(home,image=render,bd=0)
l1.image=render

l1.place(x=0, y=0, relwidth=1, relheight=1, relx=.5, rely=.5, anchor='center')
l1.lower()


photo = PhotoImage (file="Landlord icon.ico")
home.iconphoto (False, photo)
home.geometry ("1350x750+0+0" )
l8 = Label (home, text='SERENE APPARTMENT', fg='black', font=('Lucida handwriting', 30, 'bold'),bg='grey')
l8.pack (side='top')
l9 = Label (home, text='HOME', fg='black', font=('arial', 24, 'bold', 'underline'),bg='grey')
l9.pack (side='top')
b3 = Button (home, text="DATABASE", relief=RAISED, bd=10, command=lambda: view_pg ())
b3.pack (side='top', padx=20, pady=10)
bu1 = Button (home, text="EXIT", relief=RAISED, bd=10, command=lambda: exit ())
bu1.pack (side='top', padx=20, pady=10)

home.mainloop ()
