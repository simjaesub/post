# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:31:02 2020

@author: shuer
"""

import numpy as np

import matplotlib.pyplot as plt

plt.figure()

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (16.3, 8)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = '10'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"
centerOf8Cages = [[-150, 50],
                  [-50, 50],
                  [50, 50],
                  [150, 50],
                  ]
r = 25
circletheta = np.linspace(0, 2 * np.pi, 100)
for cage in centerOf8Cages:
    xc = cage[0] + r * np.cos(circletheta)
    yc = cage[1] + r * np.sin(circletheta)
    plt.plot(xc, yc, '-k', linewidth=2)
    ########## frame cable and mooring line ###############
    f1x = [cage[0] - 50, cage[0] + 50]
    f1y = [cage[1] - 50, cage[1] - 50]

    f2x = [cage[0] - 50, cage[0] + 50]
    f2y = [cage[1] + 50, cage[1] + 50]

    f3x = [cage[0] - 50, cage[0] - 50]
    f3y = [cage[1] + 50, cage[1] - 50]

    f4x = [cage[0] + 50, cage[0] + 50]
    f4y = [cage[1] + 50, cage[1] - 50]

    u1x = [cage[0] - 150, cage[0] - 50]
    u1y = [cage[1] - 50, cage[1] - 50]

    u2x = [cage[0] - 150, cage[0] - 50]
    u2y = [cage[1] + 50, cage[1] + 50]

    u3x = [cage[0] + 50, cage[0] + 150]
    u3y = [cage[1] - 50, cage[1] - 50]

    u4x = [cage[0] + 50, cage[0] + 150]
    u4y = [cage[1] + 50, cage[1] + 50]

    v1x = [cage[0] - 50, cage[0] - 50]
    v1y = [cage[1] - 50, cage[1] - 150]

    v2x = [cage[0] + 50, cage[0] + 50]
    v2y = [cage[1] - 50, cage[1] - 150]

    v3x = [cage[0] - 50, cage[0] - 50]
    v3y = [cage[1] + 50, cage[1] + 150]

    v4x = [cage[0] + 50, cage[0] + 50]
    v4y = [cage[1] + 50, cage[1] + 150]
    plt.plot(f1x, f1y, '-k')
    plt.plot(f2x, f2y, '-k')
    plt.plot(f3x, f3y, '-k')
    plt.plot(f4x, f4y, '-k')
    plt.plot(u1x, u1y, '-k')
    plt.plot(u2x, u2y, '-k')
    plt.plot(u3x, u3y, '-k')
    plt.plot(u4x, u4y, '-k')
    plt.plot(v1x, v1y, '-k')
    plt.plot(v2x, v2y, '-k')
    plt.plot(v3x, v3y, '-k')
    plt.plot(v4x, v4y, '-k')

    conP1 = [0.261799, 0.785398, 1.309]
    conP2 = [1.8326, 2.35619, 2.87979]
    conP3 = [3.40339, 3.92699, 4.45059]
    conP4 = [4.97419, 5.49779, 6.02139]

    buoyx = [cage[0] + 50, cage[0] - 50, cage[0] - 50, cage[0] + 50]
    buoyy = [cage[1] - 50, cage[1] - 50, cage[1] + 50, cage[1] + 50]
    ############ Bridle 1 to 3 #######################
    for i in range(len(conP1)):
        bx = [buoyx[0], cage[0] + r * np.cos(conP1[i])]
        by = [buoyy[0], cage[1] - r * np.sin(conP1[i])]
        plt.plot(bx, by, '-k')
    ############ Bridle 4 to 6 #######################    
    for i in range(len(conP2)):
        bx = [buoyx[1], cage[0] + r * np.cos(conP2[i])]
        by = [buoyy[1], cage[1] - r * np.sin(conP2[i])]
        plt.plot(bx, by, '-k')
        ############ Bridle 7 to 9 #######################
    for i in range(len(conP3)):
        bx = [buoyx[2], cage[0] + r * np.cos(conP3[i])]
        by = [buoyy[2], cage[1] - r * np.sin(conP3[i])]
        plt.plot(bx, by, '-k')
        ############ Bridle 10 to 12 #####################
    for i in range(len(conP1)):
        bx = [buoyx[3], cage[0] + r * np.cos(conP4[i])]
        by = [buoyy[3], cage[1] - r * np.sin(conP4[i])]
        plt.plot(bx, by, '-k')

    for i in range(-25, 25, 4):
        y = i + cage[1]
        plt.hlines(y, cage[0] - np.sqrt(r ** 2 - (y - cage[1]) ** 2), cage[0] + np.sqrt(r ** 2 - (y - cage[1]) ** 2),
                   colors='k', linestyle='solid')
    for i in range(-25, 25, 4):
        x = i + cage[0]
        plt.vlines(x, cage[1] - np.sqrt(r ** 2 - (x - cage[0]) ** 2), cage[1] + np.sqrt(r ** 2 - (x - cage[0]) ** 2),
                   colors='k', linestyle='solid')
    if centerOf8Cages.index(cage) <= 3:
        plt.text(cage[0] - 20, cage[1] + 35, 'Cage ' + str(centerOf8Cages.index(cage) + 1), weight='bold', fontsize=20,
                 color='firebrick')
    else:
        plt.text(cage[0] - 20, cage[1] - 46, 'Cage ' + str(centerOf8Cages.index(cage) + 1), weight='bold', fontsize=20,
                 color='firebrick')

    # add cage number
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('multicage_drawing.png', dpi=600)
