import tkinter as tk
import tkinter.ttk as ttk

#######---ADDING FOR LATER---#######
#import mysql.connector 
#db_connection = mysql.connector.connect(
#    host="",
#    user="",
#    password="")


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

def readRel():
    print("Read.")

def updateTuple():
    print("Updated")

def deleteTuple():
    print("deleted")



#------Titled Window------#
window= tk.Tk() #Window Creation
window.title("Database CRUD Application") #Titling Window
window.geometry("750x500") #Window Size

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
    command=readRel
)
but_read.pack()

#------Update Button------#
but_upd=tk.Button(
    text="UPDATE",
    width=30,
    height=5,
    bg="cyan",
    fg="purple",
    command=updateTuple
)
but_upd.pack()

#------Delete Button------#
but_del=tk.Button(
    text="DELETE",
    width=30,
    height=5,
    bg="cyan",
    fg="purple",
    command=deleteTuple
)
but_del.pack()

































window.mainloop() #Needed At end of a python file for executable application to properly run