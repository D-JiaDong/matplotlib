#导入matploylib模块
import matplotlib as mpl
#导入pyplot模块
import matplotlib.pyplot as plt
#导入numpy模块
import numpy as np
#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
#用来正常显示负号
plt.rcParams['axes.unicode_minus']=False
# 创建一个字典对象
pg_langs={'Java':(30,'#7B68EE'),'Python':(25,'#EEC900'),
                   'C#':(15,'#8E388E'),'PHP':(7,'#00CD66'),
                   'HTML5':(13,'#FF8C00'),'Database':(10,'#8B5A00')}
#各个部分的占比
per = [i[0] for i in pg_langs.values()]
print(per)
#颜色的取值
colors =[i[1] for i in pg_langs.values()]
print(colors)
#赋予每一块一个标签，（标签，占比）
labels = [ '{}\n{}'.format(pg,per) for pg,per in zip(pg_langs.keys(),per)]
print(labels)
explode= [0,0,0,0.4,0,0]
#必选参数，占比（占比之和100），labels，各部分标签值，labeldistance，标签距离中间点的距离
#colors，注意加s，修改颜色；explode描述各部分距离中间点多长；shadow加不加阴影，默认为False
#radius，圆的半径，默认为1
plt.pie(per,labels =labels,labeldistance=0.5,colors= colors,explode = explode,shadow= False,radius=1)
plt.show()