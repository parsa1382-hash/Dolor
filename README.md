# Dolor
import tkinter as tk
from tkinter import filedialog, Text, ttk
from tkinter import*
import requests


root=tk.Tk()
#container = ttk.Frame(root)
canvas = tk.Canvas(root, height=350, width=640)
canvas.pack()

d= {'Dolor':22000,'Euro':26000,'Pond':30000,'Toman':1}
'''
def up():
    global d
    
    url=requests.get('https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1')
    do=url.text.split('\n')[3038][-12:-5].split(',')
    do='.'.join(do)
    do=float(do)/10
    
    url1=requests.get('https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1')
    eu=url1.text.split('\n')[3150:3180].split(',')
    eu='.'.join(eu)
    print(eu)
    
    e=float(eu)/10
    d.update({'Dolor':do,'Euro':eu})
    
'''
#    print(do,e)
#root.after(5000,up)
#up()
num=StringVar(root)
num.set(1)
e=Entry(canvas,textvariable=num,width=8).grid(row = 1, column = 1)

var = StringVar(root)


var.set('Dolor')

menu = OptionMenu(canvas, var, *d)
ans=tk.Label(canvas, text=22000.0)
ans.grid(row = 1, column = 4)

menu.grid(row = 1, column =2)


var2 = StringVar(root)
var2.set('Toman')

menu2 = OptionMenu(canvas, var2, *d)
#Label(canvas, text="Choose a dish").grid(row = 1, column = 3)
menu2.grid(row = 1, column =5)

def convert():
    global ans
    a=float(d[var.get()])
    b=float(d[var2.get()])
    c=float(num.get())
    an=c*(a/b)
    an=round(an,2)
    ans.config(text=an)
    print(an)
con=Button(canvas,text="        convert        ",command=convert).grid(row = 1, column = 3)

def convert2(event):
    convert()
root.bind('<Return>',convert2)
root.mainloop()
