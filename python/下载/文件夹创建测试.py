import os
import glob

# 定义要创建的文件夹路径
folder_path = "my_new_folder"

# 检查文件夹是否存在，不存在则创建
if not os.path.exists(folder_path):
    os.makedirs(folder_path)  # 创建文件夹（包括所有必要的父目录）
    print(f"✅ 已创建文件夹: {folder_path}")
else:
    print(f"📁 文件夹已存在: {folder_path}")



for folder_path in glob.glob('*.mp3'):
    os.remove(folder_path)  #删除指令
else:
    print('完成')
