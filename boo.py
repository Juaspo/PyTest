'''
Created on Jul 9, 2017

@author: junior
'''
print ("Hello world!")
import Tkinter as tk

'''
top = tk.Tk()

top.mainloop()
'''

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.quitButton = tk.Button(self, text="Buzz OFF", command = self.quit)
        self.quitButton.grid()
        
        self.btn = tk.Button(self, text="dont know about this", command = print("mamma mia"))
        self.btn.grid(row=0, column=1, columnspan=5)
    
app = Application()
app.master.title("I do Nothing")
app.mainloop()
