import numpy as np
import matplotlib.pyplot as plt

#Differential functions
def diff(y1,y2,y3):
    dy1dt = sigma*(y2-y1)
    dy2dt = roe*y1 - y2 - y1*y3
    dy3dt = -(beta*y3) + y1*y2
    return dy1dt, dy2dt, dy3dt

#Defining constants
sigma = 10
beta = 8/3
roe = 10

tf = 30 #Final time
N = 5000 #Step count
h = tf/N #Step

#Setting arrays for t and y values
t = np.linspace(0,tf,N)
y1s = np.zeros(N)
y2s = np.zeros(N)
y3s = np.zeros(N)

#Setting initial conditions
y1s[0] = 5
y2s[0] = 5
y3s[0] = 5

#Euler
for i in range(N-1):
    dy1dt, dy2dt, dy3dt = diff(y1s[i],y2s[i],y3s[i]) #Calculating gradients
    y1s[i+1] = y1s[i] + h*dy1dt
    y2s[i+1] = y2s[i] + h*dy2dt
    y3s[i+1] = y3s[i] + h*dy3dt
    
#Plotting
plt.plot(t, y1s, t, y2s, t, y3s)
plt.show()

plt.plot(y1s,y2s, y1s, y3s)
plt.show()