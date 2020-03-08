##### Enter failed cable
Fail = 'U2'
########################

##### Enter Flow direction
Deg = '20'
########################

Failure_mode = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'FCU1', 'FCU2',
                'FCU3', 'FCU4', 'FCU5', 'FCU6', 'FCU7', 'FCU8', 'FCV1', 'FCV2', 'FCV3', 'FCV4', 'FCV5']

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (6.3, 3.5)
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"
from mpl_toolkits.mplot3d import Axes3D as Ax
import pickle

# initial condition (no-loading)
with open('..\\1x4_cages\\processed_resu1x4_noloading.csv', 'rb') as handle:
    resu_nl = pickle.load(handle)
######## intact model ########################
# with open('..\\..\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree20.csv', 'rb') as handle:
#     resu = pickle.load(handle)
######## failed model ########################
with open('..\\..\\Results_1x4cages_failure\\' + str(Fail) + '\\cprocessed_Mul1x4Vel0.5Degree' + str(Deg) + '.csv',
          'rb') as handle:
    resui = pickle.load(handle)

## Center point of cages - initial pos before loading ##
center = []
for i in range(0, 4):
    center.append(resu_nl['collar' + str(i)]['FloaterCenterPos'][1000, 0:3])

## Center point of cages - pos after loading ##
center2 = []
### Intact model - 250, Failure mode - 1000 ###
for i in range(0, 4):
    center2.append(resui['collar' + str(i)]['FloaterCenterPos'][250, 0:3])
## Buoy positions
buoy = []
for i in range(0, 5):
    for j in range(0, 2):
        buoy.append(resu_nl['mooring3']['platePosition' + str(i) + '_' + str(j)][1000, 0:3])

anchor_pos = [[-300, -50, 80],
              [-300, 50, 80],
              [300, -50, 80],
              [300, 50, 80],
              [-200, -150, 80],
              [-100, -150, 80],
              [-0, -150, 80],
              [100, -150, 80],
              [200, -150, 80],
              [-200, 150, 80],
              [-100, 150, 80],
              [-0, 150, 80],
              [100, 150, 80],
              [200, 150, 80]
              ]
## Initial state
fig = plt.figure()
ax1 = fig.gca(projection='3d')
plt.gca().invert_yaxis()
ax1.invert_zaxis()
##################### mooring lines ##################################
moor_Ux = []
moor_Uy = []
moor_Uz = []
moor_Vx = []
moor_Vy = []
moor_Vz = []

adjust = [0, 1, 4, 3]
for i in range(0, 4):
    moor_Ux.append([anchor_pos[i][0], buoy[adjust[i] * i][0]])
    moor_Uy.append([anchor_pos[i][1], buoy[adjust[i] * i][1]])
    moor_Uz.append([anchor_pos[i][2], buoy[adjust[i] * i][2]])

for i in range(0, 5):
    moor_Vx.append([anchor_pos[i + 4][0], buoy[i * 2][0]])
    moor_Vy.append([anchor_pos[i + 4][1], buoy[i * 2][1]])
    moor_Vz.append([anchor_pos[i + 4][2], buoy[i * 2][2]])

adjust2 = [1 / 5, 1 / 2, 5 / 7, 7 / 8, 1]
for i in range(5, 10):
    moor_Vx.append([anchor_pos[i + 4][0], buoy[int(adjust2[i - 5] * i)][0]])
    moor_Vy.append([anchor_pos[i + 4][1], buoy[int(adjust2[i - 5] * i)][1]])
    moor_Vz.append([anchor_pos[i + 4][2], buoy[int(adjust2[i - 5] * i)][2]])

for i in range(0, 4):
    plt.plot(moor_Ux[i], moor_Uy[i], moor_Uz[i], 'k')
for i in range(0, 10):
    plt.plot(moor_Vx[i], moor_Vy[i], moor_Vz[i], 'k')

################# Frame cables ######################################
FCUx = []
FCUy = []
FCUz = []
upper = np.arange(0, 8, 2)
lower = np.arange(1, 9, 2)
for i in upper:
    FCUx.append([buoy[i][0], buoy[i + 2][0]])
    FCUy.append([buoy[i][1], buoy[i + 2][1]])
    FCUz.append([buoy[i][2], buoy[i + 2][2]])
for i in lower:
    FCUx.append([buoy[i][0], buoy[i + 2][0]])
    FCUy.append([buoy[i][1], buoy[i + 2][1]])
    FCUz.append([buoy[i][2], buoy[i + 2][2]])

FCVx = []
FCVy = []
FCVz = []
for i in range(0, 10, 2):
    FCVx.append([buoy[i][0], buoy[i + 1][0]])
    FCVy.append([buoy[i][1], buoy[i + 1][1]])
    FCVz.append([buoy[i][2], buoy[i + 1][2]])
