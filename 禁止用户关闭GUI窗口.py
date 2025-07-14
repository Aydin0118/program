import tkinter as tk
from tkinter import messagebox
win=tk.Tk()
win.geometry('500x300')
win.iconbitmap(r'C:\Users\Administrator\Desktop\tkinter教程\ico图标\message_letter_mail_conversation_chat_inbox_send_email_envelope_icon_195748.ico') #设置窗口图标
win.title('the messagebox')
def minhh():#设置关闭窗口的回调函数设置成点击关闭窗口没用
    if messagebox.askyesno(title='确认', message='你真的要关闭窗口吗？'):# 弹出一个确认对话框,值为True或False
        win.destroy() # 如果用户点击“是”，则销毁窗口
        
#询问式
#删除关闭指令式
'''
def minhh():#设置关闭窗口的回调函数设置成点击关闭窗口没用
    pass
'''
    
win.protocol('WM_DELETE_WINDOW',minhh) #设置关闭窗口的回调函数
tk.mainloop()

