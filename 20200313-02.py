#!/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
#画布
#num 画布编号
# plt.figure(num=5,figsize=(14,6),clear=True,facecolor='pink')
# #plt.cla()
# plt.plot(np.arange(5),np.arange(5))
# plt.show()

#在画布中创建多个子图
# x = np.arange(100)
# ax1 = plt.subplot(221)
# ax1.plot(x,x)
# #xlabel,xlim,xticks
# #set_xlabel,set_xlim,set_xticklabels
# ax1.set_xlabel('X')
# #?????????????
# #ax1.set_xticklabels(['a','b','c','d','e','f'])
# ax1.set_xlim([50,100])
# ax1.set_title('yy')
# ax2 = plt.subplot(212)
# ax2.scatter(x,x)
# plt.show()
#
# fig = plt.figure()
# #polar,是否为极坐标
# ax1  = fig.add_subplot(221,polar = True)
# ax2 = fig.add_subplot(2,2,2)
# #hist()条形图
# ax2.hist(np.random.randn(100),bins=10,color='green',alpha = 0.3)
# plt.show()


#图中图
fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]
left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1=fig.add_axes([left,bottom,width,height])
ax1.set_title('area1')
ax1.plot(x,y,'r')

left,bottom,width,height = 0.2,0.6,0.25,0.25
ax2=fig.add_axes([left,bottom,width,height])
ax2.plot(x,y,'b')
ax2.set_title('area2')
plt.show()


#绘制等高线图
n = 256
#linspace()生成等差数列，（起始点，终点，生成个数,endpoint=False不包含终点）
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y =np.meshgrid(x,y)
print(np.meshgrid(x,y))
print('--------------------------------')
f = (1-X/2+X**5+Y**3)*np.exp(-X**2-Y**2)
print(f.shape)
#print(f)
# #绘制轮廓高度值
# plt.contourf(X,Y,f,cmap = 'hot')
# #绘制等高线
# C = plt.contour(X,Y,f,colors = 'black',linewidths = 1)
# #等高线上的数值
# plt.clabel(C)
# plt.show()






