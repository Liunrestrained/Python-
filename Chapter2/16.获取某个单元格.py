from openpyxl import load_workbook  # 导入三方模块

wb = load_workbook(r"D:\draft\nation.xlsx")  # 打开excel文件

sheet = wb.worksheets[0]  # 根据索引选中sheet

c1 = sheet["A1"]
print(c1.value)
