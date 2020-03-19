import pickle

### Intact model - 250, Failure mode - 1000 ###

# initial condition (no-loading)
with open('processed_resu1x4_noloading.csv', 'rb') as handle:
    resu_nl = pickle.load(handle)
######## intact model ########################
with open('..\\..\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree20.csv', 'rb') as handle:
    resui = pickle.load(handle)

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
    center.append(resu_nl['collar' + str(i)]['FloaterCenterPos'][1000, 0:3])

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

All_cables = np.ones((77, 2))
##################### mooring lines ##################################
Mooring_lines = np.zeros((14, 2))
Ux = []
Uy = []
Uz = []
Vx = []
Vy = []
Vz = []
adjust = [0, 1, 4, 3]
for i in range(0, 4):
    Ux.append(anchor_pos[i][0] - buoy[adjust[i] * i][0])
    Uy.append(anchor_pos[i][1] - buoy[adjust[i] * i][1])
    Uz.append(anchor_pos[i][2] - buoy[adjust[i] * i][2])
for i in range(0, 4):
    Mooring_lines[i][0] = np.sqrt(Ux[i] ** 2 + Uy[i] ** 2 + Uz[i] ** 2)

for i in range(0, 5):
    Vx.append(anchor_pos[i + 4][0] - buoy[i * 2][0])
    Vy.append(anchor_pos[i + 4][1] - buoy[i * 2][1])
    Vz.append(anchor_pos[i + 4][2] - buoy[i * 2][2])

adjust2 = [1 / 5, 1 / 2, 5 / 7, 7 / 8, 1]
for i in range(5, 10):
    Vx.append(anchor_pos[i + 4][0] - buoy[int(adjust2[i - 5] * i)][0])
    Vy.append(anchor_pos[i + 4][1] - buoy[int(adjust2[i - 5] * i)][1])
    Vz.append(anchor_pos[i + 4][2] - buoy[int(adjust2[i - 5] * i)][2])
for i in range(0, 10):
    Mooring_lines[i + 4][0] = np.sqrt(Vx[i] ** 2 + Vy[i] ** 2 + Vz[i] ** 2)

################# Frame cables ######################################
Frame_cables = np.zeros((13, 2))
FCUx = []
FCUy = []
FCUz = []
upper = np.arange(0, 8, 2)
lower = np.arange(1, 9, 2)
for i in upper:
    FCUx.append(buoy[i][0] - buoy[i + 2][0])
    FCUy.append(buoy[i][1] - buoy[i + 2][1])
    FCUz.append(buoy[i][2] - buoy[i + 2][2])
for i in lower:
    FCUx.append(buoy[i][0] - buoy[i + 2][0])
    FCUy.append(buoy[i][1] - buoy[i + 2][1])
    FCUz.append(buoy[i][2] - buoy[i + 2][2])
for i in range(0, 8):
    Frame_cables[i][0] = np.sqrt(FCUx[i] ** 2 + FCUy[i] ** 2 + FCUz[i] ** 2)
FCVx = []
FCVy = []
FCVz = []
for i in range(0, 10, 2):
    FCVx.append(buoy[i][0] - buoy[i + 1][0])
    FCVy.append(buoy[i][1] - buoy[i + 1][1])
    FCVz.append(buoy[i][2] - buoy[i + 1][2])
for i in range(0, 5):
    Frame_cables[i + 8][0] = np.sqrt(FCVx[i] ** 2 + FCVy[i] ** 2 + FCVz[i] ** 2)

conP1 = [4.97419, 5.49779, 6.02139]
conP2 = [3.40339, 3.92699, 4.45059]
conP3 = [1.8326, 2.35619, 2.87979]
conP4 = [0.261799, 0.785398, 1.309]
r = 25

############# Bridles #############################################
Bridles = np.zeros((48, 2))
Bx = []
By = []
Bz = []

