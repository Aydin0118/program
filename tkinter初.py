import tkinter as op


window= op.Tk()   #创建窗口
window.iconbitmap(r'C:\Users\Administrator\Desktop\tkinter教程\ico图标\borderless_worldwide_message_chat_mail_world_icon_267339.ico')
name=('my frist window')
window.title(name)  #name为窗口名

window.geometry('600x400')#格式为宽x高

l=op.Label(window,
           text='hello ktinter',
           bg='red',font=('Arial',12),
           width=15,
           height=2
           )



l.pack(pady=20)
def hit_me():
    print('hit')
    
    op.Label(window,text='你点了').pack()







B01=op.Button(window,
              text='hit me',
              width=15,
              height=2,
              command=hit_me
              )
B01.pack()



window.mainloop()  #事件循环显示
