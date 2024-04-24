# main.py
import sqlite3                    #importing module for performing SQL operations.
from tkinter import *             #importing module for creating GUI
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkcalendar import Calendar, DateEntry
from datetime import *
import pickle

def view_customer(tree): #function to view customer data
    dbfile = open('customer', 'rb')
    file_data = []
    while True:
        try:
            file_data.append(pickle.load(dbfile ))
        except EOFError:
            break
    dbfile.close()

    for row in tree.get_children(): #clear tree data
        tree.delete(row)

    for x in file_data:
        tree.insert("", 'end', values=(x['phone'], x['name'],x['gender']))


def add_customer(child_window,tree,name_entry, phone_entry, gender_entry):  #function to insert into customer
    if len(name_entry.get())==0 or len(phone_entry.get())==0 or len(gender_entry.get())==0:
        messagebox.showwarning("Error","Enter name,phone and gender",parent=child_window)
    else:
        custdb = {}
        dbfile = open('customer', 'ab')
        d1 = {'phone': phone_entry.get(), 'name': name_entry.get(),
                  'gender': gender_entry.get()}
        d1[phone_entry.get()]=phone_entry.get()
        pickle.dump(d1, dbfile)
        dbfile.close()
        view_customer(tree)
        name_entry.set("")
        phone_entry.set("")
        gender_entry.set("Male")

def delete_customer(child_window,tree): #function to delete customer
    i=tree.set(tree.focus(), column="#1")
    if len(i)==0:
        messagebox.showerror("Error","Select Customer",parent=child_window)
    else:
        dbfile = open("customer", 'rb+')
        file_data = []

        while True:
            try:
                L1 = pickle.load(dbfile)

                if (L1['phone'] != i):
                    file_data.append(L1)
            except EOFError:
                messagebox.showinfo("Status","Deleted",parent=child_window)
                break

        dbfile.seek(0)
        dbfile.truncate()

        for i in range(len(file_data)):
            pickle.dump(file_data[i], dbfile)
        dbfile.close()
        view_customer(tree)

def customer_form(window): #function to define customer form

    child_window= Toplevel(window)
    child_window.title("Customer Master")
    l1 = Label(child_window, text="Name")
    l1.grid(row=0, column=0)

    l2 = Label(child_window, text="Phone")
    l2.grid(row=1, column=0)

    l3 = Label(child_window, text="Gender")
    l3.grid(row=2, column=0)

    name_entry = StringVar()
    e1 = Entry(child_window, textvariable=name_entry)
    e1.grid(row=0, column=1)

    phone_entry = StringVar()
    e2 = Entry(child_window, textvariable=phone_entry)
    e2.grid(row=1, column=1)

    gender_options=['Male', 'Female', 'Transgender']
    gender_entry = StringVar()
    e3= OptionMenu(child_window, gender_entry, *gender_options)
    gender_entry.set("Male")
    e3.grid(row=2, column=1)

    tree = Treeview(child_window, column=("Phone", "Name", "Gender"), show='headings')
    tree.heading("#1", text="Phone")
    tree.heading("#2", text="Name")
    tree.heading("#3", text="Gender")
    tree.grid(row=4,column=0,rowspan=12,columnspan=2)

    button_view = Button(child_window, text="View all", width=12, command=lambda: view_customer(tree))
    button_view.grid(row=3, column=3)
    button_add = Button(child_window, text="Add Customer", width=12, command=lambda: add_customer(child_window,tree,name_entry, phone_entry, gender_entry))
    button_add.grid(row=5, column=3)

    button_del = Button(child_window, text="Delete Customer", width=12,command= lambda: delete_customer(child_window,tree))
    button_del.grid(row=9, column=3)

def view_hotel(tree):#function to view data of hotel
    dbfile = open('hotel', 'rb')
    file_data = []
    while True:
        try:
            file_data.append(pickle.load(dbfile))
        except EOFError:
            break
    dbfile.close()

    for row in tree.get_children():  # clear tree data
        tree.delete(row)

    for x in file_data:
        tree.insert("", 'end', values=(x['name'], x['city'], x['contact'],x['rooms']))

def add_hotel(child_window,tree,name_entry, city_entry, contact_entry,rooms_entry):#function to add hotel
    if len(name_entry.get())==0 or len(contact_entry.get())==0 or len(rooms_entry.get())==0:
        messagebox.showinfo("Error","Enter name,contact and number of rooms",parent=child_window)
    else:
        hoteldb  = {}
        dbfile = open('hotel', 'ab')
        d1 = {'name': name_entry.get(), 'city': city_entry.get(),
              'contact': contact_entry.get(),'rooms':rooms_entry.get()}
        d1[name_entry.get()] = name_entry.get()
        pickle.dump(d1, dbfile)
        dbfile.close()
        view_hotel(tree)
        name_entry.set("")
        city_entry.set("")
        contact_entry.set("")
        rooms_entry.set("")
        messagebox.showinfo("Status","Added",parent=child_window)

