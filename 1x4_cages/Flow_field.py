# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:03:47 2020

@author: shuer
"""

import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (16.3, 8)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = '10'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"
centerOf8Cages = [[-150, 50],
                  [-50, 50],
                  [50, 50],
                  [150, 50]]


def velor(orgcoor, theta, xcoor, ycoor):
    Sn = 0.2
    xcoor -= orgcoor[0]
    ycoor -= orgcoor[1]
    coor = np.array([xcoor, ycoor])
    localcoor = np.dot(np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]), coor)
    xcoor = localcoor[0] - 25
    ycoor = localcoor[1]
    if 0 < xcoor < 50 * 40 and -1 < ycoor / 50 < 1:
        a0 = 0.02402 * 5
        a1 = 0.04824 * 5
        a2 = 0.002303 * 5
        a3 = -0.01288 * 5
        a4 = 0.0006093 * 5
        a5 = 0.005875 * 5
        a6 = -0.001147 * 5
        a7 = -0.002984 * 5
        w = 2.692
        vr = (a0 \
              + a1 * np.cos(1 * ycoor / 50 * w) \
              + a2 * np.cos(2 * ycoor / 50 * w) \
              + a3 * np.cos(3 * ycoor / 50 * w) \
              + a4 * np.cos(4 * ycoor / 50 * w) \
              + a5 * np.cos(5 * ycoor / 50 * w) \
              + a6 * np.cos(6 * ycoor / 50 * w) \
              + a7 * np.cos(7 * ycoor / 50 * w)) * (Sn / 0.25) * np.sqrt(np.exp(-(xcoor / 50 - 1.5) / 25))
    else:
        vr = 0
    return vr


X = np.linspace(-50 * 6, 50 * 6, 400)
Y = np.linspace(-50 * 4, 50 * 4, 240)
Z = np.ones((len(Y), len(X)))
thetadegree = [i for i in range(0, 10, 10)]

for tha in thetadegree:
    theta = tha * np.pi / 180
    for cage in centerOf8Cages:
        for x in range(len(X)):
            for y in range(len(Y)):
                Z[y][x] -= velor(cage, theta, X[x], Y[y])

    plt.figure(figsize=(6.3, 3.5))
    plt.contourf(X, Y, np.abs(Z), levels=np.linspace(0, 1.5, 16), cmap=cm.jet)
    cbar = plt.colorbar()
    cbar.set_label("Velocity reduction factor ")
    Z = np.ones((len(Y), len(X)))  # back to 1 for next contour plot
    # >>>>>>>plot circle
    r = 25  # fish cage 0.5*diameter
    circlethera = np.linspace(0, 2 * np.pi, 100)
    for cage in centerOf8Cages:
        xc = cage[0] + r * np.cos(circlethera)
        yc = cage[1] + r * np.sin(circlethera)
        plt.plot(xc, yc, '-k')
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
        for i in range(-25, 25, 8):
            y = i + cage[1]
            plt.hlines(y, cage[0] - np.sqrt(r ** 2 - (y - cage[1]) ** 2),
                       cage[0] + np.sqrt(r ** 2 - (y - cage[1]) ** 2), colors='k', linestyle='solid')
        for i in range(-25, 25, 8):
            x = i + cage[0]
            plt.vlines(x, cage[1] - np.sqrt(r ** 2 - (x - cage[0]) ** 2),
                       cage[1] + np.sqrt(r ** 2 - (x - cage[0]) ** 2), colors='k', linestyle='solid')
        if centerOf8Cages.index(cage) <= 3:
            plt.text(cage[0] - 25, cage[1] + 56, 'Cage ' + str(centerOf8Cages.index(cage) + 1), weight='bold',
                     fontsize=10, color='k')
        else:
            plt.text(cage[0] - 25, cage[1] - 66, 'Cage ' + str(centerOf8Cages.index(cage) + 1), weight='bold',
                     fontsize=10, color='k')

    plt.xlim([-300, 300])
    plt.ylim([-100, 200])
    plt.xlabel('$X$ (m)')
    plt.ylabel('$Y$ (m)')
    plt.figaspect(1)
    plt.tight_layout()
    # plt.title("The flow direction is "+str(tha)+" degree")
    plt.savefig('.\\1x4_cages_figures\\1x4cages_vel_contour' + str(tha) + 'Deg.png', dpi=600)
