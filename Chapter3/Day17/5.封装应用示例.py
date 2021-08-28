class Pagination:
    def __init__(self, current_page, per_page_num=10):
        self.per_page_num = per_page_num  # 将page_object的第2个值赋值给per_page_num

        if not current_page.isdecimal():  # 如果输入的页码current_page不是十进制数
            self.current_page = 1  # 就让current_page = 1
            return
        current_page = int(current_page)  # 如果输入的页码current_page是一个十进制数，就把它转换为整形
        if current_page < 1:  # 如果输入的页码小于1
            self.current_page = 1  # 那就让它等于1
            return
        self.current_page = current_page  # 将转换的整形current_page参数重新赋值

    def start(self):
        return (self.current_page - 1) * self.per_page_num  # 页码-1，乘以要显示的条数，作为起始行

    def end(self):
        return self.current_page * self.per_page_num  # 页码乘以条数，作为要显示的终止行


user_list = ["用户-{}".format(i) for i in range(1, 3000)]

# 分页显示，每页显示10条
while True:
    page = input("请输入页码")
    pg_object = Pagination(page, 20)  # (current_page, per_page_num)
    page_data_list = user_list[pg_object.start():pg_object.end()]  # 回过头来执行两个方法
    for i in page_data_list:
        print(i)
