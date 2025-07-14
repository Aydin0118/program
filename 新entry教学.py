import tkinter as tk
win=tk.Tk()
win.title('entry')
win.geometry('300x200')
e=tk.Entry(win,show='')
e.pack()
def insert():
    var=e.get()
    t.insert('insert',var)
    print(var)
def end():
    var=e.get()
    t.insert('end',var)    
tk.Button(win,text='point',command=insert).pack()
tk.Button(win,text='end',command=end).pack()
t=tk.Text(win,width=12,height=2)
t.pack()

tk.mainloop()













