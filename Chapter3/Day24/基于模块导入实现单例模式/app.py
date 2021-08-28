from page import UFO  # 导入模块

print("第1", UFO)
import utils


def run():
    print("第3", UFO)


if __name__ == '__main__':
    run()

# 第1 <class 'page.UFO'>
# 第2 <class 'page.UFO'>
# 第3 <class 'page.UFO'>
