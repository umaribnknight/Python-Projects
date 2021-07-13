f = open('amazing sale.html','w')

message = """<html>
<head></head>
<body><p>Stay tuned for our amazing summer sale!</p></body>
</html>"""

f.write(message)
f.close()

import webbrowser
### webbrowser.open_new_tab('amazing sale.html')

#create gui for users
import tkinter as tk
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('400x400')
        self.title('Web Page Generator')
        first_label = tk.Label(self, text = "WELCOME USER!!", font=10)
        first_label.pack(padx= 3, pady = 3)

        #This is how the user enters his input
        first_button = tk.Button(self, text ="Enter Here", command = hello)
        first_button.pack(padx= 5, pady = 5)
        Application.first_entry = tk.Entry(self, width = 30)
        Application.first_entry.pack(padx = 7, pady = 7)
        webbrowser.open_new_tab

      

       # userInput =  Application.first_entry.get()
       # message = """<html>
        ##<head></head>
        #<body><p>"""+userInput+"""</p></body>
        #</html>"""
        #f.write(message)
        #f.close()
def hello():
    x = Application.first_entry.get()
    print(x)
    userInput =  Application.first_entry.get()
    htmlFile = open("amazing sale.html","w")
    message = """<html>
    <head></head>
    <body><p>"""+userInput+"""</p></body>
    </html>"""
    htmlFile.write(message)
    htmlFile.close()
    webbrowser.open_new_tab('amazing sale.html')
app = Application()
app.mainloop()
