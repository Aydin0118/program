from tkinter import *
i=0
def callback():
    

    var.set('点了之后')
    


win=Tk()
win.title('GUI程序')
win.geometry('500x300')
var=StringVar()
var.set('点了之前')
Label_1=Label(win,textvariable=var)
button=Button(win,text='hit me',command=callback)
Label_1.pack()
button.pack()

mainloop()