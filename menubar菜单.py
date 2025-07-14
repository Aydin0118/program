import tkinter as tk
win=tk.Tk()
win.geometry('400x300')
l=tk.Label(win,text='hello world',bg='pink')
l.pack()
counter=0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter+=1



menubar=tk.Menu(win)#确定菜单位置
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)#菜单命名
filemenu.add_command(label='New',command=do_job)#菜单内的组件
filemenu.add_command(label='OPen',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()#加横线分割
filemenu.add_command(label='Exit',command=win.quit)
#filemenu.add_separator()#加横线分割
i=0
def open_():
    global i
    if i<1:
        tk.Button(win,text='hit',width=11,command=win.quit).pack()
        i+=1
    elif i==1:
        tk.Label(win,text='button in it',bg='red').pack()
        i+=1
    else:
        pass
a=0
def jiesi():
    global a
    if a==0:
        tk.Label(win,text='hit  button closeGUI').pack()
        a+=1
    else:
        pass

    







bar=tk.Menu(win)
filemenu=tk.Menu(bar,tearoff=0)
menubar.add_cascade(label='File2',menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label='New',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Help',command=jiesi)
filemenu.add_separator()
filemenu.add_command(label='OPen button',command=open_)
filemenu.add_separator()
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=win.quit)

win.config(menu=menubar)#显示菜单

win.mainloop()