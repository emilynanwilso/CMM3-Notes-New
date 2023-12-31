import numpy as np
import math
import matplotlib.pyplot as plt

#Differential function for equation 2B
def diff2B(w,theta):
    dthetadt = w
    dwdt = -(g/l)*np.sin(theta)
    return dthetadt, dwdt

#Differential function for equation 2C
def diff2C(w,theta):
    dthetadt = w
    dwdt = -(g/l)*theta
    return dthetadt, dwdt

#Constants
g = 9.81
l = 9.81

#Interval stuff
h = 0.001
tf = 30
N = math.ceil(tf/h)

#time array
t = np.linspace(0,tf,N)

#w and theta array for 2B
theta2B = np.zeros(N)
w2B = np.zeros(N)

#w and theta array for 2C
theta2C = np.zeros(N)
w2C = np.zeros(N)

#Initial conditions (for w they are already 0)
theta2B[0] = np.pi/4
theta2C[0] = np.pi/4

#Euler for equation 2B
for i in range(N-1):
    dthetadt, dwdt = diff2B(w2B[i],theta2B[i])
    w2B[i+1] = w2B[i] + dwdt*h
    theta2B[i+1] = theta2B[i] + dthetadt*h
    
#Euler for equation 2C
for i in range(N-1):
    dthetadt, dwdt = diff2C(w2C[i],theta2C[i])
    w2C[i+1] = w2C[i] + dwdt*h
    theta2C[i+1] = theta2C[i] + dthetadt*h

#Plotting w
plt.plot(t,w2B,t,w2C)
plt.title('w')
plt.show()

#Plotting theta
plt.plot(t,theta2B,t,theta2C)
plt.title('theta')
plt.show()

#Comparing values at t = 10, 20 and 30
#The min(range(len stuff is to find the index of the value in t which is closest to
#the desired value (10 for the first 4, 20 for the next etc.)
print('At t=10s, the value for w at Eq2B is',w2B[min(range(len(t)), key=lambda i: abs(t[i] - 10))])
print('At t=10s, the value for w at Eq2C is',w2C[min(range(len(t)), key=lambda i: abs(t[i] - 10))])
print('At t=10s, the value for theta at Eq2B is',theta2B[min(range(len(t)), key=lambda i: abs(t[i] - 10))])
print('At t=10s, the value for theta at Eq2C is',theta2C[min(range(len(t)), key=lambda i: abs(t[i] - 10))])

print('\nAt t=20s, the value for w at Eq2B is',w2B[min(range(len(t)), key=lambda i: abs(t[i] - 20))])
print('At t=20s, the value for w at Eq2C is',w2C[min(range(len(t)), key=lambda i: abs(t[i] - 20))])
print('At t=20s, the value for theta at Eq2B is',theta2B[min(range(len(t)), key=lambda i: abs(t[i] - 20))])
print('At t=20s, the value for theta at Eq2C is',theta2C[min(range(len(t)), key=lambda i: abs(t[i] - 20))])

print('\nAt t=30s, the value for w at Eq2B is',w2B[min(range(len(t)), key=lambda i: abs(t[i] - 30))])
print('At t=30s, the value for w at Eq2C is',w2C[min(range(len(t)), key=lambda i: abs(t[i] - 30))])
print('At t=30s, the value for theta at Eq2B is',theta2B[min(range(len(t)), key=lambda i: abs(t[i] - 30))])
print('At t=30s, the value for theta at Eq2C is',theta2C[min(range(len(t)), key=lambda i: abs(t[i] - 30))])