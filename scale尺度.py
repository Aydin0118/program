import tkinter as tk
win=tk.Tk()
win.geometry('600x400')
win.title('Aydin')
l=tk.Label(win,bg='cyan',width=20,text='empty')
l.pack()
def print_selection(v):
    l.config(text='your selected '+v)


s=tk.Scale(win,label='try me',from_=4,to=10,orient=tk.HORIZONTAL,
           length=200,
           showvalue=1,
           tickinterval=2,
           resolution=0.01,
           command=print_selection)
s.pack()
win.mainloop()