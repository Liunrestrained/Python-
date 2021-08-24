from openpyxl import workbook

wb = workbook.Workbook()  # 创建sheet

# 修改Sheet名称会清空excel全部内容
sheet = wb.worksheets[0]
sheet.title = "数据集"  # 修改sheet名称
wb.save(r"D:\draft\every.xlsx")