def delete_hotel(child_window,tree): #function to delete hotel
    i=tree.set(tree.focus(), column="#1")
    if len(i)==0:
            messagebox.showinfo("Error","Select Hotel",parent=child_window)
    else:
        dbfile = open("hotel", 'rb+')
        file_data = []

        while True:
            try:
                L1 = []
                L1 = pickle.load(dbfile)
                print(L1['name'])

                if (L1['name'] != i):
                    file_data.append(L1)
            except EOFError:
                messagebox.showinfo("Status","Deleted",parent=child_window)
                break

        dbfile.seek(0)
        dbfile.truncate()

        for i in range(len(file_data)):
            pickle.dump(file_data[i], dbfile)
        else:
            dbfile.close()

        view_hotel(tree)

def hotel_form(window):#function to define hotel form
    child_window= Toplevel(window)
    child_window.title("Hotel Master")
    l1 = Label(child_window, text="Name")
    l1.grid(row=0, column=0)

    l2 = Label(child_window, text="City")
    l2.grid(row=1, column=0)

    l3 = Label(child_window, text="Contact")
    l3.grid(row=2, column=0)

    l4 = Label(child_window, text="Rooms")
    l4.grid(row=3, column=0)

    name_entry = StringVar()
    e1 = Entry(child_window, textvariable=name_entry)
    e1.grid(row=0, column=1)

    city_entry = StringVar()
    e2 = Entry(child_window, textvariable=city_entry)
    e2.grid(row=1, column=1)

    contact_entry = StringVar()
    e2 = Entry(child_window, textvariable=contact_entry)
    e2.grid(row=2, column=1)

    rooms_entry = StringVar()
    e2 = Entry(child_window, textvariable =rooms_entry)
    e2.grid(row=3, column=1)

    tree = Treeview(child_window, column=( "Name", "City","Contact", "Rooms"), show='headings')
    tree.heading("#1", text="Name")
    tree.heading("#2", text="City")
    tree.heading("#3", text="Contact")
    tree.heading("#4", text="No of Rooms")
    tree.grid(row=5, column=0, rowspan=6, columnspan=2)

    button_view = Button(child_window, text="View all", width=12, command=lambda: view_hotel(tree))
    button_view.grid(row=6, column=3)

    button_add = Button(child_window, text="Add Hotel", width=12, command=lambda: add_hotel(child_window,tree,name_entry, city_entry, contact_entry,rooms_entry))
    button_add.grid(row=7, column=3)

    button_del = Button(child_window, text="Delete Hotel", width=12,command= lambda: delete_hotel(child_window,tree))
    button_del.grid(row=8, column=3)

def view_booking(tree): #function to view bookings
    dbfile = open('booking', 'rb')
    file_data = []
    while True:
        try:
            file_data.append(pickle.load(dbfile))
        except EOFError:
            break
    dbfile.close()

    for row in tree.get_children():  # clear tree data
        tree.delete(row)

    for x in file_data:
        tree.insert("", 'end', values=(x['Hotel'], x['Customer'], x['DateFrom'], x['DateTo'], x['Rooms'],x['Rating']))

def add_booking(child_window,tree,hotelid,customerid, datefrom,dateto,rooms):  #function to add bookings
    if len(hotelid) == 0 or len(customerid) == 0 or len(datefrom) == 0 or len(dateto) == 0 or len(rooms) == 0:
        messagebox.showwarning("Error", "Select Hotel,Customer,DateFrom,DateTo,Rooms", parent=child_window)
    else:
        bookingdb = {}
        dbfile = open('booking', 'ab')
        d1 = {'Hotel': hotelid, 'Customer':customerid,
              'DateFrom': datefrom, 'DateTo': dateto ,'Rooms':rooms,'Rating':"-"}
        pickle.dump(d1, dbfile)
        dbfile.close()

        view_booking(tree)
        hotelid.set("")
        customerid.set("")
        datefrom.set("")
        dateto.set("")
        rooms.set("")
        view_booking(tree)
        messagebox.showinfo("Status","Added",parent=child_window)

def delete_booking(child_window,tree): #function to delete bookings
    cust=tree.set(tree.focus(), column="#2")
    hotel=tree.set(tree.focus(), column="#1")
    dt = tree.set(tree.focus(), column="#3")
    if len(cust)==0:
        messagebox.showinfo("Error","Select booking",parent=child_window)
    else:
        dbfile = open("booking", 'rb+')
        file_data = []

        while True:
            try:
                L1 = []
                L1 = pickle.load(dbfile)
                if not (L1['Hotel'] == hotel and L1['Customer']  == cust and L1['DateFrom'] == dt):
                    file_data.append(L1)
            except EOFError:
                break

        dbfile.seek(0)
        dbfile.truncate()

        for i in range(len(file_data)):
            pickle.dump(file_data[i], dbfile)
        else:
            dbfile.close()

        view_booking(tree)

