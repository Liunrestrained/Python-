'''例如：网络问题，自身代码问题，三方软件或代码的问题。'''
import requests

while True:
    url = input("请输入下载链接")

    try:  # 正常情况下执行的：
        res = requests.get(url=url)
    except Exception as e:
        # 代码块，上述代码出现异常，待执行。
        print("请求失败，原因：{}".format(str(e)))
        continue  # 重新执行循环

    with open("content.txt", mode="wb")as f:
        f.write(res.content)


