'''print('   '*4+"!"*(8-2))#while的示例


sum=eval(input('请输入偶数:'))
while sum%2!=0:
    sum=eval(input('请重新输入'))
else:
    print('运行中，请稍后')'''
import subprocess
import os

def download_video_only(url, output_dir="./", verbose=False):
    """
    使用 you-get 仅下载视频（不下载字幕/封面/弹幕等）
    
    参数:
        url: 视频网址
        output_dir: 保存目录 (默认当前目录)
        verbose: 是否显示详细输出
    """
    try:
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 构建命令
        cmd = [
            "you-get",
            "--no-caption",       # 不下载字幕，就是不下载xml的文本文件
            #"--no-merge",         # 禁止合并分段视频（避免额外处理）
            "-o", output_dir,     # 输出目录
            url
        ]
        
        # 执行命令
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=not verbose,  # 静默模式时不捕获输出
            text=True
        )
        
        if verbose:
            print(result.stdout)
            print("视频下载完成！")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"下载失败: {e}")
        if not verbose and e.stderr:
            print("错误详情:", e.stderr)
        return False

# 使用示例
if __name__ == "__main__":
    video_url = input('请输入B站视频网址:')
    download_video_only(
        url=video_url,
        output_dir="./videos",
        verbose=True  # 显示下载进度
    )