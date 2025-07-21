import requests
package_website=input('请输入包网址：')

url=package_website

_referer=input('请输入referer:')

user_agent=input('请输入user-agent:')

wz = {'user-agent':user_agent,"referer":_referer}

res = requests.get(url,headers = wz)

open("视频.mp4","wb").write(res.content)

print(res.status_code)