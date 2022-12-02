import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from tkinter import messagebox

# replace with your own local database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password='StAnLoOnA5',
    database='clothingStore'
)

dbCursor = db_connection.cursor()

# ------Titled Window------ #
window = tk.Tk()  # Window Creation
window.title("Database CRUD Application - Clothing Store")  # Titling Window
window.geometry("750x500")

# ------Title-------
cFrame = tk.Frame(window, bg="#274D8B")
cLabel = tk.Label(cFrame, text="Clothing Store", bg="#274D8B", font=("Arial", 20, "bold"), fg="white").pack(pady=5,
                                                                                                            padx=5)
cFrame.pack(side="top", fill='x')

# ---- Tabs -----
nb = ttk.Notebook(window, width=700, height=450)
nb.pack(pady=5, expand=True)

# create tabs
tab1 = tk.Frame(nb)
tab2 = tk.Frame(nb)
tab3 = tk.Frame(nb)
tab4 = tk.Frame(nb)
tab5 = tk.Frame(nb)

# ---- TAB CONTENT ----
# Each tab is divided into two equal parts: left and right. Left can be used for text entry, buttons, filters, etc.
# Right can be used to output a table or a result message box



# ---- Create New Record (Tab 1) ----
tab1left = tk.Frame(tab1, width=350)
tab1right = tk.Frame(tab1, width=350)
tab1left.pack(side='left', expand=True, fill='both')
tab1right.pack(side='left', expand=True, fill='both')

#Gain Entries for Clothing Addition
tab1title=tk.Label(tab1left, text="Add Clothing", font=('Arial', 14, 'bold')).pack(anchor='nw', padx=5, pady=10)
allTab1Entries= tk.Frame(tab1left)
allTab1Entries.pack(side='top', pady=10)

tab1Frame1 = tk.Frame(allTab1Entries)
productType = tk.Label(tab1Frame1, text="Product Type", font=('Arial',12)).pack(side='left')
prodTypeEntry = tk.Entry(tab1Frame1, width=20)
prodTypeEntry.pack(side='left')
tab1Frame1.pack(side='top', pady=10)

tab1Frame2 = tk.Frame(allTab1Entries)
suppID = tk.Label(tab1Frame2, text="Supplier ID ", font=('Arial',12)).pack(side='left')
suppIDEntry = tk.Entry(tab1Frame2, width=20)
suppIDEntry.pack(side='left')
tab1Frame2.pack(side='top', pady=10)

tab1Frame3 = tk.Frame(allTab1Entries)
sizeLabel = tk.Label(tab1Frame3, text="Size ", font=('Arial',12)).pack(side='left')
sizeEntry = tk.Entry(tab1Frame3, width=20)
sizeEntry.pack(side='left')
tab1Frame3.pack(side='top', pady=10)

tab1Frame4 = tk.Frame(allTab1Entries)
materialLabel = tk.Label(tab1Frame4, text="Material ", font=('Arial',12)).pack(side='left')
materialEntry = tk.Entry(tab1Frame4, width=20)
materialEntry.pack(side='left')
tab1Frame4.pack(side='top', pady=10)

tab1Frame5 = tk.Frame(allTab1Entries)
priceLabel = tk.Label(tab1Frame5, text="Price ", font=('Arial',12)).pack(side='left')
priceEntry = tk.Entry(tab1Frame5, width=20)
priceEntry.pack(side='left')
tab1Frame5.pack(side='top', pady=10)

tab1title = tk.Label(tab1right, text="Results", font=('Arial', 16, 'bold')).pack(side='top', anchor='nw', padx=10, pady=10)
tab1headers = tk.Frame(tab1right, padx=110)
col11 = tk.Entry(tab1headers,bg='#89CFF0',width=10)
col11.grid(row=0, column=0)
col11.insert(tk.END, "Type")
col12 = tk.Entry(tab1headers,bg='#89CFF0',width=10)
col12.grid(row=0, column=1)
col12.insert(tk.END, "SupplierID")
col13 = tk.Entry(tab1headers,bg='#89CFF0', width=10)
col13.grid(row=0, column=2)
col13.insert(tk.END, "Size")
col14 = tk.Entry(tab1headers,bg='#89CFF0', width=10)
col14.grid(row=0, column=3)
col14.insert(tk.END, "Material")
col15 = tk.Entry(tab1headers, bg='#89CFF0', width=10)
col15.grid(row=0, column=4)
col15.insert(tk.END, "Price")
tab1headers.pack(side='top')

