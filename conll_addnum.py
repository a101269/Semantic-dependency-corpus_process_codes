fr1 = open('G:\corpus\yunhan_ori\yunhan_five', 'r', encoding='utf')
fr2 = open('G:\corpus\yunhan_ori\yunhan_five.conllu.sem16', 'r', encoding='utf')
fw = open('G:\corpus\yunhan_ori\yunhan_five.conllu.sem16_addnum', mode='w', encoding='utf')

lines1 = fr1.read()
lines2 = fr2.read()
sents1 = lines1.strip().split("\n\n")  # 每行句子最后一个词换行后，又换行（空行),所以\n\n,否则无法切分各个句子
sents2 = lines2.strip().split("\n\n")

number = []  # 编号
number_set = []  # 编号
n = 0
for sent in sents1:
    # sentences.append([])
    words = sent.strip().split("\n")
    for word in words:
        items = word.strip().split("\t")
        number.append(items[10].encode('utf-8').decode('utf-8-sig'))
        n += 1
    number_set.append(number[-1])
print(number_set)

n = 0
for sent in sents2:
    words = sent.strip().split("\n")
    for word in words:
        word += "\t" + number_set[n] + "\n"
        fw.write(word)
    n += 1
    fw.write("\n")

fr1.close()
fr2.close()
fw.close()
