import requests

url="https://xy42x101x55x145xy240ey908y8011yy17xy.mcdn.bilivideo.cn:4483/upgcxcode/60/79/30309747960/30309747960-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&tag=&nbs=1&oi=1974805196&trid=0000e547cf714204471e8282f4a71ece9dcu&deadline=1749121668&gen=playurlv3&os=mcdn&og=cos&uipk=5&platform=pc&mid=3546696845888070&upsig=0875e24ea1b369fbdf80b5dce0f56233&uparams=e,tag,nbs,oi,trid,deadline,gen,os,og,uipk,platform,mid&mcdnid=50018153&bvc=vod&nettype=0&bw=248894&dl=0&f=u_0_0&agrr=1&buvid=003B58E1-106B-0F09-7751-8007A67E153479113infoc&build=0&orderid=0,3"

wz = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0","referer":'https://www.bilibili.com/video/BV1cd74zrENg/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=5aeaadc2c5273b90ce8d31c7a3f531f2'}

res = requests.get(url,headers = wz)

open("视频.mp4","wb").write(res.content)
print(res.status_code)

url="https://xy42x101x55x145xy240ey908y8011yy17xy.mcdn.bilivideo.cn:4483/upgcxcode/60/79/30309747960/30309747960-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&nbs=1&os=mcdn&oi=1974805196&trid=0000e547cf714204471e8282f4a71ece9dcu&mid=3546696845888070&deadline=1749121668&tag=&uipk=5&platform=pc&gen=playurlv3&og=hw&upsig=f5ae095fb2cccfb1e66dc8d4b08b9402&uparams=e,nbs,os,oi,trid,mid,deadline,tag,uipk,platform,gen,og&mcdnid=50018153&bvc=vod&nettype=0&bw=104537&buvid=003B58E1-106B-0F09-7751-8007A67E153479113infoc&build=0&dl=0&f=u_0_0&agrr=1&orderid=0,3"

wz = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0","referer":'https://www.bilibili.com/video/BV1cd74zrENg/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=5aeaadc2c5273b90ce8d31c7a3f531f2'}

res = requests.get(url,headers = wz)

open("音频.mp3","wb").write(res.content)
print(res.status_code)

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

video=VideoFileClip("视频.mp4")
audio=AudioFileClip("音频.mp3")


video_with_audio = video.with_audio(audio)


video_with_audio.write_videofile("output.mp4")