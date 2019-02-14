# import docx
#
# def get_docx(file_name):
#     d = docx.opendocx(file_name)
#     doc = docx.getdocumenttext(d)
#     return doc
#
# doc = get_docx('1.docx')
# print(doc)  # 输出行数：1075
# for d in doc[:]:
#     print(d) # 打印前5行
#
fr = open('1.txt', 'r',encoding='utf')
fw = open('G:\corpus\新_自动标注结果\原版对照组\词袋.txt', mode='w', encoding='utf')

for line in fr.readlines():
    print(line)

fr.close()
fw.close()

