def dateprocess():
    # 从文件中加载数据
    fr = open('G:\corpus\yunhanoutput.txt', 'r', encoding="utf")
    # fw1 = open('G:\corpus\yunhannum.txt', 'w', encoding="utf")
    fw2 = open('G:\corpus\yunhanfirst.txt', 'w', encoding="utf")
    # fw3 = open('G:\corpus\yunhansecond.txt', 'w', encoding="utf")
    # fw4 = open('G:\corpus\yunhanlabel.txt', 'w', encoding="utf")
    for line in fr.readlines():
        # 返回移除字符串头尾指定的字符生成的新字符串
        line = line.strip()
        # 以 '\t' 切割字符串
        listFromLine = line.split('\t')
        # 每列的属性数据
        # fw1.write(listFromLine[0] + '\n')  # 字母数字编码
        fw2.write(listFromLine[0]+'\t'+listFromLine[1] + '\n'+listFromLine[0]+'\t'+listFromLine[2] + '\n')  # 第一句
        # fw2.write(listFromLine[0]+'\t'+listFromLine[2] + '\n')  # 第二句
        # fw4.write(listFromLine[3] + '\n')  # 标签


if __name__ == "__main__":
    dateprocess()
