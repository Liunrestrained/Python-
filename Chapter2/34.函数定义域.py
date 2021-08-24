def func():
    print("沙河高晓松")


def handler():
    print("昌平吴彦祖")

    def inner():
        print("朝阳大妈")
        inner()

    func()
    print("海淀网友")


handler()