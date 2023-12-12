import numpy as np

def simps(f,a,b,N=50):
    if N % 2 == 1:
        raise ValueError("N mustbe an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] +
    4*y[1::2] + y[2::2])
    return S

def f(x):
    return x**2 + 4*x - 12

print(simps(f, -10, 10, 100000))