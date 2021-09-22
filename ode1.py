# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:26:16 2020

@author: Asus
"""

#find a num solution for dy/dt = -y+1 y(0) = 0
from functools import partial 
from collections import defaultdict 
import numpy as np # Numerical computing library
import matplotlib.pyplot as plt # Plotting library
import scipy.integrate #Integration library
from mpl_toolkits.mplot3d import axes3d #Used for the 3d bifurcation plot
import matplotlib.patches as mpatches #used to write custom legends
#function that returns dy/dt


def s_n_nform(x,r,a):
    '''x = vector, r = parameter'''
    return r - a*x**2

ic = 0
time = np.linspace(-10,10)

def get_root(func, init, param):
    '''func - function
    guess 
    param - parameters for func -> tuple'''  
    sol, info, convergence, sms = scipy.optimize.fsolve(func, init, args =param, full_output=1)
    if convergence == 1:
        return sol
    return np.nan

def get_roots(func, param, inits = np.arange(-10.1,10)):
    l = []
    for init in inits:
        r = get_root(func,init,param)
        ok = 1
        for el in l:
            if abs(r-el) < 0.0001:
                ok = 0
        if r is not np.nan and ok == 1:
            l.append(r)
    return l

ic = [-1,0,1]

        