'''
1.导入numpy
2.实例化数组类array()对象X,并且整形n行1列
3.实例化数组类array()对象y
4.计算X平均值x_bar
5.计算方差
6.输出平均值和方差
7.用numpy库中的var方法计算，ddof设置克塞尔校正
8.计算y平均值
9.计算X和y的协方差
10.输出协方差
11.用numpy库中的cov方法计算协方差


方差 衡量一组值的偏离程度，越小则值越接近平均数  
    差的分母为个数减1，为贝塞尔校正

协方差  如果两组值一起增加协方差为正，相反则为负。
两个量没有线性关系则协方差为0
'''

import numpy as np

X = np.array([[6],[8],[10],[14],[18]])
y = np.array([7,9,13,17.5,18])

x_bar = X.mean()
variance = ((X-x_bar)**2).sum()/(X.shape[0]-1)
print('X的平均值为%.2f'%x_bar)
print('方差的值为%.2f'%variance)
print('var方法方差为：')
print(np.var(X,ddof=1))

y_bar = y.mean()
covariance = np.multiply((X-x_bar).transpose(),y-y_bar).sum()/(X.shape[0]-1)
print('协方差的值为%.2f'%covariance)
print('cov方法协方差值：')
print(np.cov(X.transpose(),y)[0][1])