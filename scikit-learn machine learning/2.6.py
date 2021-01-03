'''
1.导入numpy
3.导入sklearn.linear_model   线性回归LinearRegression
4.实例化估计器类LinearRegression()对象model
5.实例化数组类array()对象X_train,并且整形n行1列
6.创建列表y_train
7.训练数据拟合模型fit(),X_train,y_train
5.实例化数组类array()对象X_test,并且整形n行1列
6.创建列表y_test
9.用score()方法，得出X_test,y_test的R方，r_squared,用来评价模型对另一组数据的预测能力
10.输出

用R方，评价测试集，大于0小于1的数
'''

import numpy as np
from sklearn.linear_model import LinearRegression

model = LinearRegression()
X_train = np.array([[6],[8],[10],[14],[18]])
y_train = [7,9,13,17.5,18]
model.fit(X_train,y_train)

X_test = np.array([[8],[9],[11],[16],[12]])
y_test = [11,8.5,15,18,11]
r_squared = model.score(X_test,y_test)
print('R方的值为: %.4f' % r_squared)