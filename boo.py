'''
Created on Jul 9, 2017

@author: junior
'''
from argparse import Action
from _functools import partial
import sys
from Tkinter import *
print ("Hello world!")
import Tkinter as tk

'''
top = tk.Tk()

top.mainloop()
'''

textStr = ""


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.quitButton = tk.Button(self, text="Buzz OFF", command = self.quit)
        self.quitButton.grid()
        
        self.btn = tk.Button(self, text="dont know about this", command=partial(action, "boo"))
        self.btn.grid(row=0, column=1, columnspan=5)
        
        self.btn2 = tk.Button(self,  text="Grab text", command = getInput)
        self.btn2.grid(row=1, column=0, columnspan=2)
        
        self.btn3 = tk.Button(self,  text="write to terminal", command = getText)
        self.btn3.grid(row=3, column=0, columnspan=2)
        
        self.Txt = tk.Text(self, height=2, width=30)
        self.Txt.grid(row=1, column=2, columnspan=1)
        
    def txtGet(self):
        return self.Txt.get("1.0", 'end-1c') 
        #the 1.0 means read from line 1 0th char
        #end-1c means read to end but do not read the last char (-1c) since this is an extra \n
    
            
        

def getText():
        content = app.txtGet()
        print (content)
        
            
def action( strn ):
    print (strn)
    return
    
def getInput():
    try:
        stri = sys.stdin.readline()
        print (stri)
    except:
        print("no input detected!")
    
    return

    
app = Application()
app.master.title("I do Nothing")
app.mainloop()