tableFrameTab1 = tk.Frame(tab1right)
tableFrameTab1.pack(side='top')
#generate first instance of table
dbCursor.execute("SELECT * FROM Product")
i = 0
for product in dbCursor:
    for j in range(len(product)):
        e = tk.Entry(tableFrameTab1, width=(len(product) + 4))
        e.grid(row=i, column=j)
        e.insert(tk.END, product[j])
    i = i + 1

# generate Product table
def showProductTable(tableFrameTab1):
    dbCursor.execute("SELECT * FROM Product")
    i = 0
    for product in dbCursor:
        for j in range(len(product)):
            e = tk.Entry(tableFrameTab1, width=(len(product) + 4))
            e.grid(row=i, column=j)
            e.insert(tk.END, product[j])
        i = i + 1
    tableFrameTab1.update()

#Add Product Entry to Product Table
def addProduct():
    # make sure customer ID has been entered
    
    upQuery = "INSERT INTO Product (Type, SupplierID, Size, Material, Price) VALUES "
    entries = [prodTypeEntry.get(), suppIDEntry.get(), sizeEntry.get(), materialEntry.get(), priceEntry.get()]

    if (not (prodTypeEntry.get() and suppIDEntry.get() and sizeEntry.get() and materialEntry.get() and priceEntry.get())):
        messagebox.showinfo("Request not complete", "Please enter all fields")
        return

    upQuery += '("' + prodTypeEntry.get() + '","' + suppIDEntry.get() + '","' + sizeEntry.get() + '","' + materialEntry.get() + '","' + priceEntry.get() + '")'
    print(upQuery)
    dbCursor.execute(upQuery)
    db_connection.commit()  # NEED THIS IN ORDER TO ACTUALLY UPDATE CHANGES INTO DATABASE
    showProductTable(tableFrameTab1)

#Add Clothing Button
tab1Btn = tk.Button(tab1left, command=lambda: addProduct(), text="Add Clothing", bg='#274D8B', fg='white',
                    font=('Arial', 14, 'bold')).pack(side='top', anchor='nw', padx=10, pady=10)













# ---- Read (Tab 2) ----
tab2left = tk.Frame(tab2, width=350)
tab2right = tk.Frame(tab2, width=350)
tab2left.pack(side='left', expand=True, fill='both')
tab2right.pack(side='left', expand=True, fill='both')

tab2title=tk.Label(tab2left, text="Enter Filter Criteria", font=('Arial',14,'bold')).pack(anchor='nw', padx=5, pady=10)
allTab2Entries = tk.Frame(tab2left)
allTab2Entries.pack(side='top', pady=10)

tab2Frame1=tk.Frame(allTab2Entries)
supplierID = tk.Label(tab2Frame1, text="Supplier ID", font=('Arial', 12)).pack(side='left')
supplierIDEntry = tk.Entry(tab2Frame1, width=20)
supplierIDEntry.pack(side='left')
tab2Frame1.pack(side='top', pady=10)

tab2Frame2=tk.Frame(allTab2Entries)
supplierName = tk.Label(tab2Frame2, text="Supplier Name", font=('Arial', 12)).pack(side='left')
supplierNameEntry = tk.Entry(tab2Frame2, width=20)
supplierNameEntry.pack(side='left')
tab2Frame2.pack(side='top', pady=10)



tab2title = tk.Label(tab2right, text="Results", font=('Arial', 16, 'bold')).pack(side='top', anchor='nw', padx=1, pady=1)
tab2headers = tk.Frame(tab2right, padx=30)
col21 = tk.Entry(tab2headers,bg='#89CFF0',width=4)
col21.grid(row=0, column=0)
col21.insert(tk.END, "Type")
col22 = tk.Entry(tab2headers,bg='#89CFF0',width=10)
col22.grid(row=0, column=1)
col22.insert(tk.END, "SupplierID")
col23 = tk.Entry(tab2headers,bg='#89CFF0', width=4)
col23.grid(row=0, column=2)
col23.insert(tk.END, "Size")
col24 = tk.Entry(tab2headers,bg='#89CFF0', width=7)
col24.grid(row=0, column=3)
col24.insert(tk.END, "Material")
col25 = tk.Entry(tab2headers, bg='#89CFF0', width=5)
col25.grid(row=0, column=4)
col25.insert(tk.END, "Price")
tab2headers.pack(side='top')

