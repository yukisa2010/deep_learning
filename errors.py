import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

t = np.array([0,0,1,0,0,0,0,0,0,0])
# y = np.array([0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0])
y = np.array([0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0])

# ans = mean_squared_error(np.array(y),np.array(t))
# print(ans)

# y = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]

# ans = mean_squared_error(np.array(y),np.array(t))
# print(ans)


def cross_entropy_error(y, t):
    delta = 1e-7 #-inf対策
    return -np.sum(t * np.log(y + delta))

print(cross_entropy_error(y, t))

