from socket import *
from PIL import ImageGrab
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import sys
import time
import logging
import requests
import configparser

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('client.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

# 默认配置
DEFAULT_SERVER_IP = '117.183.205.145'
DEFAULT_SERVER_PORT = 8888
CONFIG_FILE = 'client_config.ini'

# 从配置文件加载设置
def load_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
        server_ip = config.get('SERVER', 'IP', fallback=DEFAULT_SERVER_IP)
        server_port = config.getint('SERVER', 'PORT', fallback=DEFAULT_SERVER_PORT)
    else:
        server_ip = DEFAULT_SERVER_IP
        server_port = DEFAULT_SERVER_PORT
    return server_ip, server_port

# 保存配置到文件
def save_config(server_ip, server_port):
    config = configparser.ConfigParser()
    config['SERVER'] = {
        'IP': server_ip,
        'PORT': str(server_port)
    }
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

# 初始化全局变量
SERVER_IP, SERVER_PORT = load_config()

def get_public_ip():
    """获取本机公网IP"""
    try:
        return requests.get('https://api.ipify.org', timeout=5).text
    except Exception as e:
        logging.error(f"获取公网IP失败: {e}")
        return "无法获取公网IP"

def check_port_availability(ip, port):
    """检查端口是否可用"""
    s = socket()
    s.settimeout(3)
    try:
        s.connect((ip, port))
        return True
    except Exception as e:
        logging.error(f"端口检查失败: {e}")
        return False
    finally:
        s.close()

def background_service():
    """后台服务线程函数"""
    global SERVER_IP, SERVER_PORT
    
    logging.info("后台服务启动中...")
    connection_success = False
    
    for attempt in range(1, 6):
        try:
            s = socket()
            logging.info(f"尝试连接服务器 {SERVER_IP}:{SERVER_PORT} (第{attempt}次)...")
            
            # 设置较短的超时时间（3秒）
            s.settimeout(3.0)
            s.connect((SERVER_IP, SERVER_PORT))
            
            logging.info("服务器连接成功")
            connection_success = True
            
            c = s.recv(1024).decode()
            logging.info(f"收到服务器指令: {c}")
            
            if c == '1':
                while True:
                    try:
                        # 截屏并调整大小
                        image = ImageGrab.grab()
                        image = image.resize((960, 540))
                        image.save('1.jpg')
                        size = os.path.getsize('1.jpg')
                        logging.debug(f"图片大小: {size}字节")
                        
                        # 发送文件大小信息
                        size_str = str(size)
                        s.send(len(size_str).to_bytes(4, 'big'))
                        s.send(size_str.encode())
                        
                        # 等待确认
                        s.recv(1024)
                        
                        # 发送图片数据
                        with open('1.jpg', 'rb') as file:
                            while True:
                                data = file.read(4096)
                                if not data:
                                    break
                                s.send(data)
                        logging.debug("图片发送完成")
                        time.sleep(1)  # 控制帧率
                    except Exception as e:
                        logging.error(f"发送图片时出错: {e}")
                        break
            elif c == '2':
                logging.info("执行关机操作")
                os.system('shutdown -s -t 1')
                sys.exit(0)
            elif c == '3':
                logging.info("执行重启操作")
                os.system('shutdown -r -t 1')
                sys.exit(0)
            break  # 成功执行后跳出重试循环
            
        except timeout:
            wait_time = attempt * attempt  # 指数退避：1, 4, 9, 16, 25秒
            logging.error(f"连接超时，{wait_time}秒后重试...")
            time.sleep(wait_time)
        except ConnectionRefusedError:
            logging.error("服务器拒绝连接，可能是服务未运行或防火墙阻止")
            time.sleep(5)
        except Exception as e:
            logging.error(f"连接服务器失败: {type(e).__name__} - {e}")
            time.sleep(5)
        finally:
            try:
                s.close()
            except:
                pass
    
    if not connection_success:
        logging.error("无法连接服务器，请检查配置和网络状态")


service_thread = None
service_running = False

def start_background_service():
   
    global service_thread, service_running
    
    if service_running:
        logging.warning("服务已经在运行中")
        return
    
    service_thread = threading.Thread(target=background_service)
    service_thread.daemon = True
    service_running = True
    service_thread.start()

def restart_background_service():
    """重启后台服务线程"""
    global service_running
    service_running = False
    
    # 等待线程结束
    if service_thread and service_thread.is_alive():
        service_thread.join(timeout=1.0)
    
    time.sleep(0.5)
    start_background_service()
    logging.info("后台服务已重启")

# GUI界面
def create_gui():
    root = tk.Tk()
    root.title('Aydin Control')
    root.geometry('800x600')
    # root.iconbitmap(r'C:\path\to\icon.ico')  # 取消注释并设置正确路径
    
    # 状态变量
    server_ip_var = tk.StringVar(value=SERVER_IP)
    server_port_var = tk.StringVar(value=str(SERVER_PORT))
    
    def update_server_info():
        """更新服务器信息显示"""
        global SERVER_IP, SERVER_PORT
        SERVER_IP = server_ip_var.get()
        SERVER_PORT = int(server_port_var.get())
        save_config(SERVER_IP, SERVER_PORT)
        server_info_label.config(text=f"服务器地址: {SERVER_IP}:{SERVER_PORT}")
        
    def test_connection():
        """测试连接按钮回调"""
        update_server_info()
        port_open = check_port_availability(SERVER_IP, SERVER_PORT)
        
        if port_open:
            messagebox.showinfo("连接测试", "端口已开放，可以尝试连接")
        else:
            messagebox.showerror("连接测试", 
                "无法连接到服务器\n"
                "可能原因:\n"
                "1. 服务器未运行\n"
                "2. 防火墙阻止连接\n"
                "3. 网络配置错误\n"
                "4. IP地址或端口号不正确")
    
    def open_settings():
        """打开设置对话框"""
        settings_window = tk.Toplevel(root)
        settings_window.title("服务器设置")
        settings_window.geometry("400x250")
        settings_window.grab_set()
        
        tk.Label(settings_window, text="服务器设置", font=("Arial", 14)).pack(pady=10)
        
        # IP 地址设置
        ip_frame = tk.Frame(settings_window)
        ip_frame.pack(fill="x", padx=20, pady=5)
        tk.Label(ip_frame, text="服务器 IP:").pack(side="left")
        ip_entry = tk.Entry(ip_frame, textvariable=server_ip_var, width=20)
        ip_entry.pack(side="right", padx=10)
        
        # 端口设置
        port_frame = tk.Frame(settings_window)
        port_frame.pack(fill="x", padx=20, pady=5)
        tk.Label(port_frame, text="服务器端口:").pack(side="left")
        port_entry = tk.Entry(port_frame, textvariable=server_port_var, width=10)
        port_entry.pack(side="right", padx=10)
        
        # 按钮区域
        btn_frame = tk.Frame(settings_window)
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text="保存设置", command=lambda: [update_server_info(), settings_window.destroy()]).pack(side="left", padx=5)
        tk.Button(btn_frame, text="测试连接", command=test_connection).pack(side="left", padx=5)
        tk.Button(btn_frame, text="取消", command=settings_window.destroy).pack(side="left", padx=5)
    
    def reconnect_service():
        """手动重连服务"""
        restart_background_service()
        status_label.config(text="状态: 正在重新连接...", fg="blue")
    
    # 添加UI元素
    header_frame = tk.Frame(root)
    header_frame.pack(fill="x", padx=10, pady=15)
    
    tk.Label(header_frame, text="远程监控客户端", font=("Arial", 16, "bold")).pack(side="left")
    
    # 功能按钮区域
    btn_frame = tk.Frame(header_frame)
    btn_frame.pack(side="right", padx=10)
    
    tk.Button(btn_frame, text="设置", command=open_settings, width=8).pack(side="left", padx=3)
    tk.Button(btn_frame, text="重连", command=reconnect_service, width=8).pack(side="left", padx=3)
    
    # 服务器信息
    server_frame = tk.LabelFrame(root, text="服务器信息")
    server_frame.pack(pady=10, padx=20, fill="x")
    
    server_info_label = tk.Label(server_frame, text=f"服务器地址: {SERVER_IP}:{SERVER_PORT}")
    server_info_label.pack(anchor="w", padx=10, pady=3)
    
    tk.Label(server_frame, text=f"本机公网IP: {get_public_ip()}").pack(anchor="w", padx=10, pady=3)
    
    # 连接状态
    status_frame = tk.Frame(server_frame)
    status_frame.pack(fill="x", padx=10, pady=5)
    
    tk.Label(status_frame, text="状态:").pack(side="left")
    status_label = tk.Label(status_frame, text="连接中...", fg="blue")
    status_label.pack(side="left", padx=5)
    
    # 日志显示
    log_frame = tk.LabelFrame(root, text="运行日志")
    log_frame.pack(pady=10, padx=20, fill="both", expand=True)
    
    log_text = tk.Text(log_frame, height=10)
    log_text.pack(padx=10, pady=5, fill="both", expand=True)
    
    # 日志滚动条
    scrollbar = tk.Scrollbar(log_frame, command=log_text.yview)
    scrollbar.pack(side="right", fill="y")
    log_text.config(yscrollcommand=scrollbar.set)
    
    # 添加日志处理器
    class TextHandler(logging.Handler):
        def __init__(self, text):
            logging.Handler.__init__(self)
            self.text = text
            
        def emit(self, record):
            msg = self.format(record)
            
            # 根据日志级别设置颜色
            if record.levelno >= logging.ERROR:
                color = "red"
            elif record.levelno >= logging.WARNING:
                color = "orange"
            elif record.levelno >= logging.INFO:
                color = "blue"
            else:
                color = "black"
                
            self.text.configure(state="normal")
            self.text.tag_config(color, foreground=color)
            self.text.insert(tk.END, msg + '\n', color)
            self.text.configure(state="disabled")
            self.text.see(tk.END)
    
    text_handler = TextHandler(log_text)
    text_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(text_handler)
    
    # 关闭按钮
    def on_close():
        if messagebox.askyesno("退出", "确定要退出程序吗？"):
            root.destroy()
            sys.exit(0)
    
    footer_frame = tk.Frame(root)
    footer_frame.pack(pady=15)
    
    btn_exit = tk.Button(footer_frame, text="退出程序", command=on_close, width=12)
    btn_exit.pack()
    
    # 工具提示
    def show_tooltip(event, text):
        tooltip = tk.Toplevel(root)
        tooltip.wm_overrideredirect(True)
        tooltip.geometry(f"+{event.x_root+10}+{event.y_root+10}")
        label = tk.Label(tooltip, text=text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()
        
        def hide_tooltip():
            tooltip.destroy()
            
        tooltip.after(3000, hide_tooltip)
    
    # 添加状态栏
    statusbar = tk.Label(root, text="就绪", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    statusbar.pack(side=tk.BOTTOM, fill=tk.X)
    
    # 绑定工具提示到状态标签
    status_label.bind("<Enter>", lambda e: show_tooltip(e, "当前服务连接状态"))
    status_label.bind("<Leave>", lambda e: root.after(1000, lambda: e.widget.master.destroy()))
    
    # 启动后台服务
    start_background_service()
    
    # 定期更新状态
    def update_status():
        global service_running
        
        if service_running and service_thread.is_alive():
            status_label.config(text="状态: 运行中", fg="green")
        else:
            status_label.config(text="状态: 未连接", fg="red")
        
        root.after(2000, update_status)
    
    update_status()
    
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

# 启动GUI
if __name__ == "__main__":
    create_gui()
