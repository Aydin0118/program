import tkinter as tk
win=tk.Tk()
win.geometry('500x300')
win.title('A Listbox')
var=tk.StringVar()

la1=tk.Label(win,height=3,width=33,bg='cyan',textvariable=var)
la1.pack()

def print():
    value=listbox.get(listbox.curselection())
    var.set(value)




bu1=tk.Button(win,text='print selection',command=print)
bu1.pack()

var1=tk.StringVar()
var1.set((1,2,3,4,5,6))

listbox=tk.Listbox(win,listvariable=var1)
newlist= ['小妹',1,77,365,000]
for i in newlist:
    listbox.insert('end',i)
listbox.insert(0,'choos')
listbox.delete(0)
listbox.pack()
tk.mainloop()