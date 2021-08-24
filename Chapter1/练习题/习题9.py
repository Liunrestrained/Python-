'''让用户输入一段文本，请实现将文本中的敏感词 `苍老师`、`波波老师`替换为 `***`，最后并输入替换后的文本。'''

data_list = ["苍老师", "波波老师"]
enter = input("输入你最爱的女演员").strip()

for i in data_list:
    if i in enter:
        data = enter.replace(i, "***")
        print(data)
