# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:20:55 2020

@author: Asus
"""


import numpy as np
import sdeint
import matplotlib.pyplot as plt
a = 1.0
b = 19.3
r = 40.
S = 0.1
K = 10.
tspan = np.linspace(0.0, 20.0, 3500)
x0 = 5.88

def f(x, t):
    #if t>10 and t < 10.2:
     #   return(r/K**2)*x*(K-x)*(x-S)-(b+0.1*t+5)*x
    #if t>20 and t < 20.2:
     #   return(r/K**2)*x*(K-x)*(x-S)-(b+0.1*t+6)*x
    #if t>20 and t < 20.2:
      #  return(r/K**2)*x*(K-x)*(x-S)-(b+0.1*t+5)*x
    #if t>60 and t < 60.2:
     #   return(r/K**2)*x*(K-x)*(x-S)-(b+0.1*t+5)*x
    #if t>70 and t < 70.2:
     #   return(r/K**2)*x*(K-x)*(x-S)-(b+0.1*t+5)*x
    return (r/K**2)*x*(K-x)*(x-S)-(b)*x

def g(x, t):
    return -.1*x


#u1 =  sdeint.itoint(f,g,x0,tspan)
#print('mean', np.average(u1))

def get_graphs():
    graphs = []
    for j in range(100):
        graphs.append(sdeint.itoint(f, g, x0, tspan))
    return graphs
def to_zero(result):
    
    if result[3499] < 0.1:
        return True
    else:
        return False

def get_var(results):
    S = 0
    T = len(results)
    for i in results:
        if not to_zero(i):
            v = i[50:]
            
            S = S + np.var(v)
        else:
            T = T -1
    return S/T


#b =3.5
#b1 = b
#result1 = get_graphs()
#var1 = get_var(result1)
#
#
#
#b = 3.75
#b2 = b
#result2 = get_graphs()
#var2 = get_var(result2)
#
#
#b = 4.
#b3 = b
#result3 = get_graphs()
#var3 = get_var(result3)
#
#b = 4.2
#b4 = b
#result4 = get_graphs()
#var4 = get_var(result4)
#
#b = 4.4
#b5 = b
#result5 = get_graphs()
#var5 = get_var(result5)
#
#b = 4.6
#b6 = b
#result6 = get_graphs()
#var6 = get_var(result6)
#
#b = 4.8
#b7 = b
#result7 = get_graphs()
#var7 = get_var(result7)
#
#b = 4.85
#b8 = b
#result8 = get_graphs()
#var8 = get_var(result8)
#
##b = 4.9
##b9 = b
##result9 = get_graphs()
##var9 = get_var(result9)
#
#
#b = 4.82
#b10 = b
#result10 = get_graphs()
#var10 = get_var(result10)
#
#b = 4.83
#b11 = b
#result11 = get_graphs()
#var11 = get_var(result11)
#
#b = 4.85
#b12 = b
#result11 = get_graphs()
#var12 = get_var(result11)
#    
#b = 4
#b2 = b
#result2 = get_graphs()
#var2 = get_var(result2)
#
#
#b = 4.75
#b3 = b
#result3 = get_graphs()
#var3 = get_var(result3)



#b =7.3
#b1 = b
#result1 = get_graphs()
#var1 = get_var(result1)
#
#
#
#b = 7.8
#b2 = b
#result2 = get_graphs()
#var2 = get_var(result2)
#
#
#b = 8.1
#b3 = b
#result3 = get_graphs()
#var3 = get_var(result3)
#
#
#b = 8.4
#b4 = b
#result4 = get_graphs()
#var4 = get_var(result4)
#
#b = 8.6
#b5 = b
#result5 = get_graphs()
#var5 = get_var(result5)
#
#b = 8.8
#b6 = b
#result6 = get_graphs()
#var6 = get_var(result6)
#
#b = 9.
#b7 = b
#result7 = get_graphs()
#var7 = get_var(result7)
#
#b = 9.2
#b8 = b
#result8 = get_graphs()
#var8 = get_var(result8)
#
#b = 9.3
#b9 = b
#result9 = get_graphs()
#var9 = get_var(result9)
#
#
#b = 9.4
#b10 = b
#result10 = get_graphs()
#var10 = get_var(result10)
#
#b = 9.5
#b11 = b
#result11 = get_graphs()
#var11 = get_var(result11)
#
#b = 9.6
#b12 = b
#result11 = get_graphs()
#var12 = get_var(result11)
    

#####################################################################
 
r = 80    

b =14.
b1 = b
result1 = get_graphs()
var1 = get_var(result1)



b = 15.
b2 = b
result2 = get_graphs()
var2 = get_var(result2)


b = 16.
b3 = b
result3 = get_graphs()
var3 = get_var(result3)


b = 17.
b4 = b
result4 = get_graphs()
var4 = get_var(result4)

b = 18.
b5 = b
result5 = get_graphs()
var5 = get_var(result5)

b = 19.
b6 = b
result6 = get_graphs()
var6 = get_var(result6)

b = 19.1
b7 = b
result7 = get_graphs()
var7 = get_var(result7)

b = 19.2
b8 = b
result8 = get_graphs()
var8 = get_var(result8)

b = 19.3
b9 = b
result9 = get_graphs()
var9 = get_var(result9)


b = 19.4
b10 = b
result10 = get_graphs()
var10 = get_var(result10)

b = 19.5
b11 = b
result11 = get_graphs()
var11 = get_var(result11)

#b = 9.6
#b12 = b
#result11 = get_graphs()
#var12 = get_var(result11)

########################################



print(b1, var1)
print(b2, var2)
print(b3, var3)
print(b4, var4)
print(b5, var5)
print(b6, var6)
print(b7, var7)
print(b8, var8)
print(b9, var9)
print(b10, var10)
print(b11, var11)
#print(b12, var12)

def get_graphs():
    graphs = []
    for j in range(100):
        graphs.append(sdeint.itoint(f, g, x0, tspan))
    return graphs


