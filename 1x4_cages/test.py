import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax
import pickle

# initial condition (no-loading)
with open('processed_resu1x4_noloading.csv', 'rb') as handle:
    resu_nl = pickle.load(handle)
######## intact model ########################
with open('..\\..\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree20.csv', 'rb') as handle:
    resui = pickle.load(handle)
######## failed model ########################
with open('..\\..\\Results_1x4cages_failure\\U2\\cprocessed_Mul1x4Vel0.5Degree20.csv', 'rb') as handle:
    resu = pickle.load(handle)
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
    plt.plot(moor_Ux_s[i], moor_Uy_s[i], moor_Uz_s[i], color='firebrick', alpha=0.6)
for i in range(0, 10):
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
    plt.plot(FCUx_s[i], FCUy_s[i], FCUz_s[i], color='firebrick', alpha=0.6)
for i in range(0, 5):
    plt.plot(FCVx_s[i], FCVy_s[i], FCVz_s[i], color='firebrick', alpha=0.6)
