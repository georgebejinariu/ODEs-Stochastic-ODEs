# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:37:43 2020

@author: Asus
"""


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dz/dt
def model(z,t,u):
    x = z[0]
    y = z[1]
    dxdt = (-x + u)/2.0
    dydt = (-y + x)/5.0
    dzdt = [dxdt,dydt]
    return dzdt

# initial condition
z0 = [0,0]

# number of time points
n = 401

# time points
t = np.linspace(0,40,n)

# step input
u = np.zeros(n)
# change to 2.0 at time = 5.0
u[51:] = 2.0

# store solution
x = np.empty_like(t)
y = np.empty_like(t)
# record initial conditions
x[0] = z0[0]
y[0] = z0[1]

# solve ODE
for i in range(1,n):
    # span for next time step
    tspan = [t[i-1],t[i]]
    # solve for next step
    z = odeint(model,z0,tspan,args=(u[i],))
    # store solution for plotting
    x[i] = z[1][0]
    y[i] = z[1][1]
    # next initial condition
    z0 = z[1]

# plot results
plt.plot(t,u,'g:',label='u(t)')
plt.plot(t,x,'b-',label='x(t)')
plt.plot(t,y,'r--',label='y(t)')
plt.ylabel('values')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()



def f(y,t,params):
    theta,omega = y
    Q,d,Omega = params
    derivs = [omega, -omega/Q+np.sin(theta)+d*np.cos(Omega*t)]
    return derivs

#parameters
Q=2.0
d=1.5
Omega = 0.65
#Bundle parameters for ODE
params = [Q,d,Omega]
#Initial values
theta0 = 0.0
omega0 = 0.0

#Bundle initial conditions for ODE solver
y0 = [theta0,omega0]
#Make time array for solution
tStop = 200.
tInc = 0.05
t = np.arange(0,tStop,tInc)
#Call the ODE solver
psoln = odeint(f,y0,t,args=(params,))
#Plot resutls
fig = plt.figure(1,figsize = (8,8))
#Plot theta as a function of time
ax1 = fig.add_subplot(311)
ax1.plot(t,psoln[:,0])
ax1.set_xlabel('time')
ax1.set_ylabel('theta')

#Plot omega as a function of time
ax2 = fig.add_subplot(312)
ax2.plot(t,psoln[:,1])
ax2.set_xlabel('time')
ax2.set_ylabel('omega')

#Plot pmega vs theta
ax3 = fig.add_subplot(313)
twopi = 2.0*np.pi
ax3.plot(psoln[:,0]%twopi,psoln[:,1],'.',ms=1)
ax3.set_xlabel('theta')
ax3.set_ylabel('omega')
ax3.set_xlim(0., twopi)

plt.tight_layout()
plt.show()







