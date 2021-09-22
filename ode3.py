# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:18:56 2020

@author: Asus
"""

#solve dx/dt = 3exp(-t) 
#      dy/dt = 3-y(t)
#   x(0) = 0 y(0) = 0

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#function that returns dz/dt
def model(z,t):
    dxdt = 3.0*np.sin(t)
    dydt = -z[1] + 3
    dzdt =[dxdt,dydt]
    return dzdt

#init cond
z0 = [0,0]

#time points
t = np.linspace(0,5)

#solve ODE
z = odeint(model,z0,t)

#plot results

plt.plot(t,z[:,0],'b-',label = '1')
plt.plot(t,z[:,1],'r--', label = '2')
plt.ylabel('response')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()


