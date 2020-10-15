#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure()
# ax = Axes3D(fig)
# x = np.arange(0,7)
# y = np.random.uniform(2,20,7)
# for c,z in zip(['r','y','b','g'],[0,5,15,25]):
#     ax.bar(x,y,zs=z,zdir='y',color=c,alpha=0.8)
# ax.set_xlabel('X')
# ax.set_zlabel('Z')
# #ax.set_xticklabels
# #plt.xticks([轴值],[标签])
# ax.set_zticks([1,2,3])
# ax.set_zticklabels(['a','b','c'])
# plt.show()


# plt.plot([1,2,3],[2,3,4])
# plt.show()
'''
    使用axisartist包对画布上坐标轴进行修改

'''
#axisartist
from mpl_toolkits import  axisartist
fig = plt.figure(figsize=(8,8))
#使用axisartist.Subplot方法创建一个绘图对象
ax = axisartist.Subplot(fig,111)
fig.add_axes(ax)
#ax.axis[:],代表画布上的轴线
#['right','left','top','bottom']
#set_visible(False),某个轴值是否可见
ax.axis[:].set_visible(False)
#添加新的轴值ax.new_floating_axis(nth_coord,value)
#nth_coord,0是X轴方向，1是Y轴方向
#value代表轴值的位置,如果是X轴方向，value代表对应于Y轴的位置，如果是Y轴方向，value代表对应于X轴的位置
ax.axis['x'] = ax.new_floating_axis(nth_coord=0,value=0)
ax.axis['y'] = ax.new_floating_axis(1,0)  #x,y轴交点是（0，0）
plt.rcParams['font.sans-serif'] = ['SimHei']
#增加轴值标签，修改颜色
ax.axis['x'].label.set_text('x轴')
ax.axis['x'].label.set_color('blue')
#在轴上增加箭头axisline_style()
ax.axis['x'].set_axisline_style('-|>',size = 1.0)
ax.axis['y'].set_axisline_style('-|>',size = 1.0)
#修改刻度值的位置
#bottom,top
ax.axis['x'].set_axis_direction('bottom')
#left,right
ax.axis['y'].set_axis_direction('left')
x = np.arange(-15,15,0.1)
y = np.sin(x)
plt.plot(x,y,c='black')
plt.rcParams['axes.unicode_minus'] = False
plt.xlim(-8,8)
plt.ylim(-1,1)
plt.show()