# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:05:00 2020

@author: Jaesub Sim
"""
##### Enter failed cable
Fail = 'U2'
########################

##### Enter Flow direction
Deg = '20'
########################
Failure_mode = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'FCU1', 'FCU2',
                'FCU3', 'FCU4', 'FCU5', 'FCU6', 'FCU7', 'FCU8', 'FCV1', 'FCV2', 'FCV3', 'FCV4', 'FCV5']

import pickle

# initial condition (no-loading)
# with open('..\\1x4_cages\\processed_resu1x4_noloading.csv', 'rb') as handle:
#     resu_nl = pickle.load(handle)
######## intact model ########################
with open('..\\..\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree' + str(Deg) + '.csv', 'rb') as handle:
    resu_nl = pickle.load(handle)
######## failed model ########################
with open('..\\..\\Results_1x4cages_failure\\' + str(Fail) + '\\cprocessed_Mul1x4Vel0.5Degree' + str(Deg) + '.csv',
          'rb') as handle:
    resu = pickle.load(handle)

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (6.5, 3.5)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = '10'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"

## Center point of cages - initial pos before loading ##
center = []
for i in range(0, 4):
    center.append(resu_nl['collar' + str(i)]['FloaterCenterPos'][1000, 0:2])

## Center point of cages - pos after loading ##
center2 = []
### Intact model - 250, Failure mode - 1000 ###
for i in range(0, 4):
    center2.append(resu['collar' + str(i)]['FloaterCenterPos'][250, 0:2])
## Buoy positions
buoy = []
for i in range(0, 5):
    for j in range(0, 2):
        buoy.append(resu_nl['mooring3']['platePosition' + str(i) + '_' + str(j)][1000, 0:2])

anchor_pos = [[-300, -50],
              [-300, 50],
              [300, -50],
              [300, 50],
              [-200, -150],
              [-100, -150],
              [-0, -150],
              [100, -150],
              [200, -150],
              [-200, 150],
              [-100, 150],
              [-0, 150],
              [100, 150],
              [200, 150]
              ]
## Initial state
plt.figure()
plt.gca().invert_yaxis()
##################### mooring lines ##################################

moor_Ux = []
moor_Uy = []
moor_Vx = []
moor_Vy = []
adjust = [0, 1, 4, 3]
for i in range(0, 4):
    moor_Ux.append([anchor_pos[i][0], buoy[adjust[i] * i][0]])
for i in range(0, 4):
    moor_Uy.append([anchor_pos[i][1], buoy[adjust[i] * i][1]])

for i in range(0, 5):
    moor_Vx.append([anchor_pos[i + 4][0], buoy[i * 2][0]])
    moor_Vy.append([anchor_pos[i + 4][1], buoy[i * 2][1]])

adjust2 = [1 / 5, 1 / 2, 5 / 7, 7 / 8, 1]
for i in range(5, 10):
    moor_Vx.append([anchor_pos[i + 4][0], buoy[int(adjust2[i - 5] * i)][0]])
    moor_Vy.append([anchor_pos[i + 4][1], buoy[int(adjust2[i - 5] * i)][1]])

for i in range(0, 4):
    plt.plot(moor_Ux[i], moor_Uy[i], 'k')
for i in range(0, 10):
    plt.plot(moor_Vx[i], moor_Vy[i], 'k')

################# Frame cables ######################################
FCUx = []
FCUy = []
upper = np.arange(0, 8, 2)
lower = np.arange(1, 9, 2)
for i in upper:
    FCUx.append([buoy[i][0], buoy[i + 2][0]])
for i in upper:
    FCUy.append([buoy[i][1], buoy[i + 2][1]])
for i in lower:
    FCUx.append([buoy[i][0], buoy[i + 2][0]])
for i in lower:
    FCUy.append([buoy[i][1], buoy[i + 2][1]])

FCVx = []
FCVy = []
for i in range(0, 10, 2):
    FCVx.append([buoy[i][0], buoy[i + 1][0]])
for i in range(0, 10, 2):
    FCVy.append([buoy[i][1], buoy[i + 1][1]])
for i in range(0, 8):
    plt.plot(FCUx[i], FCUy[i], 'k')
for i in range(0, 5):
    plt.plot(FCVx[i], FCVy[i], 'k')

conP1 = [4.97419, 5.49779, 6.02139]
conP2 = [3.40339, 3.92699, 4.45059]
conP3 = [1.8326, 2.35619, 2.87979]
conP4 = [0.261799, 0.785398, 1.309]
r = 25
ang = np.linspace(0, 2 * np.pi, 50)

for cage in range(0, 4):
    xc = center[cage][0] + r * np.cos(ang)
    yc = center[cage][1] + r * np.sin(ang)

    ############# Bridles #############################################

    ############ Bridle 1 to 3 #######################

    for i in range(len(conP1)):
        bx = [buoy[3 + 2 * cage][0], center[cage][0] + r * np.cos(conP1[i])]
        by = [buoy[3 + 2 * cage][1], center[cage][1] - r * np.sin(conP1[i])]
        plt.plot(bx, by, '-k')
        ############ Bridle 4 to 6 #######################
    for i in range(len(conP2)):
        bx = [buoy[1 + 2 * cage][0], center[cage][0] + r * np.cos(conP2[i])]
        by = [buoy[1 + 2 * cage][1], center[cage][1] - r * np.sin(conP2[i])]
        plt.plot(bx, by, '-k')
        ############ Bridle 7 to 9 #######################
    for i in range(len(conP3)):
        bx = [buoy[0 + 2 * cage][0], center[cage][0] + r * np.cos(conP3[i])]
        by = [buoy[0 + 2 * cage][1], center[cage][1] - r * np.sin(conP3[i])]
        plt.plot(bx, by, '-k')
        ############ Bridle 10 to 12 #####################
    for i in range(len(conP1)):
        bx = [buoy[2 + 2 * cage][0], center[cage][0] + r * np.cos(conP4[i])]
        by = [buoy[2 + 2 * cage][1], center[cage][1] - r * np.sin(conP4[i])]
        plt.plot(bx, by, '-k')
    ##########  Floating collar ###########
    plt.plot(xc, yc, linewidth=2, color='k', zorder=1)

    ########### net ###############
    for i in range(-25, 25, 4):
        y = i + center[cage][1]
        plt.hlines(y, center[cage][0] - np.sqrt(r ** 2 - (i) ** 2),
                   center[cage][0] + np.sqrt(r ** 2 - (i) ** 2), colors='k', linestyle='solid')
    for i in range(-25, 25, 4):
        x = i + center[cage][0]
        plt.vlines(x, center[cage][1] - np.sqrt(r ** 2 - (i) ** 2),
                   center[cage][1] + np.sqrt(r ** 2 - (i) ** 2), colors='k', linestyle='solid')
#####################################################################################################################
############################################ shifted cage ############################################################
#####################################################################################################################

## Buoy positions
buoy_s = []
for i in range(0, 5):
    for j in range(0, 2):
        buoy_s.append(resu['mooring3']['platePosition' + str(i) + '_' + str(j)][250, 0:2])

##################### mooring lines ##################################

moor_Ux_s = []
moor_Uy_s = []
moor_Vx_s = []
moor_Vy_s = []
adjust = [0, 1, 4, 3]
for i in range(0, 4):
    moor_Ux_s.append([anchor_pos[i][0], buoy_s[adjust[i] * i][0]])
for i in range(0, 4):
    moor_Uy_s.append([anchor_pos[i][1], buoy_s[adjust[i] * i][1]])

for i in range(0, 5):
    moor_Vx_s.append([anchor_pos[i + 4][0], buoy_s[i * 2][0]])
    moor_Vy_s.append([anchor_pos[i + 4][1], buoy_s[i * 2][1]])

adjust2 = [1 / 5, 1 / 2, 5 / 7, 7 / 8, 1]
for i in range(5, 10):
    moor_Vx_s.append([anchor_pos[i + 4][0], buoy_s[int(adjust2[i - 5] * i)][0]])
    moor_Vy_s.append([anchor_pos[i + 4][1], buoy_s[int(adjust2[i - 5] * i)][1]])

for i in range(0, 4):
    if i == Failure_mode.index(Fail):
        plt.plot(moor_Ux_s[i], moor_Uy_s[i], color='firebrick', alpha=0.0)
    else:
        plt.plot(moor_Ux_s[i], moor_Uy_s[i], color='firebrick', alpha=0.5)
for i in range(0, 10):
    if i + 4 == Failure_mode.index(Fail):
        plt.plot(moor_Vx_s[i], moor_Vy_s[i], color='firebrick', alpha=0.0)
    else:
        plt.plot(moor_Vx_s[i], moor_Vy_s[i], color='firebrick', alpha=0.5)

################# Frame cables ######################################
FCUx_s = []
FCUy_s = []
upper = np.arange(0, 8, 2)
lower = np.arange(1, 9, 2)
for i in upper:
    FCUx_s.append([buoy_s[i][0], buoy_s[i + 2][0]])
for i in upper:
    FCUy_s.append([buoy_s[i][1], buoy_s[i + 2][1]])
for i in lower:
    FCUx_s.append([buoy_s[i][0], buoy_s[i + 2][0]])
for i in lower:
    FCUy_s.append([buoy_s[i][1], buoy_s[i + 2][1]])

FCVx_s = []
FCVy_s = []
for i in range(0, 10, 2):
    FCVx_s.append([buoy_s[i][0], buoy_s[i + 1][0]])
for i in range(0, 10, 2):
    FCVy_s.append([buoy_s[i][1], buoy_s[i + 1][1]])
for i in range(0, 8):
    if i + 14 == Failure_mode.index(Fail):
        plt.plot(FCUx_s[i], FCUy_s[i], color='firebrick', alpha=0.0)
    else:
        plt.plot(FCUx_s[i], FCUy_s[i], color='firebrick', alpha=0.5)
for i in range(0, 5):
    if i + 22 == Failure_mode.index(Fail):
        plt.plot(FCVx_s[i], FCVy_s[i], color='firebrick', alpha=0.0)
    else:
        plt.plot(FCVx_s[i], FCVy_s[i], color='firebrick', alpha=0.5)

############# Bridles #############################################
conP1 = [4.97419, 5.49779, 6.02139]
conP2 = [3.40339, 3.92699, 4.45059]
conP3 = [1.8326, 2.35619, 2.87979]
conP4 = [0.261799, 0.785398, 1.309]
r = 25
ang = np.linspace(0, 2 * np.pi, 50)

for cage in range(0, 4):
    xc = center2[cage][0] + r * np.cos(ang)
    yc = center2[cage][1] + r * np.sin(ang)

    ############ Bridle 1 to 3 #######################

    for i in range(len(conP1)):
        bx = [buoy_s[3 + 2 * cage][0], center2[cage][0] + r * np.cos(conP1[i])]
        by = [buoy_s[3 + 2 * cage][1], center2[cage][1] - r * np.sin(conP1[i])]
        plt.plot(bx, by, color='firebrick', alpha=0.5)
        ############ Bridle 4 to 6 #######################
    for i in range(len(conP2)):
        bx = [buoy_s[1 + 2 * cage][0], center2[cage][0] + r * np.cos(conP2[i])]
        by = [buoy_s[1 + 2 * cage][1], center2[cage][1] - r * np.sin(conP2[i])]
        plt.plot(bx, by, color='firebrick', alpha=0.5)
        ############ Bridle 7 to 9 #######################
    for i in range(len(conP3)):
        bx = [buoy_s[0 + 2 * cage][0], center2[cage][0] + r * np.cos(conP3[i])]
        by = [buoy_s[0 + 2 * cage][1], center2[cage][1] - r * np.sin(conP3[i])]
        plt.plot(bx, by, color='firebrick', alpha=0.5)
        ############ Bridle 10 to 12 #####################
    for i in range(len(conP1)):
        bx = [buoy_s[2 + 2 * cage][0], center2[cage][0] + r * np.cos(conP4[i])]
        by = [buoy_s[2 + 2 * cage][1], center2[cage][1] - r * np.sin(conP4[i])]
        plt.plot(bx, by, color='firebrick', alpha=0.5)
    ##########  Floating collar ###########
    plt.plot(xc, yc, linewidth=2, color='firebrick', alpha=0.5)

    ########### net ###############
    for i in range(-25, 25, 4):
        y = i + center2[cage][1]
        plt.hlines(y, center2[cage][0] - np.sqrt(r ** 2 - (i) ** 2),
                   center2[cage][0] + np.sqrt(r ** 2 - (i) ** 2), color='firebrick', alpha=0.5, linestyle='solid')
    for i in range(-25, 25, 4):
        x = i + center2[cage][0]
        plt.vlines(x, center2[cage][1] - np.sqrt(r ** 2 - (i) ** 2),
                   center2[cage][1] + np.sqrt(r ** 2 - (i) ** 2), color='firebrick', alpha=0.5, linestyle='solid')

plt.axis('off')
plt.axis('equal')
plt.tight_layout(pad=0)
plt.savefig('1x4_shifted_state_failure(' + str(Deg) + 'deg_' + str(Fail) + '_Fail).png', dpi=600)
