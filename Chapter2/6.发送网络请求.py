import requests  # 发送网络请求模块 pip3 install requests

res = requests.get(url="https://wallpapershome.com/images/wallpapers/lighthouse-3840x2160-ocean-waves-4k-23537.jpg",
                   headers={
                       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"})
print(res.content)
# 按照固定的格式进行使用，一般网络存在防爬虫机制，使用headers来伪造浏览器请求头，发送网络请求。