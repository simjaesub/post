# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:31:57 2020

@author: shuer
"""


def matgen(degree, failure):
    import numpy as np
    import pickle
    with open('..\\..\\..\\OneDrive - Universitetet i Stavanger\\Fhsim_wake\\bin\\Results_1x4cages_failure\\' + str(
            failure) + '\\cprocessed_Mul1x4Vel0.5Degree' + str(
            degree) + '.csv', 'rb') as handle:
        resuF = pickle.load(handle)

    with open(
            '..\\..\\..\\OneDrive - Universitetet i Stavanger\\Fhsim_wake\\bin\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree' + str(
                    degree) + '.csv',
            'rb') as handle:
        resu = pickle.load(handle)

    anchors = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10']
    anchors2 = ['U0_0_ForceA', 'U1_0_ForceA', 'U0_6_ForceB', 'U1_6_ForceB', 'V0_0_ForceA', 'V1_0_ForceA',
                'V2_0_ForceA', 'V3_0_ForceA', 'V4_0_ForceA', 'V0_3_ForceB', 'V1_3_ForceB', 'V2_3_ForceB',
                'V3_3_ForceB', 'V4_3_ForceB']
    fcables = ['FCU1', 'FCU2', 'FCU3', 'FCU4', 'FCU5', 'FCU6', 'FCU7', 'FCU8', 'FCV1', 'FCV2', 'FCV3', 'FCV4', 'FCV5']
    fcables2 = ['U0_1_ForceA', 'U0_2_ForceA', 'U0_3_ForceA', 'U0_4_ForceA', 'U1_1_ForceA', 'U1_2_ForceA', 'U1_3_ForceA',
                'U1_4_ForceA', 'V0_1_ForceA', 'V1_1_ForceA', 'V2_1_ForceA', 'V3_1_ForceA', 'V4_1_ForceA']
    fmodes = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
              'FCU1', 'FCU2', 'FCU3', 'FCU4', 'FCU5', 'FCU6', 'FCU7', 'FCU8', 'FCV1', 'FCV2', 'FCV3', 'FCV4', 'FCV5']

    ########### anchor line tensions #################################
    anchorF_intact = np.zeros((1, 14))
    for i in anchors2:
        x = np.mean(resu['mooring3']['frameCable' + i][240:250, 0])
        y = np.mean(resu['mooring3']['frameCable' + i][240:250, 1])
        z = np.mean(resu['mooring3']['frameCable' + i][240:250, 2])
        anchorF_intact[0][anchors2.index(i)] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000
    anchorF_fail = np.zeros((1, 14))
    for i in anchors2:
        xf = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 0])
        yf = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 1])
        zf = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 2])
        anchorF_fail[0][anchors2.index(i)] = np.sqrt(xf ** 2 + yf ** 2 + zf ** 2) / 1000

    ########### framecable tensions #################################
    fcableT_intact = np.zeros((1, 13))
    for i in fcables2:
        x1 = np.mean(resu['mooring3']['frameCable' + i][240:250, 0])
        y1 = np.mean(resu['mooring3']['frameCable' + i][240:250, 1])
        z1 = np.mean(resu['mooring3']['frameCable' + i][240:250, 2])
        fcableT_intact[0][fcables2.index(i)] = np.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2) / 1000
    fcableT_fail = np.zeros((1, 13))
    for i in fcables2:
        x2 = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 0])
        y2 = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 1])
        z2 = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 2])
        fcableT_fail[0][fcables2.index(i)] = np.sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2) / 1000
    ########### bridle tensions #################################
    bridlenum = np.arange(12)
    bridles = np.zeros((48, 1))
    for j in range(0, 4):
        for i in bridlenum:
            x = np.mean(resuF['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 0])
            y = np.mean(resuF['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 1])
            z = np.mean(resuF['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 2])
            bridles[12 * j + i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000

    ################## Row represents each failure mode from 0th row for U1 to 11th row for FCV2 in order of fmodes list #####################
    ############### Matrix column 0 - 13: anchor line tension (percentage of deviation compared to correspoding failure mode) #############################
    for i in range(len(anchors)):
        mat[fmodes.index(failure)][i] = anchorF_fail[0][i]

    ############### Matrix column 15 - 27: framecable tension (percentage of deviation compared to correspoding failure mode) #############################
    for i in range(len(fcables)):
        mat[fmodes.index(failure)][len(anchors) + 1 + i] = fcableT_fail[0][i]

    ############### Matrix column 29 - 76: bridle tension (percentage of deviation compared to correspoding failure mode) #############################
    for i in range(len(bridles)):
        mat[fmodes.index(failure)][len(anchors) + 1 + len(fcables) + 1 + i] = bridles[i][0]
    ########### Matrix column 78 - 81: volume of the cage (percentage of deviation compared to correspoding failure mode) #################################
    vol_intact = np.zeros((1, 4))
    for i in range(0, 4):
        vol_intact[0][i] = np.mean(resu['NetStructure0']['VolumeEst'][240:250, 0])
    vol_fail = np.zeros((1, 4))
    for i in range(0, 4):
        vol_fail[0][i] = np.mean(resuF['NetStructure' + str(i)]['VolumeEst'][980:1000, 0])
        mat[fmodes.index(failure)][len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + i] = vol_fail[0][i]

    ###########Matrix column 83 - 86: total drag force of the cage (percentage of deviation compared to correspoding failure mode) #################################
    drag_intact = np.zeros((1, 4))
    for i in range(0, 4):
        drag_intact[0][i] = np.mean(resuF['NetStructure0']['NodeSumDragForceAbs'][240:250, 0]) / 1000
    drag_fail = np.zeros((1, 4))
    for i in range(0, 4):
        drag_fail[0][i] = np.mean(resuF['NetStructure0']['NodeSumDragForceAbs'][980:1000, 0]) / 1000
        mat[fmodes.index(failure)][
            len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + len(vol_fail[0][:]) + 1 + i] = drag_fail[0][i]

    ############## Matrix column 88 to 117 - deviation of buoy position between failuremode and intactmodel x,y,z direction ########
    ######## column 88, 89, 90 are displacementS in x,y,z direction for buoy 1 and so on. Buoys are numbered in turn for positive y direction #################################
    ############# Buoy 1,2 is attached to FCV1, Buoy 3,4 are attached top FCV2 and so on ###############
    B_posi = np.zeros((30, 1))
    B_posf = np.zeros((30, 1))

    buoys = ['0_0', '0_1', '1_0', '1_1', '2_0', '2_1', '3_0', '3_1', '4_0', '4_1']
    order = np.arange(0, 30, 3)
    for i in order:
        B_posi[i][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][240:250, 0])
        B_posi[i + 1][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][240:250, 1])
        B_posi[i + 2][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][240:250, 2])

    for i in order:
        B_posf[i][0] = np.mean(resuF['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][980:1000, 0])
        B_posf[i + 1][0] = np.mean(resuF['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][980:1000, 1])
        B_posf[i + 2][0] = np.mean(resuF['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][980:1000, 2])

    B_pos = B_posi - B_posf
    for i in range(len(B_pos)):
        mat[fmodes.index(failure)][
            len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + len(vol_fail[0][:]) + 1 + len(
                drag_fail[0][:]) + 1 + i] = B_pos[i][0]


failuremodes = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                'FCU1', 'FCU2', 'FCU3', 'FCU4', 'FCU5', 'FCU6', 'FCU7', 'FCU8', 'FCV1', 'FCV2', 'FCV3', 'FCV4', 'FCV5']
import numpy as np

mat = np.ones((27, 118))
theta = np.arange(0, 100, 10)
for failure in failuremodes:
    matgen(10, failure)

# import pandas as pd
# shit = pd.DataFrame(mat)

# shit.to_excel('matgen0deg.xlsx')
