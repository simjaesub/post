# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:16:07 2020

@author: shuer
"""


def matgen(degree, failure):
    import numpy as np
    import pickle
    with open('..\\..\\Results_singlecage_failure\\' + str(failure) + '_fail\\dprocessed_Mul1x1Vel0.5Degree' + str(
            degree) + '_' + str(failure) + '_fail.csv', 'rb') as handle:
        resuF = pickle.load(handle)

    with open('..\\..\\Results_singlecage_intact_d\\dprocessed_Mul1x1Vel0.5Degree' + str(degree) + '.csv',
              'rb') as handle:
        resu = pickle.load(handle)

    anchors = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4']
    anchors2 = ['U0_0_ForceA', 'U1_0_ForceA', 'U0_3_ForceB', 'U1_3_ForceB', 'V0_0_ForceA', 'V1_0_ForceA', 'V0_3_ForceB',
                'V1_3_ForceB']
    fcables = ['FCU1', 'FCU2', 'FCV1', 'FCV2']
    fcables2 = ['U0_1_ForceA', 'U1_1_ForceA', 'V0_1_ForceA', 'V1_1_ForceA']
    fmodes = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'FCU1', 'FCU2', 'FCV1', 'FCV2']

    ########### anchor line tensions #################################
    anchorF_intact = np.zeros((1, 8))
    for i in anchors2:
        x = np.mean(resu['mooring3']['frameCable' + i][240:250, 0])
        y = np.mean(resu['mooring3']['frameCable' + i][240:250, 1])
        z = np.mean(resu['mooring3']['frameCable' + i][240:250, 2])
        anchorF_intact[0][anchors2.index(i)] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000
    anchorF_fail = np.zeros((1, 8))
    for i in anchors2:
        xf = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 0])
        yf = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 1])
        zf = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 2])
        anchorF_fail[0][anchors2.index(i)] = np.sqrt(xf ** 2 + yf ** 2 + zf ** 2) / 1000

    ########### framecable tensions ################################# 
    fcableT_intact = np.zeros((1, 4))
    for i in fcables2:
        x1 = np.mean(resu['mooring3']['frameCable' + i][240:250, 0])
        y1 = np.mean(resu['mooring3']['frameCable' + i][240:250, 1])
        z1 = np.mean(resu['mooring3']['frameCable' + i][240:250, 2])
        fcableT_intact[0][fcables2.index(i)] = np.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2) / 1000
    fcableT_fail = np.zeros((1, 4))
    for i in fcables2:
        x2 = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 0])
        y2 = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 1])
        z2 = np.mean(resuF['mooring3']['frameCable' + i][980:1000, 2])
        fcableT_fail[0][fcables2.index(i)] = np.sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2) / 1000
    ######## Bridle tensions ############
    bridlenum = np.arange(12)
    bridles_intact = np.zeros((1, 12))
    bridles_fail = np.zeros((1, 12))

    for i in bridlenum:
        x = np.mean(resu['mooring3']['forceFloater0_0' + str(i)][240:250, 0])
        y = np.mean(resu['mooring3']['forceFloater0_0' + str(i)][240:250, 1])
        z = np.mean(resu['mooring3']['forceFloater0_0' + str(i)][240:250, 2])
        bridles_intact[0][i] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000

    for i in bridlenum:
        x = np.mean(resuF['mooring3']['forceFloater0_0' + str(i)][980:1000, 0])
        y = np.mean(resuF['mooring3']['forceFloater0_0' + str(i)][980:1000, 1])
        z = np.mean(resuF['mooring3']['forceFloater0_0' + str(i)][980:1000, 2])
        bridles_fail[0][i] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000

    ################## Row represents each failure mode from 0th row for U1 to 11th row for FCV2 in order of fmodes list #####################
    ############### Matrix column 0 - 7: anchor line tension (deviation from intact model) #############################
    for i in range(len(anchors)):
        mat[fmodes.index(failure)][i] = anchorF_intact[0][i] - anchorF_fail[0][i]

    ############### Matrix column 9 - 12: framecable tension (deviation from intact model) #############################
    for i in range(len(fcables)):
        mat[fmodes.index(failure)][len(anchors) + 1 + i] = fcableT_intact[0][i] - fcableT_fail[0][i]

    ############### Matrix column 14 - 25: bridle tension (deviation from intact model) ###############
    for i in range(len(bridles_intact)):
        mat[fmodes.index(failure)][len(anchors) + 1 + len(fcables) + 1 + i] = bridles_intact[0][i] - bridles_fail[0][i]

    ########### Matrix column 27: volume of the cage (deviation from the intact model) #################################
    vol_intact = np.mean(resu['NetStructure0']['VolumeEst'][240:250, 0])
    vol_fail = np.mean(resuF['NetStructure0']['VolumeEst'][980:1000, 0])
    mat[fmodes.index(failure)][len(anchors) + 1 + len(fcables) + 1 + len(bridles_fail) + 1] = vol_intact - vol_fail

    ###########Matrix column 29: total drag force of the cage (deviation from intact) ################################# 
    drag_intact = np.mean(resu['NetStructure0']['NodeSumDragForceAbs'][240:250, 0]) / 1000
    drag_fail = np.mean(resuF['NetStructure0']['NodeSumDragForceAbs'][980:1000, 0]) / 1000
    mat[fmodes.index(failure)][
        len(anchors) + 1 + len(fcables) + 1 + len(bridles_fail) + 1 + len(vol_intact)] = drag_intact - drag_fail

    ############## Matrix column 31 to 42 - deviation of buoy position between failuremode and intactmodel x,y,z direction ########
    ######## column 13, 14, 15 are displacement in x,y,z direction for buoy 1 and so on #################################
    B_posi = np.zeros((12, 1))
    B_posf = np.zeros((12, 1))

    buoys = ['0_0', '0_1', '1_0', '1_1']
    order = np.arange(0, 12, 3)
    for i in order:
        B_posi[i][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][230:250, 0])
        B_posi[i + 1][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][230:250, 1])
        B_posi[i + 2][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][230:250, 2])

    for i in order:
        B_posf[i][0] = np.mean(resuF['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][980:1000, 0])
        B_posf[i + 1][0] = np.mean(resuF['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][980:1000, 1])
        B_posf[i + 2][0] = np.mean(resuF['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][980:1000, 2])

    B_pos = B_posi - B_posf
    for i in range(len(B_pos)):
        mat[fmodes.index(failure)][
            len(anchors) + 1 + len(fcables) + 1 + len(bridles_fail) + 1 + len(vol_intact) + 1 + i] = B_pos[i][0]


failuremodes = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'FCU1', 'FCU2', 'FCV1', 'FCV2']
import numpy as np

mat = np.ones((12, 43))
theta = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
for failure in failuremodes:
    matgen(0, failure)
