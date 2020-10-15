#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
    实战：随机漫步

'''
import numpy as np
import matplotlib.pyplot as plt
#需求1：数据从0开始，每次步长为 1 或 -1，随机漫步100次，统计每次累计的步数。

data  = np.random.normal(0,1,100)
#print(data)
#data>0:1 data<0:-1
print(np.where(data>0,1,-1))
data =np.where(data>0,1,-1)
#累计求步数
print(data.sum())
print(data.cumsum())
#统计本次随机漫步的累计步数最小值和最大值。
print('------------------------------')
data_cumsum = data.cumsum()
print(data_cumsum.max())
print(data_cumsum.min())
#设置临界值为5，分析出第一次到达临界值（正负5均可）的步数。
data_cum_step = np.where(np.logical_or(data_cumsum>=5,data_cumsum<=-5))
print(data_cum_step)
print(data_cum_step[0][0])
x = np.arange(100)

# plt.plot(x,data_cumsum)
# plt.show()

#网格函数
arr1 = np.array([1,2])
arr2 = np.array([3,4])
#(1,3),(2,3),
# (1,4),(2,4)
print(np.meshgrid(arr1,arr2))

#imshow(),打印图片，打印热图的函数
points =np.arange(0,1,0.1)
print(points)
xs,ys = np.meshgrid(points,points)
print(xs)
print(ys)
arr2d = np.sqrt(xs**2+ys**2)
plt.imshow(arr2d,cmap='rainbow')
plt.colorbar()
plt.show()







