import os
import glob
open('x.mp3','w')                            #生成名为x的mp3格式文件

__file__=glob.glob('*.mp3')                  #寻找后缀为MP3的文件

if __file__:
    for file_path in __file__:
        os.remove(file_path)                 #os永久删除代码
        print(f'已删除文件：{file_path}')
        print('完成')
else:print('未完成') 