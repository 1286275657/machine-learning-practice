'''
1.导入numpy
2.导入matplotlib.pyplot
3.导入sklearn.linear_model   线性回归LinearRegression
4.实例化估计器类LinearRegression()对象model
5.实例化数组类array()对象X,并且整形n行1列
6.创建列表y
7.训练数据拟合模型fit()
8.创建解释变量数组类型array()对象test_pizza
9.用predict()方法，开始预估价格
10.输出预测值
11.输出模型预测值和实际值之差的平方，的平均数  即为残差平方和RSS

残差平方和  RSS   residual sum of square
'''

import numpy as np
from sklearn.linear_model import LinearRegression

model = LinearRegression()
X = np.array([[6],[8],[10],[14],[18]])
y = [7,9,13,17.5,18]
model.fit(X,y)

test_pizza = np.array([[12]])
predict_price = model.predict(test_pizza)
print('A 12" pizza should cost: $%.2f' % predict_price)
print('Residual sum of square: %.2f' %np.sum((model.predict(X)-y)**2))