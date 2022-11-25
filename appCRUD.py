import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector


# db_connection = mysql.connector.connect(
# host="",
# user="",
# password="",
# database="mydatabase"
# )

# dbCursor = db_connection.cursor()


# ######------REFERENCES-------#######
# ------Widget------#
# label=tk.Label(
#    text="Hello, tkinter",
#    foreground="white", #Set Text Color to White  ----Many HTML Colors Work
#    background="black", #Set Background Color to Black ---- background="XXYYZZ" rgb option available
#    width=10, #Can control Width and Height of Label
#    height=10
#    )
# label.pack() #Adds Widget to Window

# ------Clickable Button------#
# button = tk.Button(
#   text="Click me!",
#    width=25,
#    height=5,
#    bg="blue",
#    fg="yellow",
# )
# button.pack() #Adds Button to Window

# ------Entry Widget for User Input------#
# label2=tk.Label(text="Type This")
# entry=tk.Entry()
# label2.pack()
# entry.pack()
# name=entry.get() #grabs user input for entry
# entry.delete(0) #Deletes first character of input for entry
# entry.delete(0,4) #Deletes characters indexed 0 through 4 of input for entry
# entry.delete(0,tk.END) #Deletes all characters
# entry.insert(0, "Python") #Inserts "Python" starting at index 0


# ##---Idea for Utilizing Class in Application---###
# class crudApp(tk.Tk):
#    def __init__(self):
#        super().__init__()
#        self.title("Database CRUD Application")
#        self.geometry("750x500")


# ##------Button Functions------###
# def createTuple():
#     print("Created")
#     # dbCursor.execute("INSERT INTO TABLE")
#
#
# def readTable():
#     print("Read")
#     # dbCursor.execute("SELECT * FROM TABLE")
#
#
# def updateTable():
#     print("Updated")
#     # dbCursor.execute("UPDATE TABLE SET * WHERE *")
#
#
# def deleteRel():
#     print("Deleted")
#     # dbCursor.execute("DELETE FROM TABLE WHERE")


# ------Titled Window------ #
window = tk.Tk()  # Window Creation
window.title("Database CRUD Application - Clothing Store")  # Titling Window
window.geometry("750x500")

###### Labels & Entry ######

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

# ---- TAB CONTENT ----
# Each tab is divided into two equal parts: left and right. Left can be used for text entry, buttons, filters, etc.
# Right can be used to output a table or a result message box

# ---- Tab 1 Content ----
tab1left = tk.Frame(tab1, width=350)
tab1right = tk.Frame(tab1, width=350)
tab1left.pack(side='left', expand=True, fill='both')
tab1right.pack(side='left', expand=True, fill='both')

# ---- Tab 2 Content ----
tab2left = tk.Frame(tab2, width=350)
tab2right = tk.Frame(tab2, width=350)
tab2left.pack(side='left', expand=True, fill='both')
tab2right.pack(side='left', expand=True, fill='both')

# ---- Tab 3 Content ----
tab3left = tk.Frame(tab3, width=350)
tab3right = tk.Frame(tab3, width=350)
tab3left.pack(side='left', expand=True, fill='both')
tab3right.pack(side='left', expand=True, fill='both')

# ---- Tab 4 Content ----
tab4left = tk.Frame(tab4, width=350)
tab4right = tk.Frame(tab4, width=350)
tab4left.pack(side='left', expand=True, fill='both')
tab4right.pack(side='left', expand=True, fill='both')

# pack each tab
tab1.pack(fill='both', expand=True)
tab2.pack(fill='both', expand=True)
tab3.pack(fill='both', expand=True)
tab4.pack(fill='both', expand=True)

# add tab frames to create notebook
nb.add(tab1, text='Create clothing')
nb.add(tab2, text='View suppliers')
nb.add(tab3, text='Update customer info')
nb.add(tab4, text='Delete orders')

# frame1 holds labels and entries
# frame2 holds the buttons
# frame3 holds the results messages or tables, depends on what we want to display
#
# frame1 = tk.Frame(window, height=500, width=250)
# frame2 = tk.Frame(window, height=500, width=250)
# frame3 = tk.Frame(window, highlightbackground="black", highlightthickness=1, height=500, width=250)
# frame1.pack(side='left', anchor='center', fill='both', expand=True)
# frame2.pack(side='left', anchor='center', fill='both', expand=True)
# frame3.pack(side='left', anchor='center', fill='both', expand=True)
#
# # ------Label 1------#
# allLabelEntries = tk.Frame(frame1)
# allLabelEntries.pack(side='left', anchor='center', padx=20)
#
# lFrame1 = tk.Frame(allLabelEntries)
# label1 = tk.Label(lFrame1, text="Label 1", font=(18)).pack(side='left')
# entry1 = tk.Entry(lFrame1).pack(side='left')
# lFrame1.pack(side='top', pady=10)
#
# # ------Label 2------#
# lFrame2 = tk.Frame(allLabelEntries)
# label2 = tk.Label(lFrame2, text="Label 2", font=(18)).pack(side='left')
# entry2 = tk.Entry(lFrame2).pack(side='left')
# lFrame2.pack(side='top', pady=10)
#
# # ------Label 3------#
# lFrame3 = tk.Frame(allLabelEntries)
# label3 = tk.Label(lFrame3, text="Label 3", font=(18)).pack(side='left')
# entry3 = tk.Entry(lFrame3).pack(side='left')
# lFrame3.pack(side='top', pady=10)
#
# # ------Label 4------#
# lFrame4 = tk.Frame(allLabelEntries)
# label4 = tk.Label(lFrame4, text="Label 4", font=(18)).pack(side='left')
# entry4 = tk.Entry(lFrame4).pack(side='left')
# lFrame4.pack(side='top', pady=10)
#
# # ------Label 5------#
# lFrame5 = tk.Frame(allLabelEntries)
# label5 = tk.Label(lFrame5, text="Label 5", font=(18)).pack(side='left')
# entry5 = tk.Entry(lFrame5).pack(side='left')
# lFrame5.pack(side='top', pady=10)
#
# ###### BUTTONS FOR CRUD OPERATIONS ######
# # frame to store all buttons
#
# # ------Create Button------#
# allButtons = tk.Frame(frame2)
# allButtons.pack(side='left', anchor='center', padx=20)
#
# but_create = tk.Button(
#     allButtons,
#     text="CREATE",
#     width=20,
#     height=5,
#     bg="cyan",
#     fg="purple",
#     command=createTuple
# ).pack(pady=10)
#
# # ------Read Button------#
# but_read = tk.Button(
#     allButtons,
#     text="READ",
#     width=20,
#     height=5,
#     bg="cyan",
#     fg="purple",
#     command=readTable
# ).pack(pady=10)
#
# # ------Update Button------#
# but_upd = tk.Button(
#     allButtons,
#     text="UPDATE",
#     width=20,
#     height=5,
#     bg="cyan",
#     fg="purple",
#     command=updateTable
# ).pack(pady=10)
#
# # ------Delete Button------#
# but_del = tk.Button(
#     allButtons,
#     text="DELETE",
#     width=20,
#     height=5,
#     bg="cyan",
#     fg="purple",
#     command=deleteRel
# ).pack(pady=10)

window.mainloop()  # Needed At end of a python file for executable application to properly run
