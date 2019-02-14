import xlrd
import xlwt
from xlutils.copy import copy

# 只能读不能写
fr= open('G:\研究生\扶贫\身份证.txt', mode='r', encoding='utf')
name_id={}
for line in fr.readlines():
    line = line.strip()
    line=line.split("\t")
    if len(line)==1:
        pass
    else:
        name_id[line[0]] = line[1]
fr.close()
# print(name_id)


book = xlrd.open_workbook('G:\研究生\扶贫\东委村常住农户台账.xlsx')  # 打开一个excel
# book2 = xlwt.Workbook('G:\研究生\扶贫\新台账.xlsx')  # 打开一个excel
# book = copy(book0)#拷贝一份原来的excel
sheet = book.sheet_by_index(0)  # 根据顺序获取sheet
book2 = copy(book)#拷贝一份原来的excel
sheet2 = book2.get_sheet(0)#获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的

# print(sheet.cell(0, 0).value)  # 指定行和列获取数据
# print(sheet.cell(0, 1).value)
# print(sheet.cell(0, 2).value)
# print(sheet.cell(0, 3).value)
# print(sheet.ncols)  # 获取excel里面有多少列
# print(sheet.nrows)  # 获取excel里面有多少行
# print(sheet.get_rows())
n=0
for i in sheet.get_rows():
    n+=1
    if i[4].value in name_id :
        # i[12].value=name_id[i[4].value]
        sheet2.write(n, 13, name_id[i[4].value])
    else:
        pass

# print(sheet.row_values(0))  # 获取第一行
# for i in range(sheet.nrows):  # 0 1 2 3 4 5
#     print(sheet.row_values(i))  # 获取第几行的数据
#
# print(sheet.col_values(1))  # 取第一列的数据
# for i in range(sheet.ncols):
#     print(sheet.col_values(i))  # 获取第几列的数据
# sheet.write(1,3,0)
# sheet.write(1,0,'hello')
book2.save("G:\研究生\扶贫\新东委村常住农户台账.xls")

