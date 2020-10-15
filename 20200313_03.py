#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
    绘制3D图
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#3D点线图，画图时，需要用画布的名称'.'函数名
# fig = plt.figure()
# ax  = Axes3D(fig)
# X = np.arange(0,20,0.25)
# Y = np.arange(0,20,0.25)
# Z = np.sin(X**2+Y**2)
# ax.plot(X,Y,Z,color = 'pink',linestyle='--')
# plt.show()

#3D散点图
# fig = plt.figure()
# ax = Axes3D(fig)
#
# #在散点图中绘制两类数据 ，颜色和形状不同
# for c,m,zlow,zhigh in [('r','o',0,8),('b','^',7,15)]:
#     x = np.random.uniform(0,10,100)
#     y = np.random.uniform(0,10,100)
#     z = np.random.uniform(zlow,zhigh,100)
#     ax.scatter(x,y,z,color=c,marker=m)
# plt.show()

#表面图 ax.plot_subface()
# fig = plt.figure()
# ax = Axes3D(fig)
#
# x = np.arange(0,5,0.25)
# y = np.arange(0,5,0.25)
# print((np.meshgrid(x,y)[0]).shape)
# #生成40行，40列个坐标
# x,y = np.meshgrid(x,y)
# r = np.sqrt(x**2+y**2)
# z = np.sin(r)
# ax.plot_surface(x,y,z,cmap = 'coolwarm')
# plt.show()

#将多个2d图在3d图上展示
fig = plt.figure()
ax = Axes3D(fig)

x = np.arange(0,20,0.5)
y = np.sin(x)
#zdir把哪个轴值变为z轴,,剩下的那个轴值位置在哪
for c,z in zip(['r','y','b','g'],[30,20,10,0]):
    ax.plot(x,y,zs=z,zdir='y',color=c,alpha=0.8)
plt.show()



#生成4个柱状图，
#x = (0，1，2，3，4，5，6)
#随机生成，范围在【2，20】，生成7个数（2，20，7）
#生成4个柱状图，依次排列在y轴【0，5，15，25】
#['r','y','g','b']

