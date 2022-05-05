
# AND, NAND, OR
# def AND(x1, x2):
    
#     w1, w2, theta = 0.5, 0.5, 0.7
#     tmp = x1*w1 + x2*w2
#     if tmp <= theta:
#         return 0
#     elif tmp > theta:
#         return 1

# print(AND(0,0))
# print(AND(1,0))
# print(AND(0,1))
# print(AND(1,1))



# import numpy as np
# x = np.array([0,1]) # 入力
# w = np.array([0.5,0.5]) # 重み
# b = -0.7
# print(w*x)
# print(np.sum(w*x))
# print(np.sum(w*x) + b)

import numpy as np

def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# print(NAND(1,0))

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
# print(OR(1,0))


# XOR >> パーセプトロンの限界
# 線形と非線形

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

# print(XOR(1,1))
# print(XOR(0,1))
# print(XOR(1,0))
# print(XOR(0,0))

# 第0層 > 第1層 > 第2層
# 活性化関数とは
## 入力信号の総和が発火するか判断

# ステップ関数 = 階段関数
# シグモイド関数

# パーセプトロンの活性化関数として、ステップ関数でなく、他の関数を用いればニューラルネットワークになる

import matplotlib.pylab as plt

# ステップ関数
# def step_function(x):
#     return np.array(x > 0, dtype=np.int)

# x = np.arange(-5.0, 5.0, 0.1)
# y = step_function(x)
# print(y)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()

# シグモイド関数

def sigmoid(x):
    return 1/(1 + np.exp(-x))

# x = np.arange(-5.0, 5.0, 0.1)
# y = sigmoid(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()
# x > neuron W > weight B > bias
X = np.array([1.0, 0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

A1 = np.dot(X,W1) + B1
# 活性化関数 >>> 1層目のoutput
# a > h() > z
Z1 = sigmoid(A1)

# 2層目
W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

A2 = np.dot(Z1,W2) + B2
Z2 = sigmoid(A2)

def identity_function(x):
    return x

W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])

A3 = np.dot(Z2,W3) + B3

Y = identity_function(A3)
print(Y)