import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog #not sure if we need this
import os
import datetime
from datetime import timedelta
     
 

# create necessary tkinter widgets
def CreateWidgets():
    link_Label = Label(root, text ="Select The File To Copy : ",
                    bg = "#E8D579")
    link_Label.grid(row = 1, column = 0,
                    pady = 5, padx = 5)
     
    root.sourceText = Entry(root, width = 50,
                            textvariable = sourceLocation)
    root.sourceText.grid(row = 1, column = 1,
                        pady = 5, padx = 5,
                        columnspan = 2)
     
    source_browseButton = Button(root, text ="Browse",
                                command = SourceBrowse, width = 15)
    source_browseButton.grid(row = 1, column = 3,
                            pady = 5, padx = 5)
     
    destinationLabel = Label(root, text ="Select The Destination : ",
                            bg ="#E8D579")
    destinationLabel.grid(row = 2, column = 0,
                        pady = 5, padx = 5)
     
    root.destinationText = Entry(root, width = 50,
                                textvariable = destinationLocation)
    root.destinationText.grid(row = 2, column = 1,
                            pady = 5, padx = 5,
                            columnspan = 2)
     
    dest_browseButton = Button(root, text ="Browse",
                            command = DestinationBrowse, width = 15)
    dest_browseButton.grid(row = 2, column = 3,
                        pady = 5, padx = 5)
     
    copyButton = Button(root, text ="Copy File",
                        command = CopyFile, width = 15)
    copyButton.grid(row = 3, column = 1,
                    pady = 5, padx = 5)
     
    moveButton = Button(root, text ="Move File",
                        command = MoveFile, width = 15)
    moveButton.grid(row = 3, column = 2,
                    pady = 5, padx = 5)
 
def SourceBrowse():
     
    # Opening the file-dialog directory prompting
    # the user to select files to copy using
    # filedialog.askopenfilenames() method. Setting
    # initialdir argument is optional Since multiple
    # files may be selected, converting the selection
    # to list using list()
    root.files_list = filedialog.askdirectory()
     
    # Displaying the selected files in the root.sourceText
    # Entry using root.sourceText.insert()
    root.sourceText.insert('1', root.files_list)
     
def DestinationBrowse():
    # Opening the file-dialog directory prompting
  
    destinationdirectory = filedialog.askdirectory()
 
    # Displaying the selected directory in the
    # root.destinationText Entry using
    # root.destinationText.insert()
    root.destinationText.insert('1', destinationdirectory)
     
def CopyFile():
    # Retrieving the source file selected 
    files_list = root.sourceText.get()
    files=os.listdir(files_list)
 
    destination_location = destinationLocation.get()
 
    # Looping through the files present in the list
    for f in files:
        abspath = os.path.join(files_list,f)
        hrs_24 = datetime.datetime.now() - timedelta(hours=24)
        modtime = os.path.getmtime(abspath)
        datetimeF = datetime.datetime.fromtimestamp(modtime)
        if hrs_24 < datetimeF:
        # Moving the file to the destination 
      
           shutil.copy(f, destination_location)
 
    messagebox.showinfo("SUCCESSFULL")

    
     
def MoveFile():
     
  
    files_list = root.sourceText.get()
    files = os.listdir(files_list)
    
    
    destination_location = destinationLocation.get()
 
    # Looping through the files present in the list
    for f in files:
        abspath = os.path.join(files_list,f)
        hrs_24 = datetime.datetime.now() - timedelta(hours=24)
        modtime = os.path.getmtime(abspath)
        datetimeF = datetime.datetime.fromtimestamp(modtime)
        if hrs_24 < datetimeF:
        # Moving the file to the destination 
           shutil.move(abspath, destination_location)

           messagebox.showinfo("SUCCESSFULL")
 
# Creating object of tk class
root = tk.Tk()
     

root.geometry("830x120")
root.title("Copy-Move GUI")
root.config(background = "black")
     
# Creating tkinter variable  ## not sure if i need this
sourceLocation = StringVar()
destinationLocation = StringVar()
     
# Calling the CreateWidgets() function
CreateWidgets()
     
# Defining infinite loop
root.mainloop()
