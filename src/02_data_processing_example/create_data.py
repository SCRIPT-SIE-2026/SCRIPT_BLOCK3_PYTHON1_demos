import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def tricky_func(x, a, b):
    return np.exp(-a * x) * np.cos(b * x)


def create_data(n_points=101):
    x = np.linspace(0.0, 10.0, n_points)
    a = 0.1
    b = 2.0 * np.pi * 0.5
    y = tricky_func(x, a, b)
    noise = np.random.normal(scale=0.1, size=y.shape)
    yn = y + noise
    data_dic = {"x": x, "y": y, "yn": yn}
    data = pd.DataFrame(data_dic)
    return data

data = create_data()


plt.figure()
plt.plot(data.x, data.y, "k-", label="solution")
plt.plot(data.x, data.yn, "or", label="solution + noise")
plt.grid()
plt.legend()
plt.savefig("raw_data.png")
