from tkinter import *
from tkinter import ttk
import re
root = Tk()
root.title = ('Calculator')

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

display = StringVar()
display.set('12346872345678987654323456789654321345')

"""def listsolver(lst):
    if
"""
def clearscreen():
    display.set('')

def eval():
    pass
"""
    if re.search(r'[+-*/]{2,}':
        display.set('Error')
    elif display.get() == 'Error':
        display.set('')
    else:
        func = re.findall(r'[+-*/]{1}',display.get())
        num = re.findall(r'\d+',display.get())
        newnum = []
        newfunc = []
        for i in range(0,len(func)):
            if func[i] 
            if func[i] == '*':
                num[i] = num[i] * num.pop"""
                


screen = ttk.Frame(mainframe, width = '305', height = '30', relief = 'groove').grid(column = 0, row = 0, columnspan = 5, sticky = (W, N))

ttk.Button(mainframe, text = '1', command = lambda: display.set(display.get() + '1')).grid(column = 0, row = 1)
ttk.Button(mainframe, text = '2', command = lambda: display.set(display.get() + '2')).grid(column = 1, row = 1)
ttk.Button(mainframe, text = '3', command = lambda: display.set(display.get() + '3')).grid(column = 2, row = 1)
ttk.Button(mainframe, text = '4', command = lambda: display.set(display.get() + '4')).grid(column = 0, row = 2)
ttk.Button(mainframe, text = '5', command = lambda: display.set(display.get() + '5')).grid(column = 1, row = 2)
ttk.Button(mainframe, text = '6', command = lambda: display.set(display.get() + '6')).grid(column = 2, row = 2)
ttk.Button(mainframe, text = '7', command = lambda: display.set(display.get() + '7')).grid(column = 0, row = 3)
ttk.Button(mainframe, text = '8', command = lambda: display.set(display.get() + '8')).grid(column = 1, row = 3)
ttk.Button(mainframe, text = '9', command = lambda: display.set(display.get() + '9')).grid(column = 2, row = 3)
ttk.Button(mainframe, text = '0', command = lambda: display.set(display.get() + '0')).grid(column = 1, row = 4)

ttk.Button(mainframe, text = '+', command = lambda: display.set(display.get() + '+')).grid(column = 4, row = 1, sticky = (E))
ttk.Button(mainframe, text = '-', command = lambda: display.set(display.get() + '-')).grid(column = 4, row = 2, sticky = (E))
ttk.Button(mainframe, text = '*', command = lambda: display.set(display.get() + '*')).grid(column = 4, row = 3, sticky = (E))
ttk.Button(mainframe, text = '/', command = lambda: display.set(display.get() + '/')).grid(column = 4, row = 4, sticky = (E))

ttk.Button(mainframe, text = '=', command = eval).grid(column = 2, row = 4)
ttk.Button(mainframe, text = 'C', command = clearscreen).grid(column = 0, row = 4)

ttk.Label(mainframe, textvariable = display, anchor = 'e').grid(column = 0, row = 0, columnspan = 5, sticky = (E, W))
mainframe.columnconfigure(5,weight=1)


root.mainloop()