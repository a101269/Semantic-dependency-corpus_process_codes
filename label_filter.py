fr = open('G:\corpus\新_自动标注结果\原版对照组\\seshi_label.txt', 'r', encoding="gbk")
fw = open('G:\corpus\新_自动标注结果\原版对照组\\seshi_label2.txt', mode='w', encoding='gbk')

lines = fr.read()
sents = lines.strip().split("\n\n")
print(len(sents))
for sent in sents:
    words = sent.strip().split("\n")
    label_flag=0
    for word in words:
        items = word.strip().split("\t")
        if items[7]=="eAdvt" or items[7]=="Comp" or items[7]=="dComp":
            label_flag=1
            break
    if label_flag==1:
        print(sent)
        fw.write(sent+"\n\n")
fr.close()
fw.close()
