import tkinter as tk
import webbrowser
from tkinter import *
 


class ParentWindow(Frame): # 'Frame' == the PARENT CLASS within tkinter
    def __init__(self, master): # 'self' == the'ParentWindow' class; 'master' == the 'Frame' class
        Frame.__init__(self)

        # The displayed GUI:
        self.master = master
        self.master.geometry('{}x{}'.format(650, 260)) # Window's x/y
        self.master.resizable(width=False, height=False) # Internal widgets are ABSOLUTELY positioned, no need to resize window's x/y
        self.master.title('Webpage Generator, Pt.2')
        self.master.config(bg='lightgrey')

        # The LABEL:
        self.lbl = Label(self.master, text="Welcome User")
        self.lbl.place(x=5, y=5, width=140, height=220) # Uniform padding seperates widget from its neighbors
        
        # The TEXTBOX:
        # 'Text' == tkinter's MULTI-LINE textbox widget
        self.txtbx = Text(self.master, tabs=('.5c')) # Tabs shortened from 4cm to .5cm
        self.txtbx.place(x=150, y=5, width=495, height=250) # Textbox is ABSOLUTELY positioned, so RESIZABLE=FALSE
        
        # The SUBMIT Button:
        self.btn_Submit = Button(self.master, width=7, height=1, text="Submit")
        self.btn_Submit.place(x=5, y=230, width=140)

        import webbrowser
     
        f = open('amazing sale.html','w')
        message = """<html>
       <head></head>
       <body><p>Stay tuned for our amazing summer sale!</p></body>
       </html>"""
        
        userInput =  Application.first_entry.get()
        message = """<html>
        <head></head>
        <body><p>"""+userInput+"""</p></body>
        </html>"""
        f.write(message)
        f.close()

def hello():
    webbrowser.open_new_tab('amazing sale.html')
    x = Application.first_entry.get()
    print = input({""})
app = Application()
app.mainloop()



        
if __name__ == '__main__':
    root = Tk() # the object 'root' is created from the instantiated 'Tk()' (tkinter's PARENT CLASS)
    App = ParentWindow(root) # [(root === Frame) -> passed into 'ParentWindow'] -> assigned to 'App'
    root.mainloop() # Prevents window from launching, then immediately closing
