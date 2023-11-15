import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


df = pd.read_csv (r'res/dane_pomiarowe.csv', sep="\t")
#Rzutowanie danych z kolumny z czasem i kolumny z przyśpieszeniem na wektory
np.array
t = np.array(df['t'])
a = np.array(df['a'])

a=2
b=-7
amp=10

x = np.linspace(-10,10,100)

y=a*x**2 + b + amp*(np.random.rand(len(x))-0.5)


def func(x, a, b):
    return a*x**2 + b

p0=[1,1]

fit_params, covariance_matrix = curve_fit(func, x, y, p0=p0)


print("paramsy: \na=", fit_params[0], "\nb=", fit_params[1])


plt.scatter(x,y)

plt.plot(x, func(x, *fit_params), 'r')

plt.show()