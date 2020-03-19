import numpy as np
import matplotlib.pyplot as plt
import magicFun_initial as mfi
import magicFun_failmode as mff
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (18.3, 9.5)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = '8'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"
import pickle

# initial condition (no-loading)
with open('processed_resu1x4_noloading.csv', 'rb') as handle:
    resui = pickle.load(handle)
######## intact model ########################
with open('..\\..\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree20.csv', 'rb') as handle:
    resu = pickle.load(handle)
######## failed model ########################
# with open('..\\..\\Results_1x4cages_failure\\U2\\cprocessed_Mul1x4Vel0.5Degree20.csv', 'rb') as handle:
#     resu = pickle.load(handle)

## Center point of cages - initial pos before loading ##
center = []
for i in range(0, 4):
    center.append(resui['collar' + str(i)]['FloaterCenterPos'][1000, 0:3])

## Center point of cages - pos after loading ##
center2 = []
### Intact model - 250, Failure mode - 1000 ###
for i in range(0, 4):
    center2.append(resui['collar' + str(i)]['FloaterCenterPos'][1000, 0:3])
## Buoy positions
buoy = []
for i in range(0, 5):
    for j in range(0, 2):
        buoy.append(resui['mooring3']['platePosition' + str(i) + '_' + str(j)][1000, 0:3])

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
'''
#################
  Initial state
#################
'''

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

## netting
pos0_i = np.zeros((321, 3))
for i in range(1, 322):
    pos0_i[i - 1][0] = resui['NetStructure0']['Pos_' + str(i)][1000, 0]
    pos0_i[i - 1][1] = resui['NetStructure0']['Pos_' + str(i)][1000, 1]
    pos0_i[i - 1][2] = resui['NetStructure0']['Pos_' + str(i)][1000, 2]
pos1_i = np.zeros((321, 3))
for i in range(1, 322):
    pos1_i[i - 1][0] = resui['NetStructure1']['Pos_' + str(i)][1000, 0]
    pos1_i[i - 1][1] = resui['NetStructure1']['Pos_' + str(i)][1000, 1]
    pos1_i[i - 1][2] = resui['NetStructure1']['Pos_' + str(i)][1000, 2]
pos2_i = np.zeros((321, 3))
for i in range(1, 322):
    pos2_i[i - 1][0] = resui['NetStructure2']['Pos_' + str(i)][1000, 0]
    pos2_i[i - 1][1] = resui['NetStructure2']['Pos_' + str(i)][1000, 1]
    pos2_i[i - 1][2] = resui['NetStructure2']['Pos_' + str(i)][1000, 2]
pos3_i = np.zeros((321, 3))
for i in range(1, 322):
    pos3_i[i - 1][0] = resui['NetStructure3']['Pos_' + str(i)][1000, 0]
    pos3_i[i - 1][1] = resui['NetStructure3']['Pos_' + str(i)][1000, 1]
    pos3_i[i - 1][2] = resui['NetStructure3']['Pos_' + str(i)][1000, 2]

mfi.drawCageV(pos0_i, ax1)
mfi.drawCageH(pos0_i, ax1)
mfi.drawCageV(pos1_i, ax1)
mfi.drawCageH(pos1_i, ax1)
mfi.drawCageV(pos2_i, ax1)
mfi.drawCageH(pos2_i, ax1)
mfi.drawCageV(pos3_i, ax1)
mfi.drawCageH(pos3_i, ax1)

##### Bridles


