#获取csv文件
import numpy as np
import matplotlib.pyplot as plt
data =np.loadtxt(r'D:\python视频\电影排行榜.csv',str,delimiter=',')
# print(data)
# name=[]
# num=[]
# x=np.array([i[0] for i in data])
# y=np.array([i[1] for i in data])
# for i in range(6):
#     name.append(x[i*10:(i+1)*10])
#     num.append(y[i*10:(i+1)*10])
# print(name)
# print(num)

# num=data[:,1].astype('float32')
#
# x_label=[]
# for i in range(1,11):
#     x_label.append('第'+str(i)+'名')
# plt.rcParams['font.sans-serif']=['SimHei']
# x = np.arange(0, 20, 2)
# ax=plt.subplot()
# for i in range(6):
#     movie = data[i * 10:(i + 1) * 10, :]
#     y = num[i * 10:(i + 1) * 10]
#     plt.bar(x + 0.2 * i, y, width=0.2, label='201' + str(10 - i - 1))
# plt.ion()
# plt.show()
# for j in range(6):
#     y = num[j * 10:(j + 1) * 10]
#     plt.xticks(x + 0.5, x_label)
#     if j!=0:
#          ax.lines.remove(line[0])
#     line=ax.plot(x+0.2*j,y,'o--',alpha=0.4)
#     plt.pause(1)
#     plt.legend()
# plt.ioff()
# plt.show()

num=data[:,1].astype('float32')
# print(num)
# for i in range(10):
#     arr=np.zeros(60)
#     for j in range(6):
#         arr[j*10+i]=1
#     arr1=num[arr==1]
#     print(arr1.sum())
print('........................')
li=[]
arr1=num.reshape(6,-1)
print(arr1)
for i in range(10):
    li.append(arr1[:,i].sum())

li=np.array(li).round(2)
print(li)

x=range(10)
plt.plot(x,li,'ro--')
x_=[]
for i in range(1,11):
    x_.append('NO'+str(i))
for x1,y1,i in zip(x,li,range(10)):
    plt.text(x1,y1,'%.2f'%li[i])
plt.xticks(x,x_)
plt.show()
