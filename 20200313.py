#!/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


data = {1:[30,15,60],2:[16,22,50],3:[110,90,160],
        4:[80,120,110],5:[40,80,90],6:[80,100,75],
        7:[120,76,130],8:[130,110,180],9:[120,210,192],
        10:[50,80,101],11:[80,60,60],12:[135,150,100]}

months = data.keys()
months=list(months)
print(months)
value = data.values()
print(value)
y_north = [i[0] for i in value]
y_east = [i[1] for i in value]
y_sorth =[i[2] for i in value]
#每各月份，3家公司的平均值
mean = [np.mean(i) for i in value]
print(mean)
#绘制点线图
plt.plot(months,y_north,color ='r',alpha = 0.6,marker = 'o',label = 'north')
plt.plot(months,y_east,color ='y',alpha = 0.6,marker = 'o',label = 'east')
plt.plot(months,y_sorth,color ='g',alpha = 0.6,marker ='o',label = 'sorth')
plt.plot(months,mean,color = 'grey',alpha = 0.6,marker = 'o',label = 'mean')
plt.legend()
plt.grid(linestyle = '--')
plt.title('report of scale')
plt.xlabel('months')
plt.ylabel('scale')
months = list(months)
print(months)
group_months =['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sep','Oct','Nov','Dec']
plt.xticks(months,group_months,rotation = -45)
plt.show()



