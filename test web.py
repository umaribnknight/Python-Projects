

f = open("myfile.txt", "a")
f.write("Stay tuned for our amazing summer sale!")
f.close()

#open and read the file
f = open("myfile.txt", "r")
print (f.read())
#file will open in new tab because new is set to  = 1
import webbrowser
webbrowser.open("myfile.txt", new=1, autoraise=True)
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
def hello():
    x = Application.first_entry.get()
    print(x)
app = Application()
app.mainloop()
