#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.naive_bayes import GaussianNB, MultinomialNB


if __name__ == "__main__":
    np.set_printoptions(edgeitems=10)
    np.random.seed(0)
    M = 200
    N = 1000
    x = np.random.randint(2, size=(M, N))     # [low, high)
    x = np.array(list(set([tuple(t) for t in x])))
    M = len(x)
    # y = np.arange(M)
    y = [0, 1, 2] * int((float(M)/3)+1)
    print(len(y))
    y = np.array(y[0:M])
    print('样本个数：%d，特征数目：%d' % x.shape)
    print('样本：\n', x)
    # mnb = MultinomialNB(alpha=1)    # 动手：换成GaussianNB()试试预测结果？
    mnb = GaussianNB()    # 动手：换成GaussianNB()试试预测结果？
    mnb.fit(x, y)

    test_x = np.random.randint(2, size=(10, N))     # [low, high)
    test_x = np.array(list(set([tuple(t) for t in x])))
    y_hat = mnb.predict(test_x)
    print('预测类别：', y_hat)
    print('准确率：%.2f%%' % (100*np.mean(y_hat == y)))
    print('系统得分：', mnb.score(test_x, y_hat))

