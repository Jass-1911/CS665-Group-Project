import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector 
#db_connection = mysql.connector.connect(
    #host="",
    #user="",
    #password="",
    #database="mydatabase"
    # )

#dbCursor = db_connection.cursor()


#######------REFERENCES-------#######
#------Widget------#
#label=tk.Label(
#    text="Hello, tkinter",
#    foreground="white", #Set Text Color to White  ----Many HTML Colors Work
#    background="black", #Set Background Color to Black ---- background="XXYYZZ" rgb option available
#    width=10, #Can control Width and Height of Label
#    height=10
#    )
#label.pack() #Adds Widget to Window

#------Clickable Button------#
#button = tk.Button(
#   text="Click me!",
#    width=25,
#    height=5,
#    bg="blue",
#    fg="yellow",
#)
#button.pack() #Adds Button to Window

#------Entry Widget for User Input------#
#label2=tk.Label(text="Type This")
#entry=tk.Entry()
#label2.pack()
#entry.pack()
#name=entry.get() #grabs user input for entry
#entry.delete(0) #Deletes first character of input for entry
#entry.delete(0,4) #Deletes characters indexed 0 through 4 of input for entry
#entry.delete(0,tk.END) #Deletes all characters
#entry.insert(0, "Python") #Inserts "Python" starting at index 0


###---Idea for Utilizing Class in Application---###
#class crudApp(tk.Tk):
#    def __init__(self):
#        super().__init__()
#        self.title("Database CRUD Application")
#        self.geometry("750x500")

###------Button Functions------###
def createTuple():
    print("created")
    #dbCursor.execute("INSERT INTO TABLE")

def readTable():
    print("Read.")
    #dbCursor.execute("SELECT * FROM TABLE")

def updateTable():
    print("Updated")
    #dbCursor.execute("UPDATE TABLE SET * WHERE *")

def deleteRel():
    print("deleted")
    #dbCursor.execute("DELETE FROM TABLE WHERE")



#------Titled Window------#
window= tk.Tk() #Window Creation
window.title("Database CRUD Application") #Titling Window
window.geometry("750x500") #Window Size

###### Labels & Entry ######

#------Label 1------#
label1 = tk.Label(text="Label 1")
entry1 = tk.Entry()
label1.pack()
entry1.pack()

#------Label 2------#
label2 = tk.Label(text="Label 2")
entry2 = tk.Entry()
label2.pack()
entry2.pack()

#------Label 3------#
label3 = tk.Label(text="Label 3")
entry3 = tk.Entry()
label3.pack()
entry3.pack()

#------Label 4------#
label4 = tk.Label(text="Label 4")
entry4 = tk.Entry()
label4.pack()
entry4.pack()

#------Label 5------#
label5 = tk.Label(text="Label 5")
entry5 = tk.Entry()
label5.pack()
entry5.pack()

###### BUTTONS FOR CRUD OPERATIONS ######

#------Create Button------#
but_create=tk.Button(
    text="CREATE",
    width=30,
    height=5,
    bg="cyan",
    fg="purple",
    command=createTuple
)
but_create.pack()

#------Read Button------#
but_read=tk.Button(
    text="READ",
    width=30,
    height=5,
    bg="cyan",
    fg="purple",
    command=readTable
)
but_read.pack()

#------Update Button------#
but_upd=tk.Button(
    text="UPDATE",
    width=30,
    height=5,
    bg="cyan",
    fg="purple",
    command=updateTable
)
but_upd.pack()

#------Delete Button------#
but_del=tk.Button(
    text="DELETE",
    width=30,
    height=5,
    bg="cyan",
    fg="purple",
    command=deleteRel
)
but_del.pack()

































window.mainloop() #Needed At end of a python file for executable application to properly run