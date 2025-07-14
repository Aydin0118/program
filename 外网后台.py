from socket import *
import cv2
import logging
import sys

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('server.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

S = socket()
try:
    # 绑定所有网络接口，端口8888
    S.bind(('0.0.0.0', 8888))
    S.listen(5)
    logging.info("服务已启动，等待客户端连接...")
except Exception as e:
    logging.error(f"启动服务失败: {e}")
    sys.exit(1)

s, addr = S.accept()
logging.info(f"客户端已连接: {addr}")

print('1.监视,2.关机,3.重启')
print('按ESC退出监视')
c = input('input select:')

try:
    s.send(c.encode())
    if c == '1':
        while True:
            # 接收文件大小信息
            try:
                size_len = int.from_bytes(s.recv(4), 'big')
                size_str = s.recv(size_len).decode()
                size = int(size_str)
                logging.info(f"准备接收图片，大小: {size}字节")
                
                s.send('ok'.encode())  # 发送确认
                cursize = 0
                with open('2.jpg', 'wb') as file:
                    while cursize < size:
                        data = s.recv(min(4096, size - cursize))
                        if not data:
                            break
                        file.write(data)
                        cursize += len(data)
                logging.info(f"图片接收完成，实际接收: {cursize}字节")
                
                # 显示图像
                img = cv2.imread('2.jpg')
                if img is not None:
                    cv2.imshow('aydin', img)
                    if cv2.waitKey(20) == 27:  # 按ESC退出
                        break
                else:
                    logging.error("图片读取失败")
            except Exception as e:
                logging.error(f"处理图片时出错: {e}")
                break

        cv2.destroyAllWindows()
    elif c == '2':
        logging.info("发送关机指令")
    elif c == '3':
        logging.info("发送重启指令")
        
except Exception as e:
    logging.error(f"通信错误: {e}")
finally:
    s.close()
    S.close()
    logging.info("服务已关闭")