for cage in range(0, 4):
    ############ Bridle 1 to 3 #######################
    for i in range(len(conP1)):
        Bx.append(buoy[3 + 2 * cage][0] - center[cage][0] + r * np.cos(conP1[i]))
        By.append(buoy[3 + 2 * cage][1] - center[cage][1] - r * np.sin(conP1[i]))
        Bz.append(buoy[3 + 2 * cage][2] - center[cage][2] - r * np.sin(conP1[i]))

        ############ Bridle 4 to 6 #######################
    for i in range(len(conP2)):
        Bx.append(buoy[1 + 2 * cage][0] - center[cage][0] + r * np.cos(conP2[i]))
        By.append(buoy[1 + 2 * cage][1] - center[cage][1] - r * np.sin(conP2[i]))
        Bz.append(buoy[1 + 2 * cage][2] - center[cage][2] - r * np.sin(conP2[i]))

        ############ Bridle 7 to 9 #######################
    for i in range(len(conP3)):
        Bx.append(buoy[0 + 2 * cage][0] - center[cage][0] + r * np.cos(conP3[i]))
        By.append(buoy[0 + 2 * cage][1] - center[cage][1] + r * np.cos(conP3[i]))
        Bz.append(buoy[0 + 2 * cage][2] - center[cage][2] + r * np.cos(conP3[i]))

        ############ Bridle 10 to 12 #####################
    for i in range(len(conP1)):
        Bx.append(buoy[2 + 2 * cage][0] - center[cage][0] + r * np.cos(conP4[i]))
        By.append(buoy[2 + 2 * cage][1] - center[cage][1] + r * np.cos(conP4[i]))
        Bz.append(buoy[2 + 2 * cage][2] - center[cage][2] + r * np.cos(conP4[i]))
for i in range(0, 48):
    Bridles[i][0] = np.sqrt(Bx[i] ** 2 + By[i] ** 2 + Bz[i] ** 2)
'''
# ######################################### shifted cage ###################################################
'''
## Center point of cages - pos after loading
center2 = []
for i in range(0, 4):
    center2.append(resui['collar' + str(i)]['FloaterCenterPos'][250, 0:3])
## Buoy positions
buoy_s = []
for i in range(0, 5):
    for j in range(0, 2):
        buoy_s.append(resui['mooring3']['platePosition' + str(i) + '_' + str(j)][250, 0:3])

##################### mooring lines ##################################
Ux_s = []
Uy_s = []
Uz_s = []
Vx_s = []
Vy_s = []
Vz_s = []
adjust = [0, 1, 4, 3]
for i in range(0, 4):
    Ux_s.append(anchor_pos[i][0] - buoy_s[adjust[i] * i][0])
    Uy_s.append(anchor_pos[i][1] - buoy_s[adjust[i] * i][1])
    Uz_s.append(anchor_pos[i][2] - buoy_s[adjust[i] * i][2])
for i in range(0, 4):
    Mooring_lines[i][1] = np.sqrt(Ux_s[i] ** 2 + Uy_s[i] ** 2 + Uz_s[i] ** 2)

for i in range(0, 5):
    Vx_s.append(anchor_pos[i + 4][0] - buoy_s[i * 2][0])
    Vy_s.append(anchor_pos[i + 4][1] - buoy_s[i * 2][1])
    Vz_s.append(anchor_pos[i + 4][2] - buoy_s[i * 2][2])

adjust2 = [1 / 5, 1 / 2, 5 / 7, 7 / 8, 1]
for i in range(5, 10):
    Vx_s.append(anchor_pos[i + 4][0] - buoy_s[int(adjust2[i - 5] * i)][0])
    Vy_s.append(anchor_pos[i + 4][1] - buoy_s[int(adjust2[i - 5] * i)][1])
    Vz_s.append(anchor_pos[i + 4][2] - buoy_s[int(adjust2[i - 5] * i)][2])
for i in range(0, 10):
    Mooring_lines[i + 4][1] = np.sqrt(Vx_s[i] ** 2 + Vy_s[i] ** 2 + Vz_s[i] ** 2)

################# Frame cables ######################################
FCUx_s = []
FCUy_s = []
FCUz_s = []
upper = np.arange(0, 8, 2)
lower = np.arange(1, 9, 2)
for i in upper:
    FCUx_s.append(buoy_s[i][0] - buoy_s[i + 2][0])
    FCUy_s.append(buoy_s[i][1] - buoy_s[i + 2][1])
    FCUz_s.append(buoy_s[i][2] - buoy_s[i + 2][2])
