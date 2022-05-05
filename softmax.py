def softmax(a):
    # exp_a = exp(a)
    # sum_exp_a = np.sum(exp_a)
    # y = exp_a / sum_exp_a

    # オーバーフロー対策
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = sum(exp_a)
    y = exp_a / sum_exp_a

    return y

