import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def model(x,y):
    y_1 = y[0]
    y_2 = y[1]
    y_3 = y[2]
    f_1 = sigma*(y_2 - y_1)
    f_2 = roe*y_1 - y_2 - y_1*y_3
    f_3 = -(beta*y_3) + y_1*y_2
    return [f_1,f_2,f_3]

#Defining constants
sigma = 10
beta = 8/3
roe = 28

#Setting initial conditions
t0 = 0
t_final = 30
y0_1 = 5
y0_2 = 5
y0_3 = 5

#Solving
y = solve_ivp(model, [t0, t_final], [y0_1, y0_2, y0_3])

#Extracting t, y1, y2 and y3 values from y
t = y.t
y1 = y.y[0,:]
y2 = y.y[1,:]
y3 = y.y[2,:]

#Plotting
plt.plot(t, y1, t, y2, t, y3)
plt.show()

plt.plot(y1, y2, y1, y3)
plt.show()