for i in lower:
    FCUx_s.append(buoy_s[i][0] - buoy_s[i + 2][0])
    FCUy_s.append(buoy_s[i][1] - buoy_s[i + 2][1])
    FCUz_s.append(buoy_s[i][2] - buoy_s[i + 2][2])
for i in range(0, 8):
    Frame_cables[i][1] = np.sqrt(FCUx_s[i] ** 2 + FCUy_s[i] ** 2 + FCUz_s[i] ** 2)
FCVx_s = []
FCVy_s = []
FCVz_s = []
for i in range(0, 10, 2):
    FCVx_s.append(buoy_s[i][0] - buoy_s[i + 1][0])
    FCVy_s.append(buoy_s[i][1] - buoy_s[i + 1][1])
    FCVz_s.append(buoy_s[i][2] - buoy_s[i + 1][2])
for i in range(0, 5):
    Frame_cables[i + 8][1] = np.sqrt(FCVx_s[i] ** 2 + FCVy_s[i] ** 2 + FCVz_s[i] ** 2)

conP1 = [4.97419, 5.49779, 6.02139]
conP2 = [3.40339, 3.92699, 4.45059]
conP3 = [1.8326, 2.35619, 2.87979]
conP4 = [0.261799, 0.785398, 1.309]
r = 25

############# Bridles #############################################
Bx_s = []
By_s = []
Bz_s = []

for cage in range(0, 4):
    ############ Bridle 1 to 3 #######################
    for i in range(len(conP1)):
        Bx_s.append(buoy_s[3 + 2 * cage][0] - center2[cage][0] + r * np.cos(conP1[i]))
        By_s.append(buoy_s[3 + 2 * cage][1] - center2[cage][1] - r * np.sin(conP1[i]))
        Bz_s.append(buoy_s[3 + 2 * cage][2] - center2[cage][2] - r * np.sin(conP1[i]))

        ############ Bridle 4 to 6 #######################
    for i in range(len(conP2)):
        Bx_s.append(buoy_s[1 + 2 * cage][0] - center2[cage][0] + r * np.cos(conP2[i]))
        By_s.append(buoy_s[1 + 2 * cage][1] - center2[cage][1] - r * np.sin(conP2[i]))
        Bz_s.append(buoy_s[1 + 2 * cage][2] - center2[cage][2] - r * np.sin(conP2[i]))

        ############ Bridle 7 to 9 #######################
    for i in range(len(conP3)):
        Bx_s.append(buoy_s[0 + 2 * cage][0] - center2[cage][0] + r * np.cos(conP3[i]))
        By_s.append(buoy_s[0 + 2 * cage][1] - center2[cage][1] + r * np.cos(conP3[i]))
        Bz_s.append(buoy_s[0 + 2 * cage][2] - center2[cage][2] + r * np.cos(conP3[i]))

        ############ Bridle 10 to 12 #####################
    for i in range(len(conP1)):
        Bx_s.append(buoy_s[2 + 2 * cage][0] - center2[cage][0] + r * np.cos(conP4[i]))
        By_s.append(buoy_s[2 + 2 * cage][1] - center2[cage][1] + r * np.cos(conP4[i]))
        Bz_s.append(buoy_s[2 + 2 * cage][2] - center2[cage][2] + r * np.cos(conP4[i]))
for i in range(0, 48):
    Bridles[i][1] = np.sqrt(Bx_s[i] ** 2 + By_s[i] ** 2 + Bz_s[i] ** 2)

for i in range(0, 14):
    All_cables[i][:] = Mooring_lines[i][:]
for i in range(0, 13):
    All_cables[len(Mooring_lines) + 1 + i][:] = Frame_cables[i][:]
for i in range(0, 48):
    All_cables[len(Mooring_lines) + 1 + len(Frame_cables) + 1 + i][:] = Bridles[i][:]

# import pandas as pd
# ## convert your array into a dataframe
# df = pd.DataFrame(All_cables)

# ## save to xlsx file
# filepath = 'Length_cables(1x4_initial_intact).xlsx'
# df.to_excel(filepath, index=False)
