##################### mooring lines ##################################
Mooring_lines_s = np.zeros((14, 2))
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
    Mooring_lines_s[i][1] = np.sqrt(Ux_s[i] ** 2 + Uy_s[i] ** 2 + Uz_s[i] ** 2)

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
    Mooring_lines_s[i + 4][1] = np.sqrt(Vx_s[i] ** 2 + Vy_s[i] ** 2 + Vz_s[i] ** 2)

################# Frame cables ######################################
Frame_cables_s = np.zeros((13, 2))
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
    Frame_cables_s[i][1] = np.sqrt(FCUx_s[i] ** 2 + FCUy_s[i] ** 2 + FCUz_s[i] ** 2)
FCVx_s = []
FCVy_s = []
FCVz_s = []
for i in range(0, 10, 2):
    FCVx_s.append(buoy_s[i][0] - buoy_s[i + 1][0])
    FCVy_s.append(buoy_s[i][1] - buoy_s[i + 1][1])
    FCVz_s.append(buoy_s[i][2] - buoy_s[i + 1][2])
for i in range(0, 5):
    Frame_cables_s[i + 8][1] = np.sqrt(FCVx_s[i] ** 2 + FCVy_s[i] ** 2 + FCVz_s[i] ** 2)

conP1 = [4.97419, 5.49779, 6.02139]
conP2 = [3.40339, 3.92699, 4.45059]
conP3 = [1.8326, 2.35619, 2.87979]
conP4 = [0.261799, 0.785398, 1.309]
r = 25
ang = np.linspace(0, 2 * np.pi, 50)

############# Bridles #############################################
Bridles_s = np.zeros((48, 2))
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
    Bridles_s[i][1] = np.sqrt(Bx_s[i] ** 2 + By_s[i] ** 2 + Bz_s[i] ** 2)
