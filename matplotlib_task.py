import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

labels = ['最底层','第2层','第3层','第4层','第5层','第6层','第7层','第8层','第9层','第10层','不知道','未回答']
sizes = [124,224,330,363,419,315,184,83,6,7,90,155]
explode = (0,0,0,0,0,0,0,0,0.1,0.2,0,0)
plt.axis("equal")
plt.pie(sizes,labels=labels,explode=explode,autopct="%1.1f%%", shadow=False,startangle=150)
# plt.title("家庭收入水平所在层次")
plt.show()