import numpy as np
import matplotlib.pyplot as plt
import Ex1
import Ex2
import Ex3
import Ex4

#Function to integrate
def f(x):
    return x**2 + 4*x - 12

#n value parameters
Min = 2
Max = 200
step = 2
N = int((Max-Min)/step+1)
n = np.linspace(Min,Max,N)

#Arrays for each method's errors
mid = np.zeros(N)
trap = np.zeros(N)
simp3 = np.zeros(N)
simp38 = np.zeros(N)

#Integral boundaries
a = -10
b = 10

#Getting the values for each n value for each method
for i in range(N):
    mid[i] = Ex1.rect_rule(f, a, b, int(n[i]))
    trap[i] = Ex2.trapz(f, a, b, int(n[i]))
    simp3[i] = Ex3.simps(f, a, b, int(n[i]))
    simp38[i] = Ex4.calculate(f, a, b, int(n[i]))

#Plotting
plt.plot(n,mid,n,trap,n,simp3,n,simp38)
plt.ylim(400,450)
plt.legend(['MidPoint Rule','Trapezoidal','Simpson Rule','3/8 Simpson'])
plt.show()