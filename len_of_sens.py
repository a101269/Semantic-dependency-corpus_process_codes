# 从文件中加载数据
fr = open("G:\data\产品评论语料_10000.txt", 'r',encoding="gbk")
fw = open('产品评论结果.txt', mode='w', encoding='gbk')
n=0
sum_len=0
for line in fr.readlines():
    line = line.strip()
    l=len(line)
    sum_len+=l
    n+=1
    line = line + "\n"
    fw.write(line)  # 写完通过\n进行换行
print("总行数：",n)
print("总字数：",sum_len)
print("平均每行长度：",sum_len/n)