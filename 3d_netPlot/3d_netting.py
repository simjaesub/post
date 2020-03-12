# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 11:44:12 2020

@author: shuer
"""

import numpy as np
import magicFun as mf
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (6.3, 3.5)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = '8'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"
from mpl_toolkits.mplot3d import Axes3D as Ax
import pickle

# initial condition (no-loading)
with open('dprocessed_Mul1x1Vel0.5Degree30.csv', 'rb') as handle:
    resu_nl = pickle.load(handle)
######## intact model ########################
with open('dprocessed_Mul1x1Vel0.5Degree30.csv', 'rb') as handle:
    resu = pickle.load(handle)
######## failed model ########################
with open('dprocessed_Mul1x1Vel0.5Degree30.csv', 'rb') as handle:
    resu_f = pickle.load(handle)

pos = np.zeros((321, 3))
for i in range(1, 322):
    pos[i - 1][0] = resu['NetStructure0']['Pos_' + str(i)][20, 0]
    pos[i - 1][1] = resu['NetStructure0']['Pos_' + str(i)][20, 1]
    pos[i - 1][2] = resu['NetStructure0']['Pos_' + str(i)][20, 2]


fig = plt.figure()
ax = plt.gca(projection='3d')
plt.gca().invert_zaxis()

mf.drawCageV(pos,ax)
mf.drawCageH(pos,ax)