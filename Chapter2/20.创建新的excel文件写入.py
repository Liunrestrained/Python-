from openpyxl import workbook

# 创建excel会默认创建一个sheet,名为Sheet，注意是大写S。
wb = workbook.Workbook()  # 此处后面的W是大写

sheet = wb.worksheets[0]  # 这是根据索引选中，也可以sheet = wb["Sheet"]选中
cell = sheet.cell(1, 1)  # 找到单元格，修改单元格的内容
cell.value = "新的开始"

wb.save(r"D:\draft\every.xlsx")
