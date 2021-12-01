import matplotlib.pyplot as plt
from numpy import *
import numpy as np


def f(x):
    return 5*sin(10*x)*sin(3*x)


t = np.arange(0 , 4) 
y = f(t)

plt.plot(t, y, 'm')

plt.xlabel('t')
plt.ylabel('y')
plt.title('Y(x)=5*sin(10*x)*sin(3*x)/(x^(1/2)), x=[0...4]')

plt.show()