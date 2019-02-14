import operator


def output(outfile, sents):
    fo = open(outfile, "w")
    for sent in sents:
        for idx, tok in enumerate(sent):
            line = str(tok["idx"]) + "\t" + tok["tok"] + "\t" + tok["tok"] + "\t" + tok["pos"] + "\t" + tok[
                "pos"] + "\t_\t" + str(tok["hed"]) + "\t" + tok["rel"] + "\t_\t_\n"
            fo.write(line)
        fo.write("\n")


def process(infos):
    sents = []
    i = 0
    for info in infos:
        print(i)
        sent = []
        sent2 = []
        word_numbers=[]
        i += 1
        for rel in info["result"]:
            if rel=="":
                pass
            else:
                for tok in info["tokens"]:
                    # print(tok)
                    token = tok.split("]")[1].split("/")
                    # print(token)
                    if token[0] == "Root":
                        pass
                    else:
                        sent.append({"tok": token[0], "pos": token[0]})  # [1]la/ws
                items = rel.split("_")
                # print(items)  # ['[0]Root', '[14]交谈(Root)'] ['[1]穿', '[3]衬衫(Pat)'
                index = int(items[1].split("]")[0].strip("["))  # index为 每行第 index个词的位置
                head = int(items[0].split("]")[0].strip("["))
                relation = items[1].split("(")[1].strip(")")
                word=items[1].split("(")[0].split("]")[1]
                # print(word,index, head, relation)  # 14 0 Root   3 1 Pat
                # print(word)
                word_numbers.append(index)
                for token in sent:
                    if token["tok"]==word:
                        # print(token)
                        sent2.append({"tok": word, "pos": token["pos"],"hed":head,"rel":relation,"idx":index})
                        break
        # print(word_numbers)
        if len(sent2)!=0:
            sorted_sent = sorted(sent2, key=operator.itemgetter('idx'))
            sents.append(sorted_sent)
    print("sents_length:"+str(len(sents)))
    # print(sents[0])
    return sents


if __name__ == "__main__":
    fi = open("G:\\corpus\\depend.csv", "r", encoding='utf')
    fo = open("G:\\corpus\\dependancy_test.txt", "w")
    fi = fi.read()
    sents = fi.strip().split("\n")
    infos = []
    for sent in sents:
        info = {}
        items = [it.strip("\"") for it in sent.strip().split(";")]
        # sentid	sent	dep_sent	res_sent	tag 	annoter 	time	skip	comment
        if items[7] == "1": continue  # skip the skipped sents
        info["tokens"] = items[1].strip().split()
        info["origin"] = items[2].strip().split("\t\t")
        info["result"] = items[3].strip().split("\t")
        infos.append(info)
        # fo.write(str(info["tokens"])+";"+str(info["origin"])+";"+str(info["result"])+"\n")
        fo.write(str(items[1])+";"+str(info["result"])+"\n")
    sents = process(infos)
    print(len(sents))
    # for sent in sents:
    #     for i in range(len(sent)):
    #         fo.write(str(sent[i]["hed"]) + "\n" + str(sent[i]))
        # fo.write(str(sent)+ "\n")
    output("G:\\corpus\\lannotated_test.conll", sents)

