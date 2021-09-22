# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:26:07 2020

@author: Asus
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.stats import norm
from brownian import brownian

#Forcings 

#QPF (3)

def qpforcing(t,omega,niu,d,kapa,q):
    P = 1
    for i in range(d-1):
        P = P * ((1 + np.sin(2* np.pi*(omega[i]+t*niu[i] )))/2)**q
    return kapa*P

#Random forcing(4)

#parameters of qpf
d1 = 3
theta1 = [10,4.3,2.12]
niu1 = [3.0,5.0,3.0]
kapa1 = 1.0
q1 = 2.0

#Param for sforcing
th0 = 3.14

#time
tStop = 10.
tInc = 0.05
t = np.arange(0,tStop,tInc)
#step input
   

#def qpf1(x,t):
#    dxdt = (r/(K**2))*x*(K-x)*(x-S)-(beta+kapa1*qpforcing(t,[0.3,0.3,0.12], [8.0,2.0,6.0],3,4.0,2))*x
#    return dxdt

def qpf(x,t):
    dxdt = (r/(K**2))*x*(K-x)*(x-S)-(beta+kapa1*qpforcing(t,theta1, niu1,d1,kapa1,q1))*x
    return dxdt

def nof(x,t):
    dxdt = (r/(K**2))*x*(K-x)*(x-S)-beta*x
    return dxdt

def stc(t, theta0):
    
    return (1+ np.sin(theta0 + t))

def sf(x,t):
    dxdt = (r/(K**2))*x*(K-x)*(x-S)-(beta+kapa1*(1+np.sin( th0 + norm.rvs(1) ))/1000 )*x
    return dxdt




#Init cond and parameters

x0 = 5

r = 80
K = 10.0
S = 0.1
beta = 19.0


x1 = odeint(nof,x0, t)

x2 = odeint(qpf,x0, t)

x3 = odeint(sf, x0, t)

plt.plot(t,x1)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.show()

plt.plot(t,x2)
plt.xlabel('time')
plt.ylabel('x(t) qpf')
plt.show()

plt.plot(t,x3)
plt.xlabel('time')
plt.ylabel('x(t) sf')
plt.show










