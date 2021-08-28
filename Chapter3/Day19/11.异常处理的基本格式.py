# 常用简单格式：（使用较多）
try:
    '''逻辑代码'''
except Exception as e:
    '''try逻辑代码出现问题，则执行此代码，没有异常则不执行。'''

# 完整格式：（使用较少）
try:
    '''逻辑代码'''
except Exception as e:
    '''异常处理'''
finally:
    '''无论try中的代码运行是否出现问题，此处都会照常执行，此举一般用于资源的释放'''
print("end")

# 举例：
try:
    file_object = open("xx.txt")
    # ...
except Exception as e:
    '''异常处理'''
finally:
    file_object.close()  # try中没有出现异常，最后执行关闭文件；try中出现异常，执行except异常处理，再关闭文件。
