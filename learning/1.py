from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
from pandas import *
import random
import tkinter as tk

s = pd.read_csv("Tables.csv",encoding="ANSI",dtype=pd.StringDtype())
#generator will obtain random value from selected column of table.
col = s.columns
y = 'City_plots'

x = col.get_loc(y)


root = Tk() #create base tk app
root.title("D&D Generator") #how we name the window
mainframe = ttk.Frame(root, padding="10 10 12 12") 
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(20, weight=1)
root.rowconfigure(20, weight=1)
ttk.Label(mainframe, text="Select a Category:").grid(column=1, row=1)
selectedCategory = tk.StringVar()
out = tk.StringVar()
cata_selec = ttk.Combobox(mainframe, textvariable=selectedCategory)
cata_selec['values'] = [s.columns[m] for m in range(0, 9)]
cata_selec['state'] = 'readonly'
cata_selec.grid(column=2, row=1)
def generator():
    catval = selectedCategory.get()
    prompt = s[catval]
    i = random.randrange(len(prompt))
    answer = s.at[s.index[i],catval]
    out.set(answer)
ttk.Label(mainframe, textvariable= out).grid(column=2,row=3)
ttk.Button(mainframe, text="Generate", command=generator).grid(column=1,row=2)
ttk.Button(mainframe, text="Quit", command=root.destroy).grid(column=0, row=2)
root.mainloop()
