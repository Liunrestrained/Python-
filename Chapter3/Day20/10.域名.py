'''假设你创业开发了一个网站，用户很难记住你的公网IP：`123.206.15.88:80`   ``123.206.15.88`。
那么可以使用域名，让域名和IP创建对应关系，用户只需要记住域名就可以了，域名只是和IP创建了对应关系，与端口无关 `www.baidu.com:80`，例如：

www.baidu.com   -->  110.242.68.3
www.taobao.com  --> 121.18.239.232

注意：
在用户在自己的电脑或手机上输入域名去访问时，其实要执行两个步骤：
- 根据域名寻找IP。（寻找IP）
        - 第一步：在自己电脑的DNS缓存记录中寻找 域名对应的IP，如果未命中，则执行下一步。

        - 第二步：在自己电脑的hosts文件中寻找，如果未命中，则执行下一步。

        - 第三步：在自己电脑上找到DNS配置的地址（本地域名服务器），去这个地址寻找域名对应的IP，如果未命中，则执行下一步。

        - 第四步：去根域名服务器中询问（全球共13台根域名服务器，距离中国最近的一台是在日本）
- 获得IP之后，再通过IP再去访问指定服务器。
'''


'''如何获取和使用域名：
1.租一个域名；
2.国内的域名需要备案；
3.域名解析：让域名和IP创建关联关系，并将关系同步到相关：本地域名服务器 和 根域名服务器（含顶级和二级域名服务器）。

'''