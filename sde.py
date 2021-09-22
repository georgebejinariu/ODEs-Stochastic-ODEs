# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:56:03 2020

@author: Asus
"""

import numpy as np
import sdeint
import matplotlib.pyplot as plt
a = 1.0
b = 10
r = 80.
S = 0.1
K = 10.
tspan = np.linspace(0.0, 100., 5000)
x0 = 8.5

def f(x, t):
    if t>10 and t < 10.2:
        return(r/K**2)*x*(K-x)*(x-S)-(b+0.1*t-2)*x
    #if t>20 and t < 20.2:
     #   return(r/K**2)*x*(K-x)*(x-S)-(b+0.1*t+6)*x
    if t>20 and t < 20.2:
        return(r/K**2)*x*(K-x)*(x-S)-(b+0.1*t-2)*x
    if t>60 and t < 60.2:
        return(r/K**2)*x*(K-x)*(x-S)-(b+0.1*t-2)*x
    if t>70 and t < 70.2:
        return(r/K**2)*x*(K-x)*(x-S)-(b+0.1*t-2)*x
    return (r/K**2)*x*(K-x)*(x-S)-(b+0.1*t)*x

def g(x, t):
    return -0.1*x

result1 = sdeint.itoint(f, g, x0, tspan)

result2 = sdeint.itoint(f, g, x0, tspan)
result3 = sdeint.itoint(f, g, x0, tspan)

def get_graphs():
    graphs = []
    for j in range(100):
        graphs.append(sdeint.itoint(f, g, x0, tspan))
    return graphs

plt.plot(tspan,result1)
plt.xlabel('t')
plt.ylabel('x')
#plt.xlim(left = 55, right = 75)
#plt.ylim(bottom = 5.2,top = 8.5)
#plt.xlim(left = 5, right = 25)
plt.ylim(bottom = 4.)
plt.show()


i = 2500
j = 2500+1250
sec = 125
sec_02 = 25

def rec_time(result,tspan):
    #4 shocks
    sec = int(len(tspan)/(tspan[-1]-tspan[0]))
    #print(sec)
    #shock 1: sec 10 - 10.2
    #check depth and recovery time
    s1 = result[10*sec-1]
    l1 = list(result[10*sec:int(10*sec+int(sec)/5)])
    i1 = int(10*sec+int(sec)/5)
    while(result[i1]<0.99*s1):
        l1.append(result[i1])
        i1 = i1+1
    rec_time1 = (i1 - 10*sec)/sec
    fall1 = s1 - min(l1)
    #shock 2
    s2 = result[20*sec-1]
    l2 = list(result[20*sec:int(20*sec+int(sec)/5)])
    i2 = int(20*sec+int(sec)/5)
    while(result[i2]<0.99*s2):
        l2.append(result[i2])
        i2 = i2+1
    rec_time2 = (i2 - 20*sec)/sec
    fall2 = s2 - min(l2)
    #shock 3
    s3 = result[60*sec-1]
    l3 = list(result[60*sec:int(60*sec+int(sec)/5)])
    i3 = int(60*sec+int(sec)/5)
    while(result[i3]<0.95*s3):
        l3.append(result[i3])
        i3 = i3+1
    rec_time3 = (i3 - 60*sec)/sec
    fall3 = s3 - min(l3)
    #shock 4
    s4 = result[70*sec-1]
    l4 = list(result[70*sec:int(70*sec+int(sec)/5)])
    i4 = int(70*sec+int(sec)/5)
    ok4 = 0
    while(result[i4]<0.99*s4):
        l4.append(result[i4])
        i4 = i4+1
        if i4>= len(tspan):
            ok4 +=1
            break
    i4 = int(70*sec+int(sec)/5)
    if ok4 ==1:
        i4 = int(70*sec+int(sec)/5)
        while(result[i4]<0.98*s4):
            l4.append(result[i4])
            i4 = i4+1
            if i4>= len(tspan):
                ok4 += 1
                break
    if ok4 ==2:
        i4 = int(70*sec+int(sec)/5)
        while(result[i4]<0.92*s4):
            l4.append(result[i4])
            i4 = i4+1
            if i4>= len(tspan):
                ok4 += 1
                break
    if ok4 ==3:
        i4 = int(70*sec+int(sec)/5)
        while(result[i4]<0.95*s4):
            l4.append(result[i4])
            i4 = i4+1
            if i4>= len(tspan):
                ok4 += 1
                break
    if ok4 ==4:
        i4 = int(70*sec+int(sec)/5)
        while(result[i4]<0.9*s4):
            l4.append(result[i4])
            i4 = i4+1
            if i4>= len(tspan):
                ok4 += 1
                break
    
    rec_time4 = (i4 - 70*sec)/sec
    fall4 = s4 - min(l4)
    return rec_time1, fall1, rec_time2, fall2, rec_time3, fall3, rec_time4, fall4


def avg_(graphs):
    Sr1 = 0
    Sr2 = 0
    Sr3 = 0
    Sr4 = 0
    Sf1 = 0
    Sf2 = 0
    Sf3 = 0
    Sf4 = 0
    for graph in graphs:
        r1,f1,r2,f2,r3,f3,r4,f4 = rec_time(graph,tspan)
        #rec_time1.append(r1)
        #rec_time2.append(r2)
        #rec_time3.append(r3)
        #rec_time4.append(r4)
        #fall1.append(f1)
        #fall2.append(f2)
        #fall3.append(f3)
        #fall4.append(f4)
        Sr1 = Sr1 +r1
        Sr2 = Sr2 +r2
        Sr3 = Sr3 +r3
        Sr4 = Sr4 +r4
        Sf1 = Sf1 +f1
        Sf2 = Sf2 +f2
        Sf3 = Sf3 +f3
        Sf4 = Sf4 +f4
    L = len(graphs)
    R1 = Sr1/L
    R2 = Sr2/L
    R3 = Sr3/L
    R4 = Sr4/L
    
    F1 = Sf1/L
    F2 = Sf2/L
    F3 = Sf3/L
    F4 = Sf4/L
    
    return R1,R2, R3, R4, F1, F2, F3, F4

#    
#graphs = get_graphs()
#
#
#print(avg_(graphs))




