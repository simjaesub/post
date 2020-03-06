center2 = 22

## Buoy positions
buoy_s = []
for i in range(0, 5):
    for j in range(0, 2):
        buoy_s.append(resu_i['mooring3']['platePosition' + str(i) + '_' + str(j)][1000, 0:2])

##################### mooring lines ##################################

moor_Ux_s = []
moor_Uy_s = []
moor_Vx_s = []
moor_Vy_s = []
adjust = [0, 1, 4, 3]
for i in range(0, 4):
    moor_Ux_s.append([anchor_pos[i][0], buoy_s[adjust[i] * i][0]])
for i in range(0, 4):
    moor_Uy_s.append([anchor_pos[i][1], buoy_s[adjust[i] * i][1]])

for i in range(0, 5):
    moor_Vx_s.append([anchor_pos[i + 4][0], buoy_s[i * 2][0]])
    moor_Vy_s.append([anchor_pos[i + 4][1], buoy_s[i * 2][1]])

adjust2 = [1 / 5, 1 / 2, 5 / 7, 7 / 8, 1]
for i in range(5, 10):
    moor_Vx_s.append([anchor_pos[i + 4][0], buoy_s[int(adjust2[i - 5] * i)][0]])
    moor_Vy_s.append([anchor_pos[i + 4][1], buoy_s[int(adjust2[i - 5] * i)][1]])

for i in range(0, 4):
    plt.plot(moor_Ux_s[i], moor_Uy_s[i], 'k')
for i in range(0, 10):
    plt.plot(moor_Vx_s[i], moor_Vy_s[i], 'k')

################# Frame cables ######################################
FCUx_s = []
FCUy_s = []
upper = np.arange(0, 8, 2)
lower = np.arange(1, 9, 2)
for i in upper:
    FCUx_s.append([buoy_s[i][0], buoy_s[i + 2][0]])
for i in upper:
    FCUy_s.append([buoy_s[i][1], buoy_s[i + 2][1]])
for i in lower:
    FCUx_s.append([buoy_s[i][0], buoy_s[i + 2][0]])
for i in lower:
    FCUy_s.append([buoy_s[i][1], buoy_s[i + 2][1]])

FCVx_s = []
FCVy_s = []
for i in range(0, 10, 2):
    FCVx_s.append([buoy_s[i][0], buoy_s[i + 1][0]])
for i in range(0, 10, 2):
    FCVy_s.append([buoy_s[i][1], buoy_s[i + 1][1]])
for i in range(0, 8):
    plt.plot(FCUx_s[i], FCUy_s[i], 'k')
for i in range(0, 5):
    plt.plot(FCVx_s[i], FCVy_s[i], 'k')

conP1 = [4.97419, 5.49779, 6.02139]
conP2 = [3.40339, 3.92699, 4.45059]
conP3 = [1.8326, 2.35619, 2.87979]
conP4 = [0.261799, 0.785398, 1.309]
r = 25
ang = np.linspace(0, 2 * np.pi, 50)

for cage in range(0, 4):
    xc = center2[cage][0] + r * np.cos(ang)
    yc = center2[cage][1] + r * np.sin(ang)

    ############# Bridles #############################################

    ############ Bridle 1 to 3 #######################

    for i in range(len(conP1)):
        bx = [buoy_s[3 + 2 * cage][0], center2[cage][0] + r * np.cos(conP1[i])]
        by = [buoy_s[3 + 2 * cage][1], center2[cage][1] - r * np.sin(conP1[i])]
        plt.plot(bx, by, '-k')
        ############ Bridle 4 to 6 #######################
    for i in range(len(conP2)):
        bx = [buoy_s[1 + 2 * cage][0], center2[cage][0] + r * np.cos(conP2[i])]
        by = [buoy_s[1 + 2 * cage][1], center2[cage][1] - r * np.sin(conP2[i])]
        plt.plot(bx, by, '-k')
        ############ Bridle 7 to 9 #######################
    for i in range(len(conP3)):
        bx = [buoy_s[0 + 2 * cage][0], center2[cage][0] + r * np.cos(conP3[i])]
        by = [buoy_s[0 + 2 * cage][1], center2[cage][1] - r * np.sin(conP3[i])]
        plt.plot(bx, by, '-k')
        ############ Bridle 10 to 12 #####################
    for i in range(len(conP1)):
        bx = [buoy_s[2 + 2 * cage][0], center2[cage][0] + r * np.cos(conP4[i])]
        by = [buoy_s[2 + 2 * cage][1], center2[cage][1] - r * np.sin(conP4[i])]
        plt.plot(bx, by, '-k')
    ##########  Floating collar ###########
    plt.plot(xc, yc, linewidth=2, color='k', zorder=1)

    ########### net ###############
    for i in range(-25, 25, 4):
        y = i + center2[cage][1]
        plt.hlines(y, center2[cage][0] - np.sqrt(r ** 2 - (y - center2[cage][1]) ** 2),
                   center2[cage][0] + np.sqrt(r ** 2 - (y - center2[cage][1]) ** 2), colors='k', linestyle='solid')
    for i in range(-25, 25, 4):
        x = i + center2[cage][0]
        plt.vlines(x, center2[cage][1] - np.sqrt(r ** 2 - (x - center2[cage][0]) ** 2),
                   center2[cage][1] + np.sqrt(r ** 2 - (x - center2[cage][0]) ** 2), colors='k', linestyle='solid')

    plt.axis('off')
    plt.axis('equal')
