# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:30:44 2020

@author: Jaesub
"""

import numpy as np
import pickle

mat = np.ones((10, 118))


def matgen(deg):
    with open(
            '..\\..\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree' + str(
                deg) + '.csv', 'rb') as handle:
        resu = pickle.load(handle)

    anchors = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10']
    AF_keyword = ['U0_0_ForceA', 'U1_0_ForceA', 'U0_6_ForceB', 'U1_6_ForceB', 'V0_0_ForceA', 'V1_0_ForceA',
                  'V2_0_ForceA', 'V3_0_ForceA', 'V4_0_ForceA', 'V0_3_ForceB', 'V1_3_ForceB', 'V2_3_ForceB',
                  'V3_3_ForceB', 'V4_3_ForceB']
    fcables = ['FCU1', 'FCU2', 'FCU3', 'FCU4', 'FCU5', 'FCU6', 'FCU7', 'FCU8', 'FCV1', 'FCV2', 'FCV3', 'FCV4', 'FCV5']
    FC_keyword = ['U0_1_ForceA', 'U0_2_ForceA', 'U0_3_ForceA', 'U0_4_ForceA', 'U1_1_ForceA', 'U1_2_ForceA',
                  'U1_3_ForceA',
                  'U1_4_ForceA', 'V0_1_ForceA', 'V1_1_ForceA', 'V2_1_ForceA', 'V3_1_ForceA', 'V4_1_ForceA']

    ## 0deg: 0-418s [0-836] // 10deg: 0-442s [0-884] // all the other degs: 0-500s [0-1000]
    ## 0deg: 0-418s [0-836] // 10deg: 0-442s [0-884] // all the other degs: 0-500s [0-1000]
    ## 0deg: 0-418s [0-836] // 10deg: 0-442s [0-884] // all the other degs: 0-500s [0-1000]
    ########### anchor line tensions #################################
    anchorF = np.zeros((1, 14))
    if deg == 0:
        for i in AF_keyword:
            x = np.mean(resu['mooring3']['frameCable' + i][820:836, 0])
            y = np.mean(resu['mooring3']['frameCable' + i][820:836, 1])
            z = np.mean(resu['mooring3']['frameCable' + i][820:836, 2])
            anchorF[0][AF_keyword.index(i)] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000
    if deg == 10:
        for i in AF_keyword:
            x = np.mean(resu['mooring3']['frameCable' + i][860:884, 0])
            y = np.mean(resu['mooring3']['frameCable' + i][860:884, 1])
            z = np.mean(resu['mooring3']['frameCable' + i][860:884, 2])
            anchorF[0][AF_keyword.index(i)] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000
    if deg >= 20:
        for i in AF_keyword:
            x = np.mean(resu['mooring3']['frameCable' + i][980:1000, 0])
            y = np.mean(resu['mooring3']['frameCable' + i][980:1000, 1])
            z = np.mean(resu['mooring3']['frameCable' + i][980:1000, 2])
            anchorF[0][AF_keyword.index(i)] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000

    ########### framecable tensions #################################
    frameCT = np.zeros((1, 13))
    if deg == 0:
        for i in FC_keyword:
            x1 = np.mean(resu['mooring3']['frameCable' + i][820:836, 0])
            y1 = np.mean(resu['mooring3']['frameCable' + i][820:836, 1])
            z1 = np.mean(resu['mooring3']['frameCable' + i][820:836, 2])
            frameCT[0][FC_keyword.index(i)] = np.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2) / 1000
    if deg == 10:
        for i in FC_keyword:
            x1 = np.mean(resu['mooring3']['frameCable' + i][860:884, 0])
            y1 = np.mean(resu['mooring3']['frameCable' + i][860:884, 1])
            z1 = np.mean(resu['mooring3']['frameCable' + i][860:884, 2])
            frameCT[0][FC_keyword.index(i)] = np.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2) / 1000
    if deg >= 20:
        for i in FC_keyword:
            x1 = np.mean(resu['mooring3']['frameCable' + i][980:1000, 0])
            y1 = np.mean(resu['mooring3']['frameCable' + i][980:1000, 1])
            z1 = np.mean(resu['mooring3']['frameCable' + i][980:1000, 2])
            frameCT[0][FC_keyword.index(i)] = np.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2) / 1000

    ########### bridle tensions #################################
    bridlenum = np.arange(12)
    bridles = np.zeros((48, 1))
    if deg == 0:
        for j in range(0, 4):
            for i in bridlenum:
                x = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][820:836, 0])
                y = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][820:836, 1])
                z = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][820:836, 2])
                bridles[12 * j + i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000
    if deg == 10:
        for j in range(0, 4):
            for i in bridlenum:
                x = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][860:884, 0])
                y = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][860:884, 1])
                z = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][860:884, 2])
                bridles[12 * j + i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000
    if deg >= 20:
        for j in range(0, 4):
            for i in bridlenum:
                x = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 0])
                y = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 1])
                z = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 2])
                bridles[12 * j + i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000

    #### Row represents each failure mode from 0th row for U1 to 11th row for FCV2 in order of fmodes list ####
    ############### Matrix column 0 - 13: anchor line tension  #############################
    if deg == 0:
        for i in range(len(anchors)):
            mat[0][i] = anchorF[0][i]

    if deg == 10:
        for i in range(len(anchors)):
            mat[1][i] = anchorF[0][i]

    if deg >= 20:
        for i in range(len(anchors)):
            mat[int(deg / 10)][i] = anchorF[0][i]

    ############### Matrix column 15 - 27: framecable tension  #############################
    if deg == 0:
        for i in range(len(fcables)):
            mat[0][len(anchors) + 1 + i] = frameCT[0][i]

    if deg == 10:
        for i in range(len(fcables)):
            mat[1][len(anchors) + 1 + i] = frameCT[0][i]

    if deg >= 20:
        for i in range(len(fcables)):
            mat[int(deg / 10)][len(anchors) + 1 + i] = frameCT[0][i]

    ############### Matrix column 29 - 76: bridle tension  #############################
    if deg == 0:
        for i in range(len(bridles)):
            mat[0][len(anchors) + 1 + len(fcables) + 1 + i] = bridles[i][0]

    if deg == 10:
        for i in range(len(bridles)):
            mat[1][len(anchors) + 1 + len(fcables) + 1 + i] = bridles[i][0]

    if deg >= 20:
        for i in range(len(bridles)):
            mat[int(deg / 10)][len(anchors) + 1 + len(fcables) + 1 + i] = bridles[i][0]

    ########### Matrix column 78 - 81: Cultivation volumes of the cages  #################################
    vol_intact = np.zeros((1, 4))
    if deg == 0:
        for i in range(0, 4):
            vol_intact[0][i] = np.mean(resu['NetStructure' + str(i)]['VolumeEst'][820:836, 0])
            mat[0][len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + i] = vol_intact[0][i]
    if deg == 10:
        for i in range(0, 4):
            vol_intact[0][i] = np.mean(resu['NetStructure' + str(i)]['VolumeEst'][860:884, 0])
            mat[1][len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + i] = vol_intact[0][i]
    if deg >= 20:
        for i in range(0, 4):
            vol_intact[0][i] = np.mean(resu['NetStructure' + str(i)]['VolumeEst'][980:1000, 0])
            mat[int(deg / 10)][len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + i] = vol_intact[0][i]

    ########### Matrix column 83 - 86: total drag force of the cages  #################################
    drag_intact = np.zeros((1, 4))
    if deg == 0:
        for i in range(0, 4):
            drag_intact[0][i] = np.mean(resu['NetStructure' + str(i)]['NodeSumDragForceAbs'][820:836, 0]) / 1000
            mat[0][len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + len(vol_intact[0][:]) + 1 + i] = \
                drag_intact[0][i]

    if deg == 10:
        for i in range(0, 4):
            drag_intact[0][i] = np.mean(resu['NetStructure' + str(i)]['NodeSumDragForceAbs'][860:884, 0]) / 1000
            mat[1][len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + len(vol_intact[0][:]) + 1 + i] = \
                drag_intact[0][i]

    if deg >= 20:
        for i in range(0, 4):
            drag_intact[0][i] = np.mean(resu['NetStructure' + str(i)]['NodeSumDragForceAbs'][980:1000, 0]) / 1000
            mat[int(deg / 10)][len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + len(vol_intact[0][:]) + 1 + i] = \
                drag_intact[0][i]

    ############# Matrix column 88 to 117 - deviation of buoy position between failuremode and intactmodel x,y,z direction ########
    ####### column 88, 89, 90 are displacementS in x,y,z direction for buoy 1 and so on. Buoys are numbered in turn for positive y direction #################################
    ############ Buoy 1,2 is attached to FCV1, Buoy 3,4 are attached top FCV2 and so on ###############
    B_posi = np.zeros((30, 1))
    B_pos_shift = np.zeros((30, 1))
    buoys = ['0_0', '0_1', '1_0', '1_1', '2_0', '2_1', '3_0', '3_1', '4_0', '4_1']
    order = np.arange(0, 30, 3)
    if deg == 0:
        for i in order:
            B_posi[i][0] = resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][0, 0]
            B_posi[i + 1][0] = resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][0, 1]
            B_posi[i + 2][0] = resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][0, 2]
        for i in order:
            B_pos_shift[i][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][820:836, 0])
            B_pos_shift[i + 1][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][820:836, 1])
            B_pos_shift[i + 2][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][820:836, 2])
        B_pos = B_posi - B_pos_shift
        for i in range(len(B_pos)):
            mat[0][
                len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + len(vol_intact[0][:]) + 1 + len(
                    drag_intact[0][:]) + 1 + i] = B_pos[i][0]
    if deg == 10:
        for i in order:
            B_posi[i][0] = resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][0, 0]
            B_posi[i + 1][0] = resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][0, 1]
            B_posi[i + 2][0] = resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][0, 2]
        for i in order:
            B_pos_shift[i][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][860:884, 0])
            B_pos_shift[i + 1][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][860:884, 1])
            B_pos_shift[i + 2][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][860:884, 2])
        B_pos = B_posi - B_pos_shift
        for i in range(len(B_pos)):
            mat[1][
                len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + len(vol_intact[0][:]) + 1 + len(
                    drag_intact[0][:]) + 1 + i] = B_pos[i][0]
    if deg >= 20:
        for i in order:
            B_posi[i][0] = resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][0, 0]
            B_posi[i + 1][0] = resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][0, 1]
            B_posi[i + 2][0] = resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][0, 2]
        for i in order:
            B_pos_shift[i][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][980:1000, 0])
            B_pos_shift[i + 1][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][980:1000, 1])
            B_pos_shift[i + 2][0] = np.mean(resu['mooring3']['buoyPosition' + str(buoys[int(i / 3)])][980:1000, 2])
        B_pos = B_posi - B_pos_shift
        for i in range(len(B_pos)):
            mat[int(deg / 10)][
                len(anchors) + 1 + len(fcables) + 1 + len(bridles) + 1 + len(vol_intact[0][:]) + 1 + len(
                    drag_intact[0][:]) + 1 + i] = B_pos[i][0]


theta = np.arange(0, 100, 10)
for deg in theta:
    matgen(deg)
