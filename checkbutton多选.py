import tkinter as tk
win=tk.Tk()
win.geometry('600x400')
win.title('Aydin')
l=tk.Label(win,bg='cyan',width=20,text='empty')
l.pack()
var1=tk.IntVar()
var2=tk.IntVar()
def print_selection():
    if(var1.get()==1)&(var2.get()==0):
        l.config(text='I love only python')
    elif(var1.get()==0)&(var2.get()==1):
        l.config(text='I love only C++')
    elif(var1.get()==0)&(var2.get()==0):
        l.config(text='I do not like either')
    else:
        l.config(text='I love both')

c1=tk.Checkbutton(win,text='python',variable=var1,onvalue=1,offvalue=0,command=print_selection
                  )
c2=tk.Checkbutton(win,text='C++   ',variable=var2,onvalue=1,offvalue=0,command=print_selection
                  )
c1.pack()
c2.pack()
win.mainloop()