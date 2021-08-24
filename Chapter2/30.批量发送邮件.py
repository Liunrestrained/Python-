import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(email):
    # 邮件内容配置
    msg = MIMEText("经过本院校的全面考察，您的各项条件均符合本专业的需求……")
    msg['From'] = formataddr(["兔子先生", "ZhuXietian99@163.com"])
    msg["Subject"] = "录用通知"

    # 发送邮件
    server = smtplib.SMTP_SSL("smtp.163.com")
    server.login("ZhuXietian99@163.com", "QPDHDTODAWLDKOCN")
    server.sendmail("ZhuXietian99@163.com", email, msg.as_string())
    server.quit()

v1 = send_email("STARSKY8816@gmail.com")
v2 = send_email("78647886@qq.com")
