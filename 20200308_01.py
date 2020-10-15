#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
    1.pycharm就是一个集成开发环境，并不是python
      vscode（另外一个软件）
    2.numpy和数组中有些函数同名，但是现象不同，是因为他们存在的位置不一样，定义的方式不一样的
'''
# import  numpy as np
# arr = np.array([4,6,3])
# arr.sort()
# print(arr)
# print(arr.sort())
# ####################
# print(np.sort(arr))

import matplotlib.pyplot as plt
import numpy as np
arr = np.arange(5)
#plt.plot(arr)
#plt.savefig(路径),将图片保存在电脑相应的路径下
#plt.savefig('图片.png')
#展示绘图
#plt.show()

print('绘制点线图')
x = np.arange(0,10,0.1)
y = np.sin(x)
#marker ,点的形状,color 颜色,alpha透明度【0，1】,linestyle线的类型，linewidth线的宽度，label线的标签
plt.plot(x,y,color = 'pink',alpha = 0.3,linewidth = 5,label = 'sin',linestyle='--')

#显示图例
#生成cos图像，点的形状*，颜色 green，线宽3，透明0.7，标签‘cos'
#将画布上的清空
plt.cla()
y_2 = np.cos(x)
plt.plot(x,y_2,marker = '*',color ='green',alpha =0.7,linewidth = 3,label ='cos')
#成功展示负号
plt.rcParams['axes.unicode_minus']=False
#控制x轴的取值范围，ylim（）
plt.xlim(-2,12)
#控制y轴的轴值显示，xticks（）
plt.yticks([-1,0,1],['min','0','max'])
plt.legend()
#增添网格
plt.grid(linestyle='--')
#取消x，y轴
#plt.axis('off')
#plt.show()

# plt.plot(x,y_2, 'yo--')
# plt.show()

#####绘制柱状图######
plt.cla()
animal_speed={'dog':(48,'#7199cf'),
              'cat': (45, '#4fc4aa'),
               'cheetah': (120, '#e1a7a2')}
x_key = animal_speed.keys()
print(x_key)
value = animal_speed.values()
print(value)
speed = [i[0] for i in value]
print(speed)
color = [i[1] for i in value]
print(color)
#绘制柱状图
bars = plt.bar(x_key,speed,width = 0.4,color = 'r',edgecolor = 'black')
#给每一个柱子赋予不同的颜色
# for c,b in zip(color,bars):
#     b.set_color(c)
#添加文字描述，'%d(km/h)'%y格式化输出文本，ha控制横向居中，va纵向在柱子顶端
for x,y in zip(x_key,speed):
    plt.text(x,y,'%d(km/h)'%y,ha = 'center',va = 'bottom')
#x,y 轴标签
plt.xlabel('animal')
plt.ylabel('speed')
#正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
#显示标题
plt.title('动物速度')
# plt.show()


#####饼装图######
plt.cla()
# 创建一个字典对象
pg_langs={'Java':(30,'#7B68EE'),'Python':(25,'#EEC900'),
                   'C#':(15,'#8E388E'),'PHP':(7,'#00CD66'),
                   'HTML5':(13,'#FF8C00'),'Database':(10,'#8B5A00')}
#各个部分的占比
per = [i[0] for i in pg_langs.values()]
#颜色的取值
colors =[i[1] for i in pg_langs.values()]
#赋予每一块一个标签，（标签，占比）
labels = [ '{}\n{}'.format(pg,per) for pg,per in zip(pg_langs.keys(),per)]
print(labels)
explode= [0,0,0,0.4,0,0]
#必选参数，占比（占比之和100），labels，各部分标签值，labeldistance，标签距离中间点的距离
#colors，注意加s，修改颜色；explode描述各部分距离中间点多长；shadow加不加阴影，默认为False
#radius，圆的半径，默认为1
plt.pie(per,labels =labels,labeldistance=0.5,colors= colors,explode = explode,shadow= False,radius=1)
plt.show()

######绘制散点图#####
plt.cla()
x =  np.random.randn(1,1000)
y =  np.random.randn(1,1000)
T =  np.arctan2(x,y)
plt.scatter(x,y,c=T,alpha = 0.4,marker='^')
plt.show()

#动态图
#阻塞模式
#动态图开始标志
plt.ion()
plt.show()

x = np.arange(0,10,0.1)
y = np.sin(x)
color = ['y','r','b','g']
for c in color:
    plt.plot(x,y,color=c)
    #暂停，pasue（时间）
    plt.pause(1)
#动态图结束标志
plt.ioff()
plt.show()
