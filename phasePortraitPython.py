# -*- coding: utf-8 -*-
"""
Tutorial on how to generate phase portraits of dynamical systems 
or state-space models in Python 

The tutorial webpage explaining the developed code is given here 

https://aleksandarhaber.com/phase-portraits-of-state-space-models-and-differential-equations-in-python/


@author: Aleksandar Haber 
June 2023

"""

import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

# first create create a function that evaluates the right-hand-side of the
# state-space equations for a given state vector

# x is the current state vector 
# t is current simulation time

def dynamicsStateSpace(x,t):
    dxdt=[-x[0]-3*x[1],3*x[0]-x[1]]
    return dxdt
    
# next, define a grid of points at which we will show arrows
x0=np.linspace(-2,2,20)
x1=np.linspace(-2,3,20)

# create a grid
X0,X1=np.meshgrid(x0,x1)
# projections of the trajectory tangent vector 
dX0=np.zeros(X0.shape)
dX1=np.zeros(X1.shape)

shape1,shape2=X1.shape

for indexShape1 in range(shape1):
    for indexShape2 in range(shape2):
        dxdtAtX=dynamicsStateSpace([X0[indexShape1,indexShape2],X1[indexShape1,indexShape2]],0)
        dX0[indexShape1,indexShape2]=dxdtAtX[0]
        dX1[indexShape1,indexShape2]=dxdtAtX[1]
      
        
#adjust the figure size
plt.figure(figsize=(8, 8))
# plot the phase portrait
plt.quiver(X0,X1,dX0,dX1,color='b')
# adjust the axis limits
plt.xlim(-2,2)
plt.ylim(-2,2)
# insert the title
plt.title('Phase Portrait', fontsize=14)
# set the axis labels
plt.xlabel('$x_{1}$',fontsize=14)
plt.ylabel('$x_{2}$',fontsize=14)
# adjust the font size of x and y axes
plt.tick_params(axis='both', which='major', labelsize=14)
# insert legend
# plt.legend(fontsize=14)
# save figure
plt.savefig('phasePortrait.png',dpi=600)
plt.show()

# now simulate the dynamics for a certain starting trajectory and 
# plot the dynamics on the same graph
initialState=np.array([-1,-1])
simulationTime=np.linspace(0,2,200)
# generate the state-space trajectory
solutionState=odeint(dynamicsStateSpace,initialState,simulationTime)


#adjust the figure size
plt.figure(figsize=(8, 8))
# plot the phase portrait
plt.quiver(X0,X1,dX0,dX1,color='b')
# adjust the axis limits
plt.xlim(-2,2)
plt.ylim(-2,2)
# add the state trajectory plot
plt.plot(solutionState[:,0], solutionState[:,1], color='r',linewidth=3)
# insert the title
plt.title('Phase Portrait', fontsize=14)
# set the axis labels
plt.xlabel('$x_{1}$',fontsize=14)
plt.ylabel('$x_{2}$',fontsize=14)
# adjust the font size of x and y axes
plt.tick_params(axis='both', which='major', labelsize=14)
# insert legend
# plt.legend(fontsize=14)
# save figure
plt.savefig('phasePortraitStateTrajectory.png',dpi=600)
plt.show() 
 
