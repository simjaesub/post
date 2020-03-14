# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 11:44:12 2020

@author: shuer
"""

import numpy as np
import matplotlib.pyplot as plt
import magicFun as mf

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (16.3, 15)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = '8'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"
from mpl_toolkits.mplot3d import Axes3D as Ax
import pickle

# initial condition (no-loading)
with open('processed_resu1x4_noloading.csv', 'rb') as handle:
    resu_nl = pickle.load(handle)
######## intact model ########################
with open('..\\..\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree20.csv', 'rb') as handle:
    resu = pickle.load(handle)
######## failed model ########################
with open('..\\..\\Results_1x4cages_failure\\U2\\cprocessed_Mul1x4Vel0.5Degree20.csv', 'rb') as handle:
    resu_f = pickle.load(handle)

pos0 = np.zeros((321, 3))
for i in range(1, 322):
    pos0[i - 1][0] = resu['NetStructure0']['Pos_' + str(i)][20, 0]
    pos0[i - 1][1] = resu['NetStructure0']['Pos_' + str(i)][20, 1]
    pos0[i - 1][2] = resu['NetStructure0']['Pos_' + str(i)][20, 2]
pos1 = np.zeros((321, 3))
for i in range(1, 322):
    pos1[i - 1][0] = resu['NetStructure1']['Pos_' + str(i)][20, 0]
    pos1[i - 1][1] = resu['NetStructure1']['Pos_' + str(i)][20, 1]
    pos1[i - 1][2] = resu['NetStructure1']['Pos_' + str(i)][20, 2]
pos2 = np.zeros((321, 3))
for i in range(1, 322):
    pos2[i - 1][0] = resu['NetStructure2']['Pos_' + str(i)][20, 0]
    pos2[i - 1][1] = resu['NetStructure2']['Pos_' + str(i)][20, 1]
    pos2[i - 1][2] = resu['NetStructure2']['Pos_' + str(i)][20, 2]
pos3 = np.zeros((321, 3))
for i in range(1, 322):
    pos3[i - 1][0] = resu['NetStructure3']['Pos_' + str(i)][20, 0]
    pos3[i - 1][1] = resu['NetStructure3']['Pos_' + str(i)][20, 1]
    pos3[i - 1][2] = resu['NetStructure3']['Pos_' + str(i)][20, 2]

fig = plt.figure()
ax = plt.gca(projection='3d')
plt.gca().invert_zaxis()

mf.drawCageV(pos0, ax)
mf.drawCageH(pos0, ax)

mf.drawCageV(pos1, ax)
mf.drawCageH(pos1, ax)

mf.drawCageV(pos2, ax)
mf.drawCageH(pos2, ax)

mf.drawCageV(pos3, ax)
mf.drawCageH(pos3, ax)

# zpos = np.array([0, 28, 3, 6, 9, 12, 15, 17.6, 20.2, 22.8, 25.4])

# zorder = np.sort(zpos)

# pos = np.zeros((321, 3))
# zorder = list(zorder)

# for i in range(1, 322):
#     pos[i - 1][0] = resu['NetStructure0']['Pos_' + str(i)][0, 0]
#     pos[i - 1][1] = resu['NetStructure0']['Pos_' + str(i)][0, 1]
#     pos[i - 1][2] = resu['NetStructure0']['Pos_' + str(i)][0, 2]
# # X = np.zeros((321,1))
# # Y = np.zeros((321,1))
# # Z = np.zeros((321,1))
# # for i in range(1,322):
# #     X[i-1][0] = resu['NetStructure0']['Pos_'+str(i)][0,0]
# #     Y[i-1][0] = resu['NetStructure0']['Pos_'+str(i)][0,1]
# #     Z[i-1][0] = resu['NetStructure0']['Pos_'+str(i)][0,2]


# posxz = np.delete(pos, 1, 1)
# posyz = np.delete(pos, 0, 1)

# import operator

# repos = sorted(pos, key=operator.itemgetter(2))

# re_pos = sorted(posxz, key=operator.itemgetter(1))
# re_pos2 = sorted(posyz, key=operator.itemgetter(1))

# X = np.delete(re_pos, 1, 1)
# X1 = np.sort(X)
# Y = np.delete(re_pos2, 1, 1)
# Y1 = np.sort(Y)
# Z = np.delete(re_pos, 0, 1)
# Z1 = np.sort(Z)

# ####################### coordinate of each layer #################################
# nolayer = np.arange(32, 321, 32)
# WholeLayers = []

# ########## layer 1 ###################
# layer1 = np.zeros((32, 3))
# for i in range(0, nolayer[0]):
#     layer1[i][0] = X[i]
#     layer1[i][1] = Y[i]
#     layer1[i][2] = Z[i]
# a = np.array([layer1[0][0], layer1[0][1], layer1[0][2]])
# layer1 = np.vstack((layer1, a))
# WholeLayers.append(layer1)
# ########## layer 2 ###################
# layer2 = np.zeros((32, 3))
# for i in range(nolayer[0], nolayer[1]):
#     layer2[i - nolayer[0]][0] = X[i]
#     layer2[i - nolayer[0]][1] = Y[i]
#     layer2[i - nolayer[0]][2] = Z[i]
# a = np.array([layer2[0][0], layer2[0][1], layer2[0][2]])
# layer2 = np.vstack((layer2, a))
# WholeLayers.append(layer2)
# ########## layer 3 ###################
# layer3 = np.zeros((32, 3))
# for i in range(nolayer[1], nolayer[2]):
#     layer3[i - nolayer[1]][0] = X[i]
#     layer3[i - nolayer[1]][1] = Y[i]
#     layer3[i - nolayer[1]][2] = Z[i]
# a = np.array([layer3[0][0], layer3[0][1], layer3[0][2]])
# layer3 = np.vstack((layer3, a))
# WholeLayers.append(layer3)
# ########## layer 4 ###################
# layer4 = np.zeros((32, 3))
# for i in range(nolayer[2], nolayer[3]):
#     layer4[i - nolayer[2]][0] = X[i]
#     layer4[i - nolayer[2]][1] = Y[i]
#     layer4[i - nolayer[2]][2] = Z[i]
# a = np.array([layer4[0][0], layer4[0][1], layer4[0][2]])
# layer4 = np.vstack((layer4, a))
# WholeLayers.append(layer4)
# ########## layer 5 ###################
# layer5 = np.zeros((32, 3))
# for i in range(nolayer[3], nolayer[4]):
#     layer5[i - nolayer[3]][0] = X[i]
#     layer5[i - nolayer[3]][1] = Y[i]
#     layer5[i - nolayer[3]][2] = Z[i]
# a = np.array([layer5[0][0], layer5[0][1], layer5[0][2]])
# layer5 = np.vstack((layer5, a))
# WholeLayers.append(layer5)
# ########## layer 6 ###################
# layer6 = np.zeros((32, 3))
# for i in range(nolayer[4], nolayer[5]):
#     layer6[i - nolayer[4]][0] = X[i]
#     layer6[i - nolayer[4]][1] = Y[i]
#     layer6[i - nolayer[4]][2] = Z[i]
# a = np.array([layer6[0][0], layer6[0][1], layer6[0][2]])
# layer6 = np.vstack((layer6, a))
# WholeLayers.append(layer6)
# ########## layer 7 ###################
# layer7 = np.zeros((32, 3))
# for i in range(nolayer[5], nolayer[6]):
#     layer7[i - nolayer[5]][0] = X[i]
#     layer7[i - nolayer[5]][1] = Y[i]
#     layer7[i - nolayer[5]][2] = Z[i]
# a = np.array([layer7[0][0], layer7[0][1], layer7[0][2]])
# layer7 = np.vstack((layer7, a))
# WholeLayers.append(layer7)
# ########## layer 8 ###################
# layer8 = np.zeros((32, 3))
# for i in range(nolayer[6], nolayer[7]):
#     layer8[i - nolayer[6]][0] = X[i]
#     layer8[i - nolayer[6]][1] = Y[i]
#     layer8[i - nolayer[6]][2] = Z[i]
# a = np.array([layer8[0][0], layer8[0][1], layer8[0][2]])
# layer8 = np.vstack((layer8, a))
# WholeLayers.append(layer8)
# ########## layer 9 ###################
# layer9 = np.zeros((32, 3))
# for i in range(nolayer[7], nolayer[8]):
#     layer9[i - nolayer[7]][0] = X[i]
#     layer9[i - nolayer[7]][1] = Y[i]
#     layer9[i - nolayer[7]][2] = Z[i]
# a = np.array([layer9[0][0], layer9[0][1], layer9[0][2]])
# layer9 = np.vstack((layer9, a))
# WholeLayers.append(layer9)
# ########## layer 10 ###################
# layer10 = np.zeros((32, 3))
# for i in range(nolayer[8], nolayer[9]):
#     layer10[i - nolayer[8]][0] = X[i]
#     layer10[i - nolayer[8]][1] = Y[i]
#     layer10[i - nolayer[8]][2] = Z[i]
# a = np.array([layer10[0][0], layer10[0][1], layer10[0][2]])
# layer10 = np.vstack((layer10, a))
# WholeLayers.append(layer10)

# #######

# X_layer3 = []
# Y_layer3 = []
# Z_layer3 = []
# for i in range(0, 33):
#     X_layer3.append(layer3[i][0])

# for i in range(0, 33):
#     Y_layer3.append(layer3[i][1])

# for i in range(0, 33):
#     Z_layer3.append(layer3[i][2])

# fig = plt.figure()
# ax = plt.gca(projection='3d')
# plt.gca().invert_zaxis()
# # ax.scatter(X,Y,Z)
# # ax.plot(pos[:,0],pos[:,1], pos[:,2])

# for i in range(0, 10):
#     ax.plot(WholeLayers[i][:, 0], WholeLayers[i][:, 1], WholeLayers[i][:, 2])

# # plt.figure()
# # for i in range(0,33):
# #     plt.scatter(WholeLayers[3][i,0], WholeLayers[3][i,1])
# #     plt.text(WholeLayers[3][i,0], WholeLayers[3][i,1], 'node'+str(i+1))

# # plt.plot(WholeLayers[3][:,0], WholeLayers[3][:,1])
