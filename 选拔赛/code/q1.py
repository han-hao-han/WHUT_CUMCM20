# -*- coding: utf-8 -*-
"""q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oYCd94tF34ZvCbTrcYwOoeVidp_WppBw
"""

import numpy as np
from math import *
import random
from bayes_opt import BayesianOptimization

a = 30
b = 20
len = 606#6060
wi = 216#2160

def get_theta(theta,a=a,b=b,l=len,w=wi):
    theta = theta/360*pi
    x = sqrt(4*a*b/(b*sin(theta)*sin(theta)+a*cos(theta)*cos(theta)))
    i,j=0,0
    ww = w
    num=0
    detal = x-x*cos(theta)
    while j != int(ww / (2 * b)) + 1:
        for i in range(int(l/(2*x*cos(theta)))):
            num = num+1
        # print(j,int(ww / (2 * b)))
        j+=1
        ww=w+j*1
    return num
# get_theta(60)
#
rf_bo = BayesianOptimization(
    get_theta,
    {'theta': (30, 60),}
)

print(rf_bo.maximize())


import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import Ellipse
detal = a-sqrt(3)*a/2
ells = []
j=0
h = wi
while j != int(h/(2*b))+1:
  for i in range(int(len/(2*a))):
    if j%2==0:
      e = Ellipse(xy=[i*2*a+a,j*2*b+b-detal*j], width=a*2, height=b*2, angle=0)
    else:
      e = Ellipse(xy=[i*2*a+2*a,j*2*b+b-detal*j], width=a*2, height=b*2, angle=0)
    ells.append(e)
  print(j,int(h/(2*b)))
  j = j+1
  h = wi+detal*j

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, aspect='equal')
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    alf = rnd.rand()+0.1
    alf = 1 if alf>1 else alf
    e.set_alpha(alf)
    # e.set_facecolor(rnd.rand(3))

ax.set_xlim(0, len)
ax.set_ylim(0, wi)

plt.show()
# plt.savefig("demo.png")

