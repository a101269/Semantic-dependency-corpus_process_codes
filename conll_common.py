fr = open('G:\corpus\新_自动标注结果\原版对照组\\yqyresult_5000.txt', 'r', encoding="utf")
fw = open('G:\corpus\新_自动标注结果\原版对照组\\yqyresult_5000_分词词性.txt', mode='w', encoding='utf')

words = []
pos = []
for line in fr.readlines():
    line = line.strip()
    if not len(line):
        # word_pos = [(word + "|" + str(po) + " ") for po, word in zip(pos, words)]
        word_pos = [(word + "<" + str(po)+">" ) for po, word in zip(pos, words)]
        # print(word_pos)
        sentense = ''.join(word_pos)  # 'sep'.join(seq)以sep作为分隔符，将seq所有的元素合并成一个新的字符串
        # print(sentense)
        words = []
        pos = []
        fw.write(sentense + "\n")
    else:
        info = line.split("\t")
        words.append(info[1])
        pos.append(info[3])

fr.close()
fw.close()
