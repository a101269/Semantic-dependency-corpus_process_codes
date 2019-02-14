fr = open('G:\corpus\新_自动标注结果\原版对照组\\yqyresult_5000_比较句.txt', 'r', encoding="utf")

indexs=[]
for line in fr.readlines():
    index = line.strip().split("\t")[1]
    indexs.append(int(index))
print(indexs)
fr.close()

fr2=open('G:\corpus\新_自动标注结果\原版对照组\\yqyresult_5000.txt', 'r', encoding="utf")
fw=open('G:\corpus\新_自动标注结果\原版对照组\\yqyresult_5000_比较句labal.txt', 'w', encoding="utf")
lines = fr2.read()
sents = lines.strip().split("\n\n")
print(len(sents))

i=0
j=0
lenofinde=len(indexs)
for sent in sents:
    index = indexs[j]
    if i==index:
        labels=[]
        word_oris=[]
        words = sent.strip().split("\n")
        for word in words:
            items = word.strip().split("\t")
            label=items[7]
            word_ori=items[1]
            labels.append(label)
            word_oris.append(word_ori)
        # fw.write(sent+"\n\n")
        for k in word_oris:
            fw.write(k+"\t")
        fw.write("\n")
        for k in labels:
            fw.write(k+"\t")
        fw.write("\n")
        j+=1
        if j==lenofinde:
            break
    i+=1
fr2.close()
fw.close()