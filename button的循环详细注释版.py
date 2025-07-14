from tkinter import *
i=0 #定义一个全局变量，0为F，用于跟踪按钮状态
def callback():#定义按钮点击事件函数
    global i#赋值引用局部变量，声明使用全局变量i
    if i==0:#如果按钮为F未点击
        
        i=1#设定为T，已点击
        var.set('点了之后')#将label的文字改为点了之后
        
    else:#如果点击了之后
        i=0#将i设定为F，初始化
        var.set('点了之前')#将label的文字改为点了之前
   


win=Tk()#设置一个窗口
win.title('GUI程序')#窗口名字为“GUI程序”
win.geometry('500x300')#窗口大小宽x高
var=StringVar()#在后面定义label的显示函数
var.set('点了之前')#label初始显示文本
Label_1=Label(win,textvariable=var)#win指在为win的窗口显示，显示为var
button=Button(win,text='hit me',command=callback)#按钮在win显示，文字为‘hit me’，指令为callback
Label_1.pack()#pack显示函数
button.pack()

mainloop()#整体显示函数