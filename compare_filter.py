import re

fr = open('G:\corpus\新_自动标注结果\原版对照组\\yqyresult_5000_分词词性.txt', mode='r', encoding='utf')
fw = open('G:\corpus\新_自动标注结果\原版对照组\\yqyresult_5000_比较句.txt', 'w', encoding="utf")


'''
①不是（d）没/没有（d）±*/（n|v）±*/a
②*/（n|v）±*/（v或a）,*/（n|v）±也|也是±*/（同前一分句的谓词）
③*/（n|v）±*/p±*/（n|v）±都|都不
④*/（n|v）±不比/p±*/（n|v）±*/a

①不/没/没有（d副词）±平比特征词
②*/p±*/（n|v）±有|具有|存在±差别|区别|差异
③*/（n|v）±*/（a），但|但是|可是|不过|而|然而±*/（n|v）±*/（a）

①*/（n|a|v）±比/p
②*/（n|a|v）±*/p±*/（n|v）±相比|比较|比/v
③*/（n|v）更±*/（a|v）
④*/（n|v）±*/（a）于/p
⑤*/（n|v）±没|没有（d）±*/（n|v）±*/（a|v）
⑥*/（n/v）±没法|不能*/p±*/（n|v）±比|相比
⑦*/（n|v）±不及
⑧*/（n|v）±赶|比|抵/v不

①最±*/（a|v）
②最不± */（a|v）
'''
pattern1 = re.compile(r'(不是<d>(没|没有)<d>)(.*)(<n>|<v>)')
pattern2 = re.compile(r'((<n>|<v>)(.*)(<v>|<a>)，(.*)(<n>|<v>)(.*)(也|也是))')
pattern3 = re.compile(r'((<n>|<v>)(.*)(<p>)(.*)(<n>|<v>)(.*)(都|都不))')
pattern4 = re.compile(r'((<n>|<v>)(.*)(不比<p>)(.*)(<n>|<v>)(.*)(<a>))')
pattern5 = re.compile(r'((不|没有|没)<d>(.*)(似|相同|相等|相近|类似|一样|等于|等同|如|如同|同于|相似|差不多|抵得上))')
pattern6 = re.compile(r'(<p>(.*)(<n>|<v>)(.*)(有|具有|存在)(.*)(差别|区别|差异))')
pattern7 = re.compile(r'((<n>|<v>)(.*)(<a>)，(但|但是|可是|不过|而|然而)(.*)(<n>|<v>)(.*)<a>)')
pattern8 = re.compile(r'((<n>|<a>|<v>)(.*)(比<p>))')
pattern9 = re.compile(r'((<n>|<a>|<v>)(.*)(<p>)(.*)(<n>|<v>)(.*)(相比|比较|比)<v>)')
pattern10 = re.compile(r'((<n>|<v>)(更)(.*)(<a>|<v>))')
pattern11 = re.compile(r'((<n>|<v>)(.*)(<a>)(于<p>))')
pattern12 = re.compile(r'((<n>|<v>)(.*)(没|没有)(<d>)(.*)(<n>|<v>)(.*)(<a>|<v>))')
pattern13 = re.compile(r'((<n>|<v>)(.*)(没法|不能)(.*<p>)(.*)(<n>|<v>)(.*)(比|相比))')
pattern14 = re.compile(r'((<n>|<v>)(.*)(不及))')
pattern15 = re.compile(r'((<n>|<v>)(.*)(赶|比|抵)<v>不)')
pattern16 = re.compile(r'(最(.*)(<a>|<v>))')
pattern17 = re.compile(r'(最不(.*)(<a>|<v>))')

patterns=[pattern1,pattern2, pattern3, pattern4,pattern5, pattern6,
          pattern7,pattern8,pattern9,pattern10,pattern11,pattern12,
          pattern13,pattern14,pattern15,pattern16,pattern17 ]

#
# lines = ["①他不是<d>没有<d>你<n>善良<a>。","②他学习<n>很好<a>，我学习<n>也好<a>。","③我<n>和<p>他学习<n>都好。","④工人<n>不比<p>公务员收入<n>高<a>。","我和他不<d>一样。",
# "我和<p>他<n>有很大的区别。","我弟弟学习<n>很好<a>，但是我学习<n>很差<a>。","①中国的发展速度<n>比<p>美国快。",
#  "②中国<n>和<p>美国<n>相比<v>，发展速度快。","③但是，相比之下，朱耷的躲避<v>更是绝望<a>、更是凄楚。",
#  "④这款的性能<n>优<a>于<p>那款。","⑤他<n>没有<d>他爸<n>那么能吃苦<v>。","⑥张三<n>没法跟<p>李四<n>比。",
# "⑦当<v>工人不及经商。","⑧西湖的碧波漓江的水<n>，比<v>不上韶山冲里的清泉。", "①这么些个孩子，数你最淘气<a>。","②他最不爱喝茶<v>。"]
# # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# for l in lines:
#     matchObj = re.search(pattern15,l)
#     if matchObj:
#         print("matchObj.group() : ", matchObj.group())
#         print(l)
#     # print("matchObj.group(1) : ", matchObj.group(1))
#     # print("matchObj.group(2) : ", matchObj.group(2))
#     else:
#         print("No match!!")


i=0
for line in fr.readlines():
    line = line.strip()
    for pattern in patterns:
        matchObj = re.search(pattern, line)
        if matchObj:
            # print(matchObj.group())
            print(line)
            print("\n")
            fw.write(line+'\t'+str(i)+"\n")
            break
    i+=1
print("length："+str(i))
fr.close()
fw.close()

