'''在很多项目的源码中都会有 `import_module` 和 `getattr` 配合实现根据字符串的形式导入模块并获取成员，例如：'''
from importlib import import_module

path = "openpyxl.utils.exceptions.InvalidFileException"

module_path, class_name = path.rsplit(".", maxsplit=1)  # "openpyxl.utils.exceptions"   "InvalidFileException"
# rsplit为右边开始分割, maxsplit就是最大分割数
module_object = import_module(module_path)  # 使用字符串方式导入openpyxl.utils.exceptions

cls = getattr(module_object, class_name)  # 获取两者的成员

print(cls)
