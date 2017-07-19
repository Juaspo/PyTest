'''
Created on Jul 9, 2017

@author: junior
'''

from _functools import partial
import sys
try:
    from Tkinter import *
    import Tkinter as tk
except ImportError:
    from tkinter import *
    import tkinter as tk
    
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
        lbstr = StringVar()
        lbstr.set("Make me change")
        
        self.quitButton = tk.Button(self, text="Buzz OFF", command = self.quit)
        self.quitButton.grid()
        
        self.btn = tk.Button(self, text="dont know about this", command=partial(action, "boo"))
        self.btn.grid(row=0, column=2, columnspan=2)
        
        self.btn2 = tk.Button(self,  text="Grab text", command = getInput)
        self.btn2.grid(row=1, column=0, columnspan=2)
        
        self.btn3 = tk.Button(self,  text="write to terminal", command = getText)
        self.btn3.grid(row=3, column=0, columnspan=2)
        
        self.Txt = tk.Text(self, height=2, width=30)
        self.Txt.grid(row=1, column=2, columnspan=1)
        
        self.lb = Label(self, text=lbstr)
        self.lb.grid(row=0, column=1)
        
        print(lbstr)
        
    def txtGet(self):
        return self.Txt.get("1.0", 'end-1c') 
        #the 1.0 means read from line 1 0th char
        #end-1c means read to end but do not read the last char (-1c) since this is an extra \n
        
    
    def changeLabel(self, strinput):
        self.lbstr.set(strinput)
           
        
def getText():
        content = app.txtGet()
        print (content)
        
            
def action( strn ):
    print (strn)
    return
    
def getInput():
    #try:
    stri = sys.stdin.readline()
    #stri = input("write text to print")
    print("grabbing stdin")
    app.changeLabel(stri)
    print(stri)
    print("grab finished")
    '''    
    except:
        print("no input detected!")
    '''
    return

app = Application()
app.master.title("I do Nothing")
app.mainloop()
