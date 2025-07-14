import tkinter as tk
win=tk.Tk()
win.geometry('500x300')
win.title('A Listbox')
var=tk.StringVar()
l=tk.Label(win,bg='red',width=26,text='Empty')
l.pack()
def printf():
    l.config(text='you selected'+var.get())
    print(var.get())
r1=tk.Radiobutton(win,text='Option A',variable=var,value='A',command=printf)
r1.pack()
r1=tk.Radiobutton(win,text='Option B',variable=var,value='B',command=printf)
r1.pack()
r1=tk.Radiobutton(win,text='Option C',variable=var,value='C',command=printf)
r1.pack()

tk.mainloop()