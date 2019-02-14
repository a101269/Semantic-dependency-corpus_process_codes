import os
from pyltp import Postagger,Segmentor

LTP_DATA_DIR = 'D:\\ltp_data'  # ltp模型目录的路径
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

segmentor = Segmentor()
postagger = Postagger()  # 初始化实例
postagger.load(pos_model_path)  # 加载模型
segmentor.load(cws_model_path)

fr = open('C:\\Users\\Administrator\\Desktop\\input.txt', 'r', encoding="utf")
fw = open('C:\\Users\\Administrator\\Desktop\\output.txt', mode='w', encoding='utf')
for line in fr.readlines():
    line = line.strip().split("\t")
    words = segmentor.segment(line[1])  # 分词
    postags = postagger.postag(words)  # 词性标注""
    for index, pos in enumerate(postags):
        fw.write(str(index+1) + "\t" + words[index] + "\t" + words[index] + "\t" + pos + "\t" + pos + "\t" + "_" +"\t" + "_" +"\t" + "_" + "\t" + "_" +"\t" + "_"+"\t"+ line[0]+"\n")  # 写完通过\n进行换行
    fw.write("\n")
fw.close()
postagger.release()  # 释放模型