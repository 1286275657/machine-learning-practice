'''
1.导入numpy
2.导入matplotlib.pyplot
3.实例化数组类array()对象X,并且整形n行1列
4.创建列表y
5.1.用figure()方法创建图表
5.2.用title()方法创建标题
5.3.添加x轴名称，xlabel
5.4.添加y轴名称, ylabel
5.5.绘制Y对x的标记，黑色点状 plot() k.
5.6.指定x，y轴范围,axis()
5.7.指定有网格,grid()
5.8.显示图表,show()
'''

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[6],[8],[10],[14],[18]])
y = [7,9,13,17.5,18]

plt.figure()
plt.title('Pizza price plotted against diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.plot(X,y,'k.')
plt.axis([0,25,0,25])
plt.grid(True)
plt.show()