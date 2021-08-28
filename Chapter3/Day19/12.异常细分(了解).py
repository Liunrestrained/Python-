import requests
from requests import exceptions

while True:
    url = input("下载链接")
    try:
        res = requests.get(url=url)
        print(res)
    except exceptions.MissingSchema as e:  # 细分处理
        print("URL架构不存在")
    except exceptions.InvalidSchema as e:  # 细分处理
        print("URL架构错误")
    except exceptions.InvalidURL as e:  # 细分处理
        print("URL地址格式错误")
    except exceptions.ConnectionError as e:  # 细分处理
        print("网络连接出错")
    except Exception as e:  # 模糊处理
        print("代码出现错误", e)
# # 提示：如果想要写的简单一点，其实只写一个Exception捕获错误就可以了。
