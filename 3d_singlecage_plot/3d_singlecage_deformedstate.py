import numpy as np
import matplotlib.pyplot as plt
import magicFun as mf
import magicFun_initial as mfi

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (18.3, 9.5)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = '8'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"
import pickle

with open('dprocessed_Mul1x1Vel0.5Degree0.csv', 'rb') as handle:
    resui = pickle.load(handle)

############
# Enter Time#

time = 250
############

## Anchor positions : U anchors and V anchors in turn
anchor_pos = [[-150, -50, 80],
              [-150, 50, 80],
              [150, -50, 80],
              [150, 50, 80],
              [-50, -150, 80],
              [50, -150, 80],
              [-50, 150, 80],
              [50, 150, 80]
              ]
## Buoy positions
buoy = []
for i in range(0, 2):
    for j in range(0, 2):
        buoy.append(resui['mooring3']['platePosition' + str(i) + '_' + str(j)][time, 0:3])

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

# U anchors
for i in range(0, 4):
    moor_Ux.append([anchor_pos[i][0], buoy[i][0]])
    moor_Uy.append([anchor_pos[i][1], buoy[i][1]])
    moor_Uz.append([anchor_pos[i][2], buoy[i][2]])
# V anchors
adjust = [0, 2, 1 / 2, 1]
for i in range(0, 4):
    moor_Vx.append([anchor_pos[i + 4][0], buoy[int(adjust[i] * i)][0]])
    moor_Vy.append([anchor_pos[i + 4][1], buoy[int(adjust[i] * i)][1]])
    moor_Vz.append([anchor_pos[i + 4][2], buoy[int(adjust[i] * i)][2]])

for i in range(0, 4):
    plt.plot(moor_Ux[i], moor_Uy[i], moor_Uz[i], 'k')
for i in range(0, 4):
    plt.plot(moor_Vx[i], moor_Vy[i], moor_Vz[i], 'k')

################# Frame cables ######################################
FCUx = []
FCUy = []
FCUz = []
upper = [0]
lower = [1]
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
for i in range(0, 4, 2):
    FCVx.append([buoy[i][0], buoy[i + 1][0]])
    FCVy.append([buoy[i][1], buoy[i + 1][1]])
    FCVz.append([buoy[i][2], buoy[i + 1][2]])
for i in range(0, 2):
    plt.plot(FCUx[i], FCUy[i], FCUz[i], 'g')
for i in range(0, 2):
    plt.plot(FCVx[i], FCVy[i], FCVz[i], 'g')

## netting
pos_i = np.zeros((321, 3))
for i in range(1, 322):
    pos_i[i - 1][0] = resui['NetStructure0']['Pos_' + str(i)][time, 0]
    pos_i[i - 1][1] = resui['NetStructure0']['Pos_' + str(i)][time, 1]
    pos_i[i - 1][2] = resui['NetStructure0']['Pos_' + str(i)][time, 2]

pos_ini = np.zeros((321, 3))
for i in range(1, 322):
    pos_ini[i - 1][0] = resui['NetStructure0']['Pos_' + str(i)][0, 0]
    pos_ini[i - 1][1] = resui['NetStructure0']['Pos_' + str(i)][0, 1]
    pos_ini[i - 1][2] = resui['NetStructure0']['Pos_' + str(i)][0, 2]

mf.drawCageV(pos_i, ax1)
mf.drawCageH(pos_i, ax1)

mfi.drawCageV(pos_ini, ax1)
mfi.drawCageH(pos_ini, ax1)

##### Bridles


for cage in range(0, 1):
    ### Bridle 1-3 ###
    for i in range(1, 4):
        bx = [buoy[3 + 2 * cage][0], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 0]]
        by = [buoy[3 + 2 * cage][1], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 1]]
        bz = [buoy[3 + 2 * cage][2], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 2]]
        ax1.plot(bx, by, bz, color='firebrick')

    ### Bridle 4-6 ###
    for i in range(4, 7):
        bx = [buoy[1 + 2 * cage][0], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 0]]
        by = [buoy[1 + 2 * cage][1], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 1]]
        bz = [buoy[1 + 2 * cage][2], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 2]]
        ax1.plot(bx, by, bz, color='firebrick')

    ### Bridle 7-9 ###
    for i in range(7, 10):
        bx = [buoy[0 + 2 * cage][0], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 0]]
        by = [buoy[0 + 2 * cage][1], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 1]]
        bz = [buoy[0 + 2 * cage][2], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 2]]
        ax1.plot(bx, by, bz, color='firebrick')

    ### Bridle 10-12 ###
    for i in range(10, 13):
        bx = [buoy[2 + 2 * cage][0], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 0]]
        by = [buoy[2 + 2 * cage][1], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 1]]
        bz = [buoy[2 + 2 * cage][2], resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 2]]
        ax1.plot(bx, by, bz, color='firebrick')
    Con_pointsX = []
    Con_pointsY = []
    Con_pointsZ = []

    for i in range(1, 13):
        Con_pointsX = np.append(Con_pointsX, resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 0])
        Con_pointsY = np.append(Con_pointsY, resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 1])
        Con_pointsZ = np.append(Con_pointsZ, resui['collar' + str(cage)]['FastConnectPos' + str(i)][time, 2])
    Con_pointsX = np.append(Con_pointsX, Con_pointsX[0])
    Con_pointsY = np.append(Con_pointsY, Con_pointsY[0])
    Con_pointsZ = np.append(Con_pointsZ, Con_pointsZ[0])

    ax1.plot(Con_pointsX, Con_pointsY, Con_pointsZ, 'k', linewidth=5)

plt.axis('off')
ax1.view_init(elev=50, azim=90)
