######################################### shifted cage ###################################################3
buoy1_pos2 = resu['mooring3']['platePosition0_0'][250,0:2]
buoy2_pos2 = resu['mooring3']['platePosition0_1'][250,0:2]
buoy3_pos2 = resu['mooring3']['platePosition1_0'][250,0:2]
buoy4_pos2 = resu['mooring3']['platePosition1_1'][250,0:2]




xc2 = center2[0] + r*np.cos(ang)
yc2 = center2[1] + r*np.sin(ang)

##################### mooring lines ##################################
U1x = [anchor_pos[0][0],buoy1_pos2[0]]
U1y = [anchor_pos[0][1],buoy1_pos2[1]]

U2x = [anchor_pos[1][0],buoy2_pos2[0]]
U2y = [anchor_pos[1][1],buoy2_pos2[1]]

U3x = [anchor_pos[2][0],buoy3_pos2[0]]
U3y = [anchor_pos[2][1],buoy3_pos2[1]]

U4x = [anchor_pos[3][0],buoy4_pos2[0]]
U4y = [anchor_pos[3][1],buoy4_pos2[1]]

V1x = [anchor_pos[4][0],buoy1_pos2[0]]
V1y = [anchor_pos[4][1],buoy1_pos2[1]]

V2x = [anchor_pos[5][0],buoy3_pos2[0]]
V2y = [anchor_pos[5][1],buoy3_pos2[1]]

V3x = [anchor_pos[6][0],buoy2_pos2[0]]
V3y = [anchor_pos[6][1],buoy2_pos2[1]]

V4x = [anchor_pos[7][0],buoy4_pos2[0]]
V4y = [anchor_pos[7][1],buoy4_pos2[1]]

################# Frame cables ######################################
FCU1x = [buoy1_pos2[0], buoy3_pos2[0]]
FCU1y = [buoy1_pos2[1], buoy3_pos2[1]]
FCU2x = [buoy2_pos2[0], buoy4_pos2[0]]
FCU2y = [buoy2_pos2[1], buoy4_pos2[1]]
FCV1x = [buoy1_pos2[0], buoy2_pos2[0]]
FCV1y = [buoy1_pos2[1], buoy2_pos2[1]]
FCV2x = [buoy3_pos2[0], buoy4_pos2[0]]
FCV2y = [buoy3_pos2[1], buoy4_pos2[1]]

############# Bridles #############################################
conP1 = [0.261799,0.785398,1.309]

conP2 = [1.8326,2.35619,2.87979]
conP3 = [3.40339,3.92699,4.45059]
conP4 = [4.97419,5.49779,6.02139]
B1x = [center2[0]+r*np.cos(conP1), buoy3_pos2[0]]
B1y = [center2[1]+r*np.sin(conP1), buoy3_pos2[1]]

    ############ Bridle 1 to 3 #######################
for i in range(len(conP1)):
    bx = [buoy3_pos2[0], center2[0] + r*np.cos(conP1[i])]
    by = [buoy3_pos2[1], center2[1] - r*np.sin(conP1[i])]
    plt.plot(bx,by,'-k',alpha = 0.5)
    ############ Bridle 4 to 6 #######################    
for i in range(len(conP2)):
    bx = [buoy1_pos2[0], center2[0] + r*np.cos(conP2[i])]
    by = [buoy1_pos2[1], center2[1] - r*np.sin(conP2[i])]
    plt.plot(bx,by,'-k',alpha = 0.5)
        ############ Bridle 7 to 9 #######################
for i in range(len(conP3)):
    bx = [buoy2_pos2[0], center2[0] + r*np.cos(conP3[i])]
    by = [buoy2_pos2[1], center2[1] - r*np.sin(conP3[i])]
    plt.plot(bx,by,'-k',alpha = 0.5)
        ############ Bridle 10 to 12 #####################
for i in range(len(conP1)):
    bx = [buoy4_pos2[0], center2[0] + r*np.cos(conP4[i])]
    by = [buoy4_pos2[1], center2[1] - r*np.sin(conP4[i])]
    plt.plot(bx,by,'-k',alpha = 0.5)
##########  Floating collar ###########
plt.plot(xc,yc,linewidth =3, color = 'k',alpha = 0.5)


########### net ###############
for i in range(-25, 25, 4):
    y = i+center2[1]
    plt.hlines(y,center2[0]-np.sqrt(r**2 - (y-center2[1])**2),center2[0]+np.sqrt(r**2 - (y-center2[1])**2), colors = 'k' , linestyle = 'solid',alpha = 0.5)
for i in range(-25, 25, 4):
    x = i+center2[0]
    plt.vlines(x,center2[1]-np.sqrt(r**2 - (x-center2[0])**2), center2[1]+np.sqrt(r**2 - (x-center2[0])**2), colors = 'k' , linestyle = 'solid',alpha = 0.5)


########### Mooring lines ############
plt.plot(U1x, U1y,'k',alpha = 0.5)
plt.plot(U2x, U2y,'k',alpha = 0.5)
plt.plot(U3x, U3y,'k',alpha = 0.5)
plt.plot(U4x, U4y,'k',alpha = 0.5)
plt.plot(V1x, V1y,'k',alpha = 0.5)
plt.plot(V2x, V2y,'k',alpha = 0.5)
plt.plot(V3x, V3y,'k',alpha = 0.5)
plt.plot(V4x, V4y,'k',alpha = 0.5)

######### Frame cables #############
plt.plot(FCU1x,FCU1y,'k',alpha = 0.5)
plt.plot(FCU2x,FCU2y,'k',alpha = 0.5)
plt.plot(FCV1x,FCV1y,'k',alpha = 0.5)
plt.plot(FCV2x,FCV2y,'k',alpha = 0.5)