tab2headers2 = tk.Frame(tab2right, padx=30)
col212 = tk.Entry(tab2headers2,bg='#89CFF0',width=15)
col212.grid(row=0, column=0)
col212.insert(tk.END, "Supplier Name")
col222 = tk.Entry(tab2headers2,bg='#89CFF0',width=10)
col222.grid(row=0, column=1)
col222.insert(tk.END, "Address")
col232 = tk.Entry(tab2headers2,bg='#89CFF0', width=15)
col232.grid(row=0, column=2)
col232.insert(tk.END, "# of Products")
tableFrameTab2 = tk.Frame(tab2right)
tableFrameTab2.pack(side='top')
tab2headers2.pack(side='right')

#Find Products with Supplier ID Entry
def selectProducts():
    if not supplierIDEntry.get():
        messagebox.showinfo("Request not complete", "Please enter Supplier ID")
        return
    upQuery = "SELECT * FROM Product WHERE supplierID=%s" % (supplierIDEntry.get())
    print(upQuery)
    dbCursor.execute(upQuery)
    i = 0
    for product in dbCursor:
        for j in range(len(product)):
            e = tk.Entry(tableFrameTab2, width=(len(product)))
            e.grid(row=i, column=j)
            e.insert(tk.END, product[j])
        i = i + 1
    tableFrameTab2.update()
    
    db_connection.commit() #NEEDED TO MAKE ACTUAL CHANGES TO DATABASE

tab2Btn1 = tk.Button(tab2Frame1, command=lambda: selectProducts(), text="List Products From Supplier", bg="#274D8B", fg='white', font=('Arial', 8, 'bold')).pack(side='left', anchor='nw', padx=5, pady=5)

def displaySupplierInfo():
    if not supplierNameEntry.get():
        messagebox.showinfo("Request not complete", "Please enter Supplier Name")
        return
    upQuery = "SELECT * FROM Suppliers WHERE supplierName=%s" % (supplierNameEntry.get())
    print(upQuery)
    dbCursor.execute(upQuery)
    i = 0
    for supplier in dbCursor:
        for j in range(len(supplier)):
            e = tk.Entry(tableFrameTab2, width=(len(supplier)))
            e.grid(row=i, column=j)
            e.insert(tk.END, supplier[j])
        i = i + 1
    tableFrameTab2.update()
    
    db_connection.commit() #NEEDED TO MAKE ACTUAL CHANGES TO DATABASE

tab2Btn2 = tk.Button(tab2Frame2, command=lambda: displaySupplierInfo(), text="List Supplier Info", bg="#274D8B", fg='white', font=('Arial', 8, 'bold')).pack(side='left', anchor='nw', padx=5, pady=5)

# ---- Update Customer Info (Tab 3) ----
tab3left = tk.Frame(tab3, width=300)
tab3right = tk.Frame(tab3, width=400)
tab3left.pack(side='left', expand=True, fill='both')
tab3right.pack(side='left', expand=True, fill='both')

# left side
tab3title = tk.Label(tab3left, text="Update customer info", font=('Arial', 14, 'bold')).pack(anchor='nw', padx=5,
                                                                                             pady=10)

allLabelEntries = tk.Frame(tab3left)
allLabelEntries.pack(side='top', anchor='nw')

tab3Frame1 = tk.Frame(allLabelEntries)
custIDLabel = tk.Label(tab3Frame1, text="CustomerID *", font=('Arial',12)).pack(side='left')
custIDEntry = tk.Entry(tab3Frame1, width=20)
custIDEntry.pack(side='left')
tab3Frame1.pack(side='top', pady=10)

