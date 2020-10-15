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
#柱状图数据
animal_speed={'dog':(48,'#7199cf'),
              'cat': (45, '#4fc4aa'),
               'cheetah': (120, '#e1a7a2')}
#分离数据
x_key = animal_speed.keys()

value = animal_speed.values()
print(value)
speed = [i[0] for i in value]
print(speed)
color = [i[1] for i in value]
print(color)
#绘制柱状图
bars = plt.bar(x_key,speed,width = 0.4,color = 'r',edgecolor = 'black')
#给每一个柱子赋予不同的颜色
for c,b in zip(color,bars):
    b.set_color(c)
#添加文字描述，'%d(km/h)'%y格式化输出文本，ha控制横向居中，va纵向在柱子顶端
for x,y in zip(x_key,speed):
    plt.text(x,y,'%d(km/h)'%y,ha = 'center',va = 'bottom')
#x,y 轴标签
plt.xlabel('animal')
plt.ylabel('speed')
#显示标题
plt.title('动物速度')
#显示图形
plt.show()
