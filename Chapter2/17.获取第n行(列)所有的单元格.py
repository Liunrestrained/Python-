from openpyxl import load_workbook  # 导入三方模块

wb = load_workbook(r"D:\draft\nation.xlsx")  # 打开excel文件

sheet = wb.worksheets[0]

'''for i in sheet[1]:  # 循环第1列
    print(i.value)  # 打印内容

for f in sheet["A"]:  # 循环行A
    print(f.value)'''

'''for i in sheet.rows:  # 循环sheet所有行的数据
    print(i[0].value, i[1].value)  # 打印第一行内容与第二行内容'''

for i in sheet.columns:  # 循环sheet所有列的数据
    print(i[0].value, i[1].value, i[2].value)
