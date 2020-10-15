#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
    数据集是2014-2019年，6年中电影票房排行前十的电影和票房记录；
    1-10是2019年电影排行，11-20是2018年电影排行，依次类推；
    需求：
    1.依次将6年电影票房生成柱状图（静态）和动态点线图（在同一个窗口）
    2.统计6年中，各个排名的总票房（例如，2014-2019年排名第一的总票房，共统计10个）
'''
import numpy as np
import matplotlib.pyplot as plt
#步骤一：获取.csv文件
#loadtxt()默认将.csv文件读取为float数据类型
data = np.loadtxt(r'D:\1-zr\晚班-02\电影排行榜.csv',str,delimiter=',')
#print(data)
#fig代表画布对象
fig = plt.figure()
#ax是子图对象
ax = fig.add_subplot(111)
x = np.arange(0,20,2)
box_office = data[:,1].astype('float32')
for i in range(6):
    #i取0，1，2，3，4，
    y= box_office[i*10:(i+1)*10]
    plt.bar(x+0.2*i,y,width=0.2,label='201'+str(9-i))
    print('---------------------------------------')
#更改x轴的刻度值，每个刻度在6年的柱状中间，第1名，第2名...第10名
x_label = []
for i in range(1,11):
    x_label.append('第'+str(i)+'名')
print(x_label)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xticks(x+0.5,x_label)
plt.legend()
# plt.show()

#动态生成点线图，依次展示每年票房得点线图
#不需要做到之前得点线图消失

plt.ion()
plt.show()

for i in range(6):
    y = box_office[i*10:(i+1)*10]
    #子图上所有曲线的列表
    #print('ax.lines:',type(ax.lines))
     #line生成直线的对象,line[0],绘制的直线
    if i!=0:
        ax.lines.remove(line[0])
    line = ax.plot(x+0.2*i,y,'o--',alpha = 0.4)
    #print(type(line))
    plt.pause(1)
plt.ioff()
plt.show()

#筛选数据，例如，2014-2019年排名第一6年的票房和，共统计10个
#（第一名：2019，2018，2017，2016，2015，2014）
#切片
sum=[]
for i in range(10):
    #[star:off:step]
    print(box_office[i::10])
    temp = np.sum(box_office[i::10])
    sum.append(temp)
print(sum)
plt.plot(x,sum,'ro--')
#y轴的值保留2位小数点
#在画布上添加本文
#sum = np.array(sum).round(2)
for x1,y1 in zip(x,sum):
    #plt.text(x轴，y轴，字符串)
    plt.text(x1+0.5,y1,'%.2f'%y1)
plt.show()