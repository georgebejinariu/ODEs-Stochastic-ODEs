# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:25:28 2020

@author: Asus
"""


import numpy as np
import sdeint
import matplotlib.pyplot as plt
a = 1.0
b = 19.2
r = 80.
S = 0.1
K = 10.
tspan = np.linspace(0.0, 22, 2000)
x0 = 7.4

def f(x, t):
    if t>10 and t < 10.2:
        return(r/K**2)*x*(K-x)*(x-S)-(b - 2)*x
    return (r/K**2)*x*(K-x)*(x-S)-(b)*x

def g(x, t):
    return -.1*x

#result1 = sdeint.itoint(f, g, x0, tspan)
#
#result2 = sdeint.itoint(f, g, x0, tspan)
#result3 = sdeint.itoint(f, g, x0, tspan)

def get_graphs():
    graphs = []
    for j in range(200):
        graphs.append(sdeint.itoint(f, g, x0, tspan))
    return graphs

#plt.plot(tspan,result1, label = 'β = 14')
#plt.xlabel('t')
#plt.ylabel('x')
#plt.xlim(left = 55, right = 75)
#plt.ylim(bottom = 3.6,top = 8.3)
plt.legend(loc = 'best')
plt.show()


def rec_time(result,tspan):
    #4 shocks
    sec = int(len(tspan)/(tspan[-1]-tspan[0]))
    #print(sec)
    #shock 1: sec 10 - 10.2
    #check depth and recovery time
    s1 = result[10*sec-1]
    l1 = list(result[10*sec:int(10*sec+int(sec)/5)])
    i1 = int(10*sec+int(sec)/5)
    ok = 0
    while(result[i1] > 0.99*s1):
        l1.append(result[i1])
        i1 = i1+1
        if i1 == 1999:
            ok+=1
            break
    if ok == 1:
        return 'jump'
#    l1 = list(result[10*sec:int(10*sec+int(sec)/5)])
#    i1 = int(10*sec+int(sec)/5)
#    if ok == 1:
#        while(result[i1]<0.98*s1):
#            l1.append(result[i1])
#            i1 = i1+1
#            if i1 == 1999:
#                ok+=1
#    l1 = list(result[10*sec:int(10*sec+int(sec)/5)])
#    i1 = int(10*sec+int(sec)/5)
#    if ok == 2:
#        while(result[i1]<0.97*s1):
#            l1.append(result[i1])
#            i1 = i1+1
#            if i1 == 1999:
#                ok+=1
#    l1 = list(result[10*sec:int(10*sec+int(sec)/5)])
#    i1 = int(10*sec+int(sec)/5)
#    if ok == 3:
#        while(result[i1]<0.96*s1):
#            l1.append(result[i1])
#            i1 = i1+1
#            if i1 == 1999:
#                ok+=1
#    l1 = list(result[10*sec:int(10*sec+int(sec)/5)])
#    i1 = int(10*sec+int(sec)/5)
#    if ok == 4:
#        while(result[i1]<0.95*s1):
#            l1.append(result[i1])
#            i1 = i1+1
#            if i1 == 1999:
#                ok+=1
        
        
    
    rec_time1 = (i1 - 10*sec)/sec
    fall1 = s1 - min(l1)


    
    return rec_time1, fall1



def to_zero(result):
    
    if result[1999] < 0.1:
        return True
    else:
        return False
    
def avg_(graphs):
    Sr1 = 0
 
    
    Sf1 = 0
    
    L = len(graphs)


    for graph in graphs:
        if rec_time(graph,tspan) == 'jump':
            L = L-1
               
        elif not to_zero(graph):
            
            r1,f1= rec_time(graph,tspan)
            Sr1 = Sr1 +r1
            Sf1 = Sf1 +f1
        else:
            L = L - 1
            
        
        #rec_time1.append(r1)
        #rec_time2.append(r2)
        #rec_time3.append(r3)
        #rec_time4.append(r4)
        #fall1.append(f1)
        #fall2.append(f2)
        #fall3.append(f3)
        #fall4.append(f4)
        
    
    R1 = Sr1/L


    
    F1 = Sf1/L
 
    
    return R1, F1

#
##############
    
r = 80
K =10
S = 0.1


#b1 = 19.
#b = b1 
#u1 = get_graphs()
#print('b = ', b, ',rec_time and fall', avg_(u1) )
#
#
#b2 = 18.6
#b = b2 
#u2 = get_graphs()
#print('b = ', b, ',rec_time and fall', avg_(u2) )

#b3 = 18.3
#b = b3 
#u3 = get_graphs()
#print('b = ', b, ',rec_time and fall', avg_(u3) )
#
#b4 = 18.4
#b = b4
#u4 = get_graphs()
#print('b = ', b, ',rec_time and fall', avg_(u4) )
#
#b5 = 18.9
#b = b5
#u5 = get_graphs()
#print('b = ', b, ',rec_time and fall', avg_(u5) )
#
#b6 = 19.
#b = b6
#u6 = get_graphs()
#print('b = ', b, ',rec_time and fall', avg_(u6) )
#
#b7 = 19.1
#b = b7
#u7 = get_graphs()
#print('b = ', b, ',rec_time and fall', avg_(u7) )
#
#b8 = 19.2
#b = b8
#u8 = get_graphs()
#print('b = ', b, ',rec_time and fall', avg_(u8) )
#
#b9 = 19.3
#b = b9
#u9 = get_graphs()
#print('b = ', b, ',rec_time and fall', avg_(u9) )

###################################################
#r = 40 K = 10 S = 0.1

r = 40
K = 10
S = 0.1

b1 = 8.4
b = b1
u1 = get_graphs()
print('b = ', b, ',rec_time and fall', avg_(u1))

b2 = 8.5
b = b2
u2 = get_graphs()
print('b = ', b,',rec_time and fall', avg_(u2))

b3 = 9.2
b = b3
u3 = get_graphs()
print('b = ', b, ',rec_time and fall', avg_(u3) )

b4 = 9.3
b = b4
u4 = get_graphs()
print('b = ', b, ',rec_time and fall', avg_(u4) )

b5 = 9.4
b = b5
u5 = get_graphs()
print('b = ', b, ',rec_time and fall', avg_(u5) )


b6 = 9.5
b = b6
u6 = get_graphs()
print('b = ', b, ',rec_time and fall', avg_(u6) )


b7 = 8.5
b = b7
u7 = get_graphs()
print('b = ', b, ',rec_time and fall', avg_(u7) )

b8 = 8.6
b = b8
u8 = get_graphs()
print('b = ', b, ',rec_time and fall', avg_(u8) )

b9 = 8.7
b = b9
u9 = get_graphs()
print('b = ', b, ',rec_time and fall', avg_(u9) )

b10 = 8.9
b = b10
u10 = get_graphs()
print('b = ', b, ',rec_time and fall', avg_(u10) )