for cage in range(0, 4):
    ### Bridle 1-3 ###
    for i in range(1, 4):
        bx = [buoy[3 + 2 * cage][0], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 0]]
        by = [buoy[3 + 2 * cage][1], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 1]]
        bz = [buoy[3 + 2 * cage][2], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 2]]
        ax1.plot(bx, by, bz, color='k')

    ### Bridle 4-6 ###
    for i in range(4, 7):
        bx = [buoy[1 + 2 * cage][0], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 0]]
        by = [buoy[1 + 2 * cage][1], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 1]]
        bz = [buoy[1 + 2 * cage][2], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 2]]
        ax1.plot(bx, by, bz, color='k')

    ### Bridle 7-9 ###
    for i in range(7, 10):
        bx = [buoy[0 + 2 * cage][0], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 0]]
        by = [buoy[0 + 2 * cage][1], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 1]]
        bz = [buoy[0 + 2 * cage][2], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 2]]
        ax1.plot(bx, by, bz, color='k')

    ### Bridle 10-12 ###
    for i in range(10, 13):
        bx = [buoy[2 + 2 * cage][0], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 0]]
        by = [buoy[2 + 2 * cage][1], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 1]]
        bz = [buoy[2 + 2 * cage][2], resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 2]]
        ax1.plot(bx, by, bz, color='k')
    Con_pointsX = []
    Con_pointsY = []
    Con_pointsZ = []

    for i in range(1, 13):
        Con_pointsX = np.append(Con_pointsX, resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 0])
        Con_pointsY = np.append(Con_pointsY, resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 1])
        Con_pointsZ = np.append(Con_pointsZ, resui['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 2])
    Con_pointsX = np.append(Con_pointsX, Con_pointsX[0])
    Con_pointsY = np.append(Con_pointsY, Con_pointsY[0])
    Con_pointsZ = np.append(Con_pointsZ, Con_pointsZ[0])
    ax1.plot(Con_pointsX, Con_pointsY, Con_pointsZ, 'k', linewidth=5)

'''
#############
Shifted-cages
#############
'''
## Buoy positions
buoy_s = []
for i in range(0, 5):
    for j in range(0, 2):
        buoy_s.append(resu['mooring3']['platePosition' + str(i) + '_' + str(j)][1000, 0:3])

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

########## netting ###############
## netting
pos0_f = np.zeros((321, 3))
for i in range(1, 322):
    pos0_f[i - 1][0] = resu['NetStructure0']['Pos_' + str(i)][1000, 0]
    pos0_f[i - 1][1] = resu['NetStructure0']['Pos_' + str(i)][1000, 1]
    pos0_f[i - 1][2] = resu['NetStructure0']['Pos_' + str(i)][1000, 2]
pos1_f = np.zeros((321, 3))
for i in range(1, 322):
    pos1_f[i - 1][0] = resu['NetStructure1']['Pos_' + str(i)][1000, 0]
    pos1_f[i - 1][1] = resu['NetStructure1']['Pos_' + str(i)][1000, 1]
    pos1_f[i - 1][2] = resu['NetStructure1']['Pos_' + str(i)][1000, 2]
pos2_f = np.zeros((321, 3))
for i in range(1, 322):
    pos2_f[i - 1][0] = resu['NetStructure2']['Pos_' + str(i)][1000, 0]
    pos2_f[i - 1][1] = resu['NetStructure2']['Pos_' + str(i)][1000, 1]
    pos2_f[i - 1][2] = resu['NetStructure2']['Pos_' + str(i)][1000, 2]
pos3_f = np.zeros((321, 3))
for i in range(1, 322):
    pos3_f[i - 1][0] = resu['NetStructure3']['Pos_' + str(i)][1000, 0]
    pos3_f[i - 1][1] = resu['NetStructure3']['Pos_' + str(i)][1000, 1]
    pos3_f[i - 1][2] = resu['NetStructure3']['Pos_' + str(i)][1000, 2]

mff.drawCageV(pos0_f, ax1)
mff.drawCageH(pos0_f, ax1)

mff.drawCageV(pos1_f, ax1)
mff.drawCageH(pos1_f, ax1)

mff.drawCageV(pos2_f, ax1)
mff.drawCageH(pos2_f, ax1)

mff.drawCageV(pos3_f, ax1)
mff.drawCageH(pos3_f, ax1)

##### Bridles
for cage in range(0, 4):
    ### Bridle 1-3 ###
    for i in range(1, 4):
        bx = [buoy_s[3 + 2 * cage][0], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 0]]
        by = [buoy_s[3 + 2 * cage][1], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 1]]
        bz = [buoy_s[3 + 2 * cage][2], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 2]]
        ax1.plot(bx, by, bz, color='firebrick', alpha=0.6)

    ### Bridle 4-6 ###
    for i in range(4, 7):
        bx = [buoy_s[1 + 2 * cage][0], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 0]]
        by = [buoy_s[1 + 2 * cage][1], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 1]]
        bz = [buoy_s[1 + 2 * cage][2], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 2]]
        ax1.plot(bx, by, bz, color='firebrick', alpha=0.6)

    ### Bridle 7-9 ###
    for i in range(7, 10):
        bx = [buoy_s[0 + 2 * cage][0], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 0]]
        by = [buoy_s[0 + 2 * cage][1], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 1]]
        bz = [buoy_s[0 + 2 * cage][2], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 2]]
        ax1.plot(bx, by, bz, color='firebrick', alpha=0.6)

    ### Bridle 10-12 ###
    for i in range(10, 13):
        bx = [buoy_s[2 + 2 * cage][0], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 0]]
        by = [buoy_s[2 + 2 * cage][1], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 1]]
        bz = [buoy_s[2 + 2 * cage][2], resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 2]]
        ax1.plot(bx, by, bz, color='firebrick', alpha=0.6)

    Con_pointsX_f = []
    Con_pointsY_f = []
    Con_pointsZ_f = []

    for i in range(1, 13):
        Con_pointsX_f = np.append(Con_pointsX_f, resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 0])
        Con_pointsY_f = np.append(Con_pointsY_f, resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 1])
        Con_pointsZ_f = np.append(Con_pointsZ_f, resu['collar' + str(cage)]['FastConnectPos' + str(i)][1000, 2])
    Con_pointsX_f = np.append(Con_pointsX_f, Con_pointsX_f[0])
    Con_pointsY_f = np.append(Con_pointsY_f, Con_pointsY_f[0])
    Con_pointsZ_f = np.append(Con_pointsZ_f, Con_pointsZ_f[0])
    ax1.plot(Con_pointsX_f, Con_pointsY_f, Con_pointsZ_f, color='firebrick', alpha=0.6, linewidth=5)


plt.axis('off')
# plt.axis('equal')
plt.tight_layout(pad=0.0)
ax1.view_init(elev=50, azim=90)
plt.savefig('3d_plot_defromed_state(initial-intact-20deg).png', dpi=600)
