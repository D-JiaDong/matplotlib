from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#画布
fig = plt.figure()
#3D转化
ax = Axes3D(fig)

x =np.array([0,1,2,3,4,5,6])
y = np.random.randint(2,20,size=7)
#print(x)
#print(y)
#zdir把哪个轴值变为z轴,,剩下的那个轴值位置在哪
for c,z in zip(['r','y','g','b'],[0,5,15,25]):
    ax.bar (x,y,zs=z,zdir='y',color=c,width=1)
plt.show()
#生成4个柱状图
#x = (0，1，2，3，4，5，6)
#随机生成，范围在【2，20】，生成7个数（2，20，7）
#生成4个柱状图，依次排列在y轴【0，5，15，25】
#['r','y','g','b']