tab3Frame2 = tk.Frame(allLabelEntries)
firstnameLabel = tk.Label(tab3Frame2, text="First name ", font=('Arial',12)).pack(side='left')
firstnameEntry = tk.Entry(tab3Frame2, width=20)
firstnameEntry.pack(side='left')
tab3Frame2.pack(side='top', pady=10)

tab3Frame3 = tk.Frame(allLabelEntries)
lastnameLabel = tk.Label(tab3Frame3, text="Last name ", font=('Arial',12)).pack(side='left')
lastnameEntry = tk.Entry(tab3Frame3, width=20)
lastnameEntry.pack(side='left')
tab3Frame3.pack(side='top', pady=10)

tab3Frame4 = tk.Frame(allLabelEntries)
addressLabel = tk.Label(tab3Frame4, text="Address ", font=('Arial',12)).pack(side='left')
addressEntry = tk.Entry(tab3Frame4, width=20)
addressEntry.pack(side='left')
tab3Frame4.pack(side='top', pady=10)

tab3title = tk.Label(tab3right, text="Results", font=('Arial', 16, 'bold')).pack(side='top', anchor='nw', padx=10, pady=10)
tab3headers = tk.Frame(tab3right, padx=10)
col1 = tk.Entry(tab3headers,bg='#89CFF0',width=18)
col1.grid(row=0, column=0)
col1.insert(tk.END, "CustomerID")
col2 = tk.Entry(tab3headers,bg='#89CFF0',width=18)
col2.grid(row=0, column=1)
col2.insert(tk.END, "FirstName")
col3 = tk.Entry(tab3headers,bg='#89CFF0', width=18)
col3.grid(row=0, column=2)
col3.insert(tk.END, "LastName")
col4 = tk.Entry(tab3headers,bg='#89CFF0', width=18)
col4.grid(row=0, column=3)
col4.insert(tk.END, "Address")
tab3headers.pack(side='top')

tableFrameTab3 = tk.Frame(tab3right)
tableFrameTab3.pack(side='top')
#generate first instance of table
dbCursor.execute("SELECT * FROM Customers")
i = 0
for customer in dbCursor:
    for j in range(len(customer)):
        e = tk.Entry(tableFrameTab3, width=(len(customer) + 14))
        e.grid(row=i, column=j)
        e.insert(tk.END, customer[j])
    i = i + 1

# generate customers table
def showCustomersTable(tableFrameTab3):
    dbCursor.execute("SELECT * FROM Customers")
    i = 0
    for customer in dbCursor:
        for j in range(len(customer)):
            e = tk.Entry(tableFrameTab3, width=(len(customer)+14))
            e.grid(row=i, column=j)
            e.insert(tk.END, customer[j])
        i = i + 1
    tableFrameTab3.update()


# update customer info query
def updateInfo(tableFrameTab3):
    # make sure customer ID has been entered
    if not custIDEntry.get():
        messagebox.showinfo("Request not complete", "Please enter an existing customer ID")
        return

    upQuery = "UPDATE Customers SET "
    entries = [firstnameEntry.get(), lastnameEntry.get(), addressEntry.get()]

    if firstnameEntry.get():
        upQuery += 'firstName=\'' + firstnameEntry.get() + '\''
        entries.remove(firstnameEntry.get())
        if not lastnameEntry.get() and not addressEntry.get():
            upQuery += " "
        else:
            upQuery += ", "
    else:
        entries.remove(firstnameEntry.get())

    if lastnameEntry.get():
        upQuery += 'lastName=\'' + lastnameEntry.get() + '\''
        entries.remove(lastnameEntry.get())
        if not addressEntry.get():
            upQuery += " "
        else:
            upQuery += ", "
    else:
        entries.remove(lastnameEntry.get())

    if addressEntry.get():
        upQuery += 'Address=\'' + addressEntry.get() + '\' '
        entries.remove(addressEntry.get())

    upQuery += "WHERE CustomerID=" + str(custIDEntry.get())
    print(upQuery)

    dbCursor.execute(upQuery)
    db_connection.commit()  # NEED THIS IN ORDER TO ACTUALLY UPDATE CHANGES INTO DATABASE
    showCustomersTable(tableFrameTab3)

