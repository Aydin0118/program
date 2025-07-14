from socket import *
import cv2

S = socket()
S.bind(('0.0.0.0', 8888))
S.listen()

s, addr = S.accept()
print(addr)
print('1.监视,2.关机,3.重启')
print('按ESC退出监视')
c = input('input select:')

s.send(c.encode())
if c == '1':
    while True:
        # 接收文件大小（带长度前缀）
        size_len = int.from_bytes(s.recv(4), 'big')  # 获取长度前缀
        size_str = s.recv(size_len).decode()         # 接收实际数据
        size = int(size_str)
        
        s.send('ok'.encode())  # 发送确认
        cursize = 0
        with open('2.jpg', 'wb') as file:
            while cursize < size:
                data = s.recv(min(4096, size - cursize))
                if not data:
                    break
                file.write(data)
                cursize += len(data)
        
        # 显示图像
        img = cv2.imread('2.jpg')
        if img is not None:
            cv2.imshow('aydin', img)
            if cv2.waitKey(20) == 27:  # 按ESC退出
                break
        else:
            print("Error: Failed to read image")

    cv2.destroyAllWindows()