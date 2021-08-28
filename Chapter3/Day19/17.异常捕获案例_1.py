# 案例：你我合作协同开发，你调用我写的方法。
# 我定义了一个函数:
class EmailValidError(Exception):
    title = "邮箱格式错误"


class ContentRequiredError(Exception):
    title = "文本不能为空错误"


def send_email(email, content):
    if not re.match("\w+@live.com", email):
        raise EmailValidError()
    if len(content) == 0:
        raise ContentRequiredError()
    # 发送邮件代码...
    # ...


# 你调用我写的函数
def execute():
    # 其他代码
    # ...

    try:
        send_email(...)
    except EmailValidError as e:
        pass
    except ContentRequiredError as e:
        pass
    except Exception as e:
        print("发送失败")

execute()

# 提示：如果想要写的简单一点，其实只写一个Exception捕获错误就可以了。
