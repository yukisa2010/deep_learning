import numpy as np
import matplotlib.pylab as plt

# def function_1(x):
#     return np.sum(x**2)


# x = np.array([[1,2]])

# y = function_1(x)

# plt.plot(x, y)
# plt.show()


# # x0, x1それぞれに対する関数
# def function_tmp1(x0):
#     return x0*x0 + 4.0**2
# def function_tmp2(x1):
#     return 3.0**2.0 + x1*x1

# # 偏微分
# numerical_diff(function_tmp1, 3)
# numerical_diff(function_tmp2, 4)


# y = x**2があったとする
# x = 0, x = 2の時の傾きをそれぞれ求めたい

# limitを確認
# y = lim{h->0}( f(x+h) - f(x) / h)
# y = lim{h->0}(x**2 + 2hx + h**2 - x**2 / h)
# y = lim(2hx + h**2 / h)
# y = lim 2x + h
# y = 2x
# 傾きとxの関係 => 2x // 解析的微分

# 勾配(koubai)

def numerical_gradient(f, x):
    h = 1e-4 #0.0001
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)の計算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad


def function_2(x):
    return x[0]**2 + x[1]**2


def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    
    return x

init_x = np.array([-3.0, 4.0])
lr = 1e-10
x = gradient_descent(function_2, init_x=init_x, lr=lr, step_num=100)
print(x)







