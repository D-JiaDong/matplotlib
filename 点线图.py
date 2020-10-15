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
#x坐标采样点生成
x=np.arange(0,11,0.2)
#计算对应y的正弦值
y=np.sin(x)
#控制图形格式为蓝色带星的虚线
plt.plot(x,y,c='9.2',marker='D',linestyle='--',linewidth=1,alpha=0.5,label='sin')
#显示label
plt.legend()
#横坐标说明
plt.xlabel('横坐标说明')
#纵坐标说明
plt.ylabel('纵坐标说明')
#显示图形
plt.show()
