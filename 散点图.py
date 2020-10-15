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

x =  np.random.randn(1,1000)
y =  np.random.randn(1,1000)
T =  np.arctan2(x,y)
print(T)
plt.scatter(x,y,c=T,s=25,alpha = 0.4,marker='^')
plt.show()