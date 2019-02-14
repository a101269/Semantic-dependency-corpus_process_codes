import numpy as np


fr1 = open('G:\corpus\cuicui\\test1.txt', 'r', encoding="utf")
fr2 = open('G:\corpus\cuicui\\test2.txt', 'r', encoding="utf")
fw = open('G:\corpus\cuicui\cuicuiresult.txt', mode='a', encoding='utf')

lines=[]
recurr_nums=[]
lines2=[]
recurr_nums2=[]

for line in fr1.readlines():
    line = line.strip()
    lines.append(line)
for line in fr2.readlines():
    line = line.strip()
    lines2.append(line)

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


line_num=all_np(lines)
line_num2=all_np(lines2)
print(line_num)
print(line_num2)
print(len(line_num))
print(len(line_num2))

for k,v in line_num.items():
    recurr_nums.append(v)
nums_num=all_np(recurr_nums)

for k,v in line_num2.items():
    recurr_nums2.append(v)
nums_num2=all_np(recurr_nums2)

print(nums_num)
print(nums_num2)
fr2.close()
fr1.close()
fw.close()

