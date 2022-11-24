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


#######------REFERENCES-------#######
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


###---Idea for Utilizing Class in Application---###
# class crudApp(tk.Tk):
#    def __init__(self):
#        super().__init__()
#        self.title("Database CRUD Application")
#        self.geometry("750x500")

###------Button Functions------###
def createTuple():
    print("Created")
    # dbCursor.execute("INSERT INTO TABLE")


def readTable():
    print("Read")
    # dbCursor.execute("SELECT * FROM TABLE")


def updateTable():
    print("Updated")
    # dbCursor.execute("UPDATE TABLE SET * WHERE *")


def deleteRel():
    print("Deleted")
    # dbCursor.execute("DELETE FROM TABLE WHERE")


# ------Titled Window------#
window = tk.Tk()  # Window Creation
window.title("Database CRUD Application - Clothing Store")  # Titling Window
window.geometry("750x500")

###### Labels & Entry ######
# ------Title-------#
cFrame = tk.Frame(window, bg="#274D8B")
cLabel = tk.Label(cFrame, text="Clothing Store", bg="#274D8B", font=("Arial", 20, "bold"), fg="white").pack(pady=5,
                                                                                                            padx=5)
cFrame.pack(side="top", fill='x')

# frame1 holds labels and entries
# frame2 holds the buttons
# frame3 holds the results messages or tables, depends on what we want to display

frame1 = tk.Frame(window, height=500, width=250)
frame2 = tk.Frame(window, height=500, width=250)
frame3 = tk.Frame(window, highlightbackground="black", highlightthickness=1, height=500, width=250)
frame1.pack(side='left', anchor='center', fill='both', expand=True)
frame2.pack(side='left', anchor='center',  fill='both', expand=True)
frame3.pack(side='left', anchor='center',  fill='both', expand=True)

# ------Label 1------#
allLabelEntries = tk.Frame(frame1)
allLabelEntries.pack(side='left', anchor='center', padx=20)

lFrame1 = tk.Frame(allLabelEntries)
label1 = tk.Label(lFrame1, text="Label 1", font=(18)).pack(side='left')
entry1 = tk.Entry(lFrame1).pack(side='left')
lFrame1.pack(side='top', pady=10)

# ------Label 2------#
lFrame2 = tk.Frame(allLabelEntries)
label2 = tk.Label(lFrame2, text="Label 2", font=(18)).pack(side='left')
entry2 = tk.Entry(lFrame2).pack(side='left')
lFrame2.pack(side='top', pady=10)

# ------Label 3------#
lFrame3 = tk.Frame(allLabelEntries)
label3 = tk.Label(lFrame3, text="Label 3", font=(18)).pack(side='left')
entry3 = tk.Entry(lFrame3).pack(side='left')
lFrame3.pack(side='top', pady=10)

# ------Label 4------#
lFrame4 = tk.Frame(allLabelEntries)
label4 = tk.Label(lFrame4, text="Label 4", font=(18)).pack(side='left')
entry4 = tk.Entry(lFrame4).pack(side='left')
lFrame4.pack(side='top', pady=10)

# ------Label 5------#
lFrame5 = tk.Frame(allLabelEntries)
label5 = tk.Label(lFrame5, text="Label 5", font=(18)).pack(side='left')
entry5 = tk.Entry(lFrame5).pack(side='left')
lFrame5.pack(side='top', pady=10)


###### BUTTONS FOR CRUD OPERATIONS ######
#frame to store all buttons

# ------Create Button------#
allButtons = tk.Frame(frame2)
allButtons.pack(side='left', anchor='center', padx=20)

but_create = tk.Button(
    allButtons,
    text="CREATE",
    width=20,
    height=5,
    bg="cyan",
    fg="purple",
    command=createTuple
).pack(pady=10)

# ------Read Button------#
but_read = tk.Button(
    allButtons,
    text="READ",
    width=20,
    height=5,
    bg="cyan",
    fg="purple",
    command=readTable
).pack(pady=10)

# ------Update Button------#
but_upd = tk.Button(
    allButtons,
    text="UPDATE",
    width=20,
    height=5,
    bg="cyan",
    fg="purple",
    command=updateTable
).pack(pady=10)

# ------Delete Button------#
but_del = tk.Button(
    allButtons,
    text="DELETE",
    width=20,
    height=5,
    bg="cyan",
    fg="purple",
    command=deleteRel
).pack(pady=10)

window.mainloop()  # Needed At end of a python file for executable application to properly run
