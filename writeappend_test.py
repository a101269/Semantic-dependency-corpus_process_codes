fr = open('G:\corpus\新_自动标注结果\原版对照组\\tcslresult_5000_分词词性.txt', 'r', encoding="utf")
fw = open('G:\corpus\新_自动标注结果\原版对照组\词袋.txt', mode='a', encoding='utf')

for line in fr.readlines():
    line = line.strip().split('\n')
    for word_pos in line:
        word=word_pos.split('|')[0]
        fw.write(word+" ")

fr.close()
fw.close()