def save_rating(child_window,tree,customerrating): #function to delete bookings
    cust=tree.set(tree.focus(), column="#2")
    hotel=tree.set(tree.focus(), column="#1")
    dt = tree.set(tree.focus(), column="#3")
    if len(cust)==0:
        messagebox.showinfo("Error","Select booking",parent=child_window)
    else:
        dbfile = open("booking", 'rb+')
        file_data = []

        while True:
            try:

                L1 = pickle.load(dbfile)
                if (L1['Hotel'] == hotel and L1['Customer'] == cust and L1['DateFrom'] == dt):
                    L1['Rating']=customerrating
                    file_data.append(L1)
                else:
                    file_data.append(L1)
            except EOFError:
                messagebox.showinfo("Status", "Rating Updated",parent=child_window)
                break

        dbfile.seek(0)
        dbfile.truncate()

        for i in range(len(file_data)):
            pickle.dump(file_data[i], dbfile)
        else:
            dbfile.close()

        view_booking(tree)


def booking_form(window):#function to define booking form
    child_window= Toplevel(window)
    l1 = Label(child_window, text="Hotel")
    l1.grid(row=0, column=0)

    dbfile = open('hotel', 'rb')
    file_data = []
    while True:
        try:
            file_data.append(pickle.load(dbfile))
        except EOFError:
            break
    dbfile.close()

    hotel_list = []
    for x in file_data:
        data="%s, " % (x['name'])
        hotel_list.append(data)
    hotel_id = StringVar()
    e1 = OptionMenu(child_window, hotel_id, *hotel_list)
    e1.grid(row=0, column=1)
    l2 = Label(child_window, text="Customer")
    l2.grid(row=1, column=0)
    customer_list= []
    dbfile = open('customer', 'rb')
    file_data = []
    while True:
        try:
            file_data.append(pickle.load(dbfile))
        except EOFError:
            break
    dbfile.close()

    for x in file_data:
        data = "%s, " % (x['name'])
        customer_list.append(data)

    customer_id = StringVar()
    e2 = OptionMenu(child_window, customer_id, *customer_list)
    e2.grid(row=1, column=1)

    l3 = Label(child_window, text="No of Rooms")
    l3.grid(row=2, column=0)

    rooms= StringVar()
    e3 = Entry(child_window, textvariable =rooms)
    e3.grid(row=2, column=1)

    l4 = Label(child_window, text="Date From")
    l4.grid(row=3, column=0)
    date_from = Calendar(child_window, selectmode='day', year=datetime.today().year, month=datetime.today().month, day=datetime.today().day)
    date_from.grid(row=3, column=1)

    l5 = Label(child_window, text="Date To")
    l5.grid(row=4, column=0)

    date_to = Calendar(child_window, selectmode='day', year=datetime.today().year, month=datetime.today().month, day=datetime.today().day)
    date_to.grid(row=4, column=1)

    tree = Treeview(child_window, column=("Hotel", "Customer", "Datefrom", "Dateto", "Rooms", "Rating"),show='headings')
    tree.heading("#1", text="Hotel ID")
    tree.heading("#2", text="Customer")
    tree.heading("#3", text="Date From")
    tree.heading("#4", text="Date To")
    tree.heading("#5", text="No of Rooms")
    tree.heading("#6", text="Rating")

    tree.grid(row=3, column=2, rowspan=10, columnspan=6)

    button_view = Button(child_window, text="View all", width=12, command=lambda: view_booking(tree))
    button_view.grid(row=6, column=2)

    button_add = Button(child_window, text="Add Booking", width=12,
                        command=lambda: add_booking(child_window,tree, hotel_id.get(), customer_id.get(),
                                                    date_from.get_date(), date_to.get_date(), rooms.get()))
    button_add.grid(row=6, column=3)

    button_del = Button(child_window, text="Delete Booking", width=12, command=lambda: delete_booking(child_window,tree))
    button_del.grid(row=6, column=4)

    l6 = Label(child_window, text="Rating")
    l6.grid(row=5, column=5)

    rating = []
    for i in range(1, 6):
        data = (i * '*')
        rating.append(data)
    customerrating = StringVar()
    e6 = OptionMenu(child_window, customerrating, *rating)
    e6.grid(row=6, column=5)
    button_rating = Button(child_window, text="Rate Booking", width=12, command=lambda: save_rating(child_window,   tree, customerrating.get()))
    button_rating.grid(row=6, column=6)


window = Tk() #using Tkinter module, create a GUI window
window.title("Hotel Bookings") #setting title of the window

header = Label(window, text="HOTEL BOOKING SYSTEM")
header.grid(row=1, column=3)

photo = PhotoImage(file = "logo.png")

b2 = Button(window, image=photo)
b2.grid(row=2, column=3)
b1 = Button(window, text="Customer Master", width=15, command=lambda: customer_form(window))
b1.grid(row=4, column=3)

b2 = Button(window, text="Hotel Master", width=15, command=lambda: hotel_form(window))
b2.grid(row=6, column=3)
b3 = Button(window, text="Booking", width=15,  command=lambda: booking_form(window))
b3.grid(row=8, column=3)
#b4 = Button(window, text="Report", width=15, command=lambda:show_report(window))
#b4.grid(row=10, column=3)
b6 = Button(window, text="Close",foreground ="Red", width=15, command= window.destroy)
b6.grid(row=12, column=3)

window.mainloop()