tab3Btn = tk.Button(tab3left, command=lambda: updateInfo(tableFrameTab3), text="Save changes", bg='#274D8B', fg='white',
                    font=('Arial', 14, 'bold')).pack(side='top', anchor='nw', padx=10, pady=10)
















# ---- Delete orders (Tab 4) ----
tab4left = tk.Frame(tab4, width=350)
tab4right = tk.Frame(tab4, width=350)
tab4left.pack(side='left', expand=True, fill='both')
tab4right.pack(side='left', expand=True, fill='both')

# left side
tab4title = tk.Label(tab4left, text="Delete orders", font=('Arial', 16, 'bold')).pack(anchor='nw', padx=10, pady=10)

allLabelEntries = tk.Frame(tab4left)
allLabelEntries.pack(side='top', anchor='nw', padx=10)

tab4Frame1 = tk.Frame(allLabelEntries)
orderIDLabel = tk.Label(tab4Frame1, text="OrderID ", font=('Arial', 12)).pack(side='left')
orderIDEntry = tk.Entry(tab4Frame1)
orderIDEntry.pack(side='left')
tab4Frame1.pack(side='top', pady=10)

tab4title = tk.Label(tab4right, text="Results", font=('Arial', 16, 'bold')).pack(side='top', anchor='nw', pady=10)
tab4headers = tk.Frame(tab4right, padx=10)
tab4col1 = tk.Entry(tab4headers,bg='#89CFF0',width=18)
tab4col1.grid(row=0, column=0)
tab4col1.insert(tk.END, "OrderID")
tab4col2 = tk.Entry(tab4headers,bg='#89CFF0',width=18)
tab4col2.grid(row=0, column=1)
tab4col2.insert(tk.END, "ProductID")
tab4col3 = tk.Entry(tab4headers,bg='#89CFF0', width=18)
tab4col3.grid(row=0, column=2)
tab4col3.insert(tk.END, "CustomerID")
tab4col4 = tk.Entry(tab4headers,bg='#89CFF0', width=18)
tab4col4.grid(row=0, column=3)
tab4col4.insert(tk.END, "Total")
tab4headers.pack(side='top')

tableFrameTab4 = tk.Frame(tab4right)
tableFrameTab4.pack(side='top')
# generate first instance of table
dbCursor.execute("SELECT * FROM Orders")
i = 0
for order in dbCursor:
    for j in range(len(order)):
        e4 = tk.Entry(tableFrameTab4, width=(len(order) + 14))
        e4.grid(row=i, column=j)
        e4.insert(tk.END, order[j])
    i = i + 1

tableFrameTab4 = tk.Frame(tab4right)
tableFrameTab4.pack(side='top')

# button and button function
def delOrders(tableFrameTab4):
    if not orderIDEntry.get():
        messagebox.showinfo("Request not complete", "Please enter an existing order ID")
        return

    delQuery = ("DELETE FROM orders WHERE OrderID=%s" % orderIDEntry.get())
    print(delQuery)
    dbCursor.execute(delQuery)
    db_connection.commit()
    messagebox.showinfo("Order deleted", "Order has been deleted. Restart the app to see your changes.")

tab4Btn = tk.Button(tab4left, command=lambda: delOrders(tableFrameTab4), text="Delete order", bg='#274D8B', fg='white',
                    font=('Arial', 14, 'bold')).pack(side='top', anchor='nw', padx=10, pady=10)




# ---- Predefined SQL Functions (i.e. Joins, Intersections, etc.)
tab5left = tk.Frame(tab5, width=350)
tab5right = tk.Frame(tab5, width=350)
tab5left.pack(side='left', expand=True, fill='both')
tab5right.pack(side='left', expand=True, fill='both')






# pack each tab
tab1.pack(fill='both', expand=True)
tab2.pack(fill='both', expand=True)
tab3.pack(fill='both', expand=True)
tab4.pack(fill='both', expand=True)
tab5.pack(fill='both', expand=True)

# add tab frames to create notebook
nb.add(tab1, text='Create clothing')
nb.add(tab2, text='Read Supplier''s Info/Products')
nb.add(tab3, text='Update customer info')
nb.add(tab4, text='Delete orders')
nb.add(tab5, text= 'Predefined SQL Functions')

window.mainloop()  # Needed At end of a python file for executable application to properly run