for i in range(0, 8):
    plt.plot(FCUx[i], FCUy[i], FCUz[i], 'k')
for i in range(0, 5):
    plt.plot(FCVx[i], FCVy[i], FCVz[i], 'k')

#### Shifted-cages

## Buoy positions
buoy_s = []
for i in range(0, 5):
    for j in range(0, 2):
        buoy_s.append(resui['mooring3']['platePosition' + str(i) + '_' + str(j)][250, 0:3])

#################### mooring lines ##################################
moor_Ux_s = []
moor_Uy_s = []
moor_Uz_s = []
moor_Vx_s = []
moor_Vy_s = []
moor_Vz_s = []

adjust = [0, 1, 4, 3]
for i in range(0, 4):
    moor_Ux_s.append([anchor_pos[i][0], buoy_s[adjust[i] * i][0]])
    moor_Uy_s.append([anchor_pos[i][1], buoy_s[adjust[i] * i][1]])
    moor_Uz_s.append([anchor_pos[i][2], buoy_s[adjust[i] * i][2]])

for i in range(0, 5):
    moor_Vx_s.append([anchor_pos[i + 4][0], buoy_s[i * 2][0]])
    moor_Vy_s.append([anchor_pos[i + 4][1], buoy_s[i * 2][1]])
    moor_Vz_s.append([anchor_pos[i + 4][2], buoy_s[i * 2][2]])

adjust2 = [1 / 5, 1 / 2, 5 / 7, 7 / 8, 1]
for i in range(5, 10):
    moor_Vx_s.append([anchor_pos[i + 4][0], buoy_s[int(adjust2[i - 5] * i)][0]])
    moor_Vy_s.append([anchor_pos[i + 4][1], buoy_s[int(adjust2[i - 5] * i)][1]])
    moor_Vz_s.append([anchor_pos[i + 4][2], buoy_s[int(adjust2[i - 5] * i)][2]])

for i in range(0, 4):
    if i == Failure_mode.index(Fail):
        plt.plot(moor_Ux_s[i], moor_Uy_s[i], moor_Uz_s[i], color='firebrick', alpha=0.0)
    else:
        plt.plot(moor_Ux_s[i], moor_Uy_s[i], moor_Uz_s[i], color='firebrick', alpha=0.6)
for i in range(0, 10):
    if i + 4 == Failure_mode.index(Fail):
        plt.plot(moor_Vx_s[i], moor_Vy_s[i], moor_Vz_s[i], color='firebrick', alpha=0.0)
    else:
        plt.plot(moor_Vx_s[i], moor_Vy_s[i], moor_Vz_s[i], color='firebrick', alpha=0.6)

################# Frame cables ######################################
FCUx_s = []
FCUy_s = []
FCUz_s = []
upper = np.arange(0, 8, 2)
lower = np.arange(1, 9, 2)
for i in upper:
    FCUx_s.append([buoy_s[i][0], buoy_s[i + 2][0]])
    FCUy_s.append([buoy_s[i][1], buoy_s[i + 2][1]])
    FCUz_s.append([buoy_s[i][2], buoy_s[i + 2][2]])
for i in lower:
    FCUx_s.append([buoy_s[i][0], buoy_s[i + 2][0]])
    FCUy_s.append([buoy_s[i][1], buoy_s[i + 2][1]])
    FCUz_s.append([buoy_s[i][2], buoy_s[i + 2][2]])

FCVx_s = []
FCVy_s = []
FCVz_s = []
for i in range(0, 10, 2):
    FCVx_s.append([buoy_s[i][0], buoy_s[i + 1][0]])
    FCVy_s.append([buoy_s[i][1], buoy_s[i + 1][1]])
    FCVz_s.append([buoy_s[i][2], buoy_s[i + 1][2]])
for i in range(0, 8):
    if i + 14 == Failure_mode.index(Fail):
        plt.plot(FCUx_s[i], FCUy_s[i], FCUz_s[i], color='firebrick', alpha=0.0)
    else:
        plt.plot(FCUx_s[i], FCUy_s[i], FCUz_s[i], color='firebrick', alpha=0.6)
for i in range(0, 5):
    if i + 22 == Failure_mode.index(Fail):
        plt.plot(FCVx_s[i], FCVy_s[i], FCVz_s[i], color='firebrick', alpha=0.0)
    else:
        plt.plot(FCVx_s[i], FCVy_s[i], FCVz_s[i], color='firebrick', alpha=0.6)

plt.axis('off')
# plt.axis('equal')
plt.tight_layout(pad=0.0)
ax1.view_init(elev=54, azim=80)
plt.savefig('3d_shifted_fishfarm(Fail_' + str(Fail) + '_Deg' + str(Deg) + ').png', dpi=600)
