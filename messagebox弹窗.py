import tkinter as tk
from tkinter import messagebox
win=tk.Tk()
win.geometry('500x300')
win.iconbitmap(r'C:\Users\Administrator\Desktop\tkinter教程\ico图标\message_letter_mail_conversation_chat_inbox_send_email_envelope_icon_195748.ico') #设置窗口图标
win.title('the messagebox')
def minhh():#设置关闭窗口的回调函数设置成点击关闭窗口没用
    pass
    
win.protocol('WM_DELETE_WINDOW',minhh) #设置关闭窗口的回调函数
def hit_me():
    #tk.messagebox.showinfo(title='message',message='hello world')
    print(tk.messagebox.showinfo(title='message',message='hello world'))#既可以弹窗也可以在终端显示取值
    #tk.messagebox.showwarning(title='message',message='warning')
    print(tk.messagebox.showwarning(title='message',message='warning'))
    #tk.messagebox.showerror(title='message',message='error')
    print(tk.messagebox.showerror(title='message',message='error'))
    #tk.messagebox.askquestion(title='message',message='question')
    print(tk.messagebox.askquestion(title='message',message='question'))
    #tk.messagebox.askokcancel(title='message',message='okcancel')
    print(tk.messagebox.askokcancel(title='message',message='okcancel'))
    #tk.messagebox.askyesno(title='message',message='yesno') 
    print(tk.messagebox.askyesno(title='message',message='yesno')) #
    i=(tk.messagebox.askyesno(title='message',message='yesno')) #
    if i:#tk.messagebox.askyesno(title='message',message='yesno') 返回布尔值是可以被赋值的
        print('yes')
tk.Button(win,text='showinfo',command=hit_me).pack()
tk.mainloop()