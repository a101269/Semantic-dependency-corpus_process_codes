import xlrd
import numpy as np

def all_np(arr):
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result

book = xlrd.open_workbook('G:\研究生\Python\\1.xlsx')  # 打开一个excel
sheet = book.sheet_by_index(0)  # 根据顺序获取sheet

answers=[]
for i in sheet.get_rows():
    # print(i[0].value)
    answers.append(i[0].value)

line_num=all_np(answers)
print(line_num)