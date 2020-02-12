# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:31:44 2020

@author: shuer
"""

import pickle
######## intact model ########################
# with open('..\\Results_singlecage_intact_d\\dprocessed_Mul1x1Vel0.5Degree0.csv', 'rb') as handle:
#     resu = pickle.load(handle)
 ######## failed model ########################   
with open('..\\Results_singlecage_failure\\U1_fail\\dprocessed_Mul1x1Vel0.5Degree0_U1_fail.csv', 'rb') as handle:
    resu = pickle.load(handle)

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (4, 4)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = '10'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"

cp = resu['collar0']['FloaterCenterPos'][0,0:2]
center = np.array(cp).tolist()

cp2 = resu['collar0']['FloaterCenterPos'][250,0:2]
center2 = np.array(cp2).tolist()

buoy1_pos = resu['mooring3']['platePosition0_0'][0,0:2]
buoy2_pos = resu['mooring3']['platePosition0_1'][0,0:2]
buoy3_pos = resu['mooring3']['platePosition1_0'][0,0:2]
buoy4_pos = resu['mooring3']['platePosition1_1'][0,0:2]
anchor_pos = [[-150,-50],
              [-150, 50],
              [ 150,-50],
              [ 150, 50],
              [-50,-150],
              [ 50,-150],
              [-50, 150],
              [ 50, 150]]


r = 25
ang = np.linspace(0,2*np.pi,50)
xc = center[0] + r*np.cos(ang)
yc = center[1] + r*np.sin(ang)


plt.figure()
plt.gca().invert_yaxis()
##################### mooring lines ##################################
U1x = [anchor_pos[0][0],buoy1_pos[0]]
U1y = [anchor_pos[0][1],buoy1_pos[1]]

U2x = [anchor_pos[1][0],buoy2_pos[0]]
U2y = [anchor_pos[1][1],buoy2_pos[1]]

U3x = [anchor_pos[2][0],buoy3_pos[0]]
U3y = [anchor_pos[2][1],buoy3_pos[1]]

U4x = [anchor_pos[3][0],buoy4_pos[0]]
U4y = [anchor_pos[3][1],buoy4_pos[1]]

V1x = [anchor_pos[4][0],buoy1_pos[0]]
V1y = [anchor_pos[4][1],buoy1_pos[1]]

V2x = [anchor_pos[5][0],buoy3_pos[0]]
V2y = [anchor_pos[5][1],buoy3_pos[1]]

V3x = [anchor_pos[6][0],buoy2_pos[0]]
V3y = [anchor_pos[6][1],buoy2_pos[1]]

V4x = [anchor_pos[7][0],buoy4_pos[0]]
V4y = [anchor_pos[7][1],buoy4_pos[1]]

################# Frame cables ######################################
FCU1x = [buoy1_pos[0], buoy3_pos[0]]
FCU1y = [buoy1_pos[1], buoy3_pos[1]]
FCU2x = [buoy2_pos[0], buoy4_pos[0]]
FCU2y = [buoy2_pos[1], buoy4_pos[1]]
FCV1x = [buoy1_pos[0], buoy2_pos[0]]
FCV1y = [buoy1_pos[1], buoy2_pos[1]]
FCV2x = [buoy3_pos[0], buoy4_pos[0]]
FCV2y = [buoy3_pos[1], buoy4_pos[1]]

############# Bridles #############################################
conP1 = [0.261799,0.785398,1.309]
conP2 = [1.8326,2.35619,2.87979]
conP3 = [3.40339,3.92699,4.45059]
conP4 = [4.97419,5.49779,6.02139]
B1x = [center[0]+r*np.cos(conP1), buoy3_pos[0]]
B1y = [center[1]+r*np.sin(conP1), buoy3_pos[1]]

    ############ Bridle 1 to 3 #######################
for i in range(len(conP1)):
    bx = [buoy3_pos[0], center[0] + r*np.cos(conP1[i])]
    by = [buoy3_pos[1], center[1] - r*np.sin(conP1[i])]
    plt.plot(bx,by,'-k')
    ############ Bridle 4 to 6 #######################    
for i in range(len(conP2)):
    bx = [buoy1_pos[0], center[0] + r*np.cos(conP2[i])]
    by = [buoy1_pos[1], center[1] - r*np.sin(conP2[i])]
    plt.plot(bx,by,'-k')
        ############ Bridle 7 to 9 #######################
for i in range(len(conP3)):
    bx = [buoy2_pos[0], center[0] + r*np.cos(conP3[i])]
    by = [buoy2_pos[1], center[1] - r*np.sin(conP3[i])]
    plt.plot(bx,by,'-k')
        ############ Bridle 10 to 12 #####################
for i in range(len(conP1)):
    bx = [buoy4_pos[0], center[0] + r*np.cos(conP4[i])]
    by = [buoy4_pos[1], center[1] - r*np.sin(conP4[i])]
    plt.plot(bx,by,'-k')
##########  Floating collar ###########
plt.plot(xc,yc,linewidth =2, color = 'k', zorder =1)


########### net ###############
for i in range(-25, 25, 4):
    y = i+center[1]
    plt.hlines(y,center[0]-np.sqrt(r**2 - (y-center[1])**2),center[0]+np.sqrt(r**2 - (y-center[1])**2), colors = 'k' , linestyle = 'solid')
for i in range(-25, 25, 4):
    x = i+center[0]
    plt.vlines(x,center[1]-np.sqrt(r**2 - (x-center[0])**2), center[1]+np.sqrt(r**2 - (x-center[0])**2), colors = 'k' , linestyle = 'solid')


########### Mooring lines ############
plt.plot(U1x, U1y,'k')
plt.plot(U2x, U2y,'k')
plt.plot(U3x, U3y,'k')
plt.plot(U4x, U4y,'k')
plt.plot(V1x, V1y,'k')
plt.plot(V2x, V2y,'k')
plt.plot(V3x, V3y,'k')
plt.plot(V4x, V4y,'k')

######### Frame cables #############
plt.plot(FCU1x,FCU1y,'k')
plt.plot(FCU2x,FCU2y,'k')
plt.plot(FCV1x,FCV1y,'k')
plt.plot(FCV2x,FCV2y,'k')

plt.axis('off')




######################################### shifted cage ###################################################3
buoy1_pos2 = resu['mooring3']['platePosition0_0'][1000,0:2]
buoy2_pos2 = resu['mooring3']['platePosition0_1'][1000,0:2]
buoy3_pos2 = resu['mooring3']['platePosition1_0'][1000,0:2]
buoy4_pos2 = resu['mooring3']['platePosition1_1'][1000,0:2]




xc2 = center2[0] + r*np.cos(ang)
yc2 = center2[1] + r*np.sin(ang)

##################### mooring lines ##################################
sU1x = [anchor_pos[0][0],buoy1_pos2[0]]
sU1y = [anchor_pos[0][1],buoy1_pos2[1]]

sU2x = [anchor_pos[1][0],buoy2_pos2[0]]
sU2y = [anchor_pos[1][1],buoy2_pos2[1]]

sU3x = [anchor_pos[2][0],buoy3_pos2[0]]
sU3y = [anchor_pos[2][1],buoy3_pos2[1]]

sU4x = [anchor_pos[3][0],buoy4_pos2[0]]
sU4y = [anchor_pos[3][1],buoy4_pos2[1]]

sV1x = [anchor_pos[4][0],buoy1_pos2[0]]
sV1y = [anchor_pos[4][1],buoy1_pos2[1]]

sV2x = [anchor_pos[5][0],buoy3_pos2[0]]
sV2y = [anchor_pos[5][1],buoy3_pos2[1]]

sV3x = [anchor_pos[6][0],buoy2_pos2[0]]
sV3y = [anchor_pos[6][1],buoy2_pos2[1]]

sV4x = [anchor_pos[7][0],buoy4_pos2[0]]
sV4y = [anchor_pos[7][1],buoy4_pos2[1]]

################# Frame cables ######################################
sFCU1x = [buoy1_pos2[0], buoy3_pos2[0]]
sFCU1y = [buoy1_pos2[1], buoy3_pos2[1]]
sFCU2x = [buoy2_pos2[0], buoy4_pos2[0]]
sFCU2y = [buoy2_pos2[1], buoy4_pos2[1]]
sFCV1x = [buoy1_pos2[0], buoy2_pos2[0]]
sFCV1y = [buoy1_pos2[1], buoy2_pos2[1]]
sFCV2x = [buoy3_pos2[0], buoy4_pos2[0]]
sFCV2y = [buoy3_pos2[1], buoy4_pos2[1]]

############# Bridles #############################################



    ############ Bridle 1 to 3 #######################
for i in range(len(conP1)):
    bx = [buoy3_pos2[0], center2[0] + r*np.cos(conP1[i])]
    by = [buoy3_pos2[1], center2[1] - r*np.sin(conP1[i])]
    plt.plot(bx,by, color = 'firebrick',alpha = 0.5)
    ############ Bridle 4 to 6 #######################    
for i in range(len(conP2)):
    bx = [buoy1_pos2[0], center2[0] + r*np.cos(conP2[i])]
    by = [buoy1_pos2[1], center2[1] - r*np.sin(conP2[i])]
    plt.plot(bx,by,color = 'firebrick',alpha = 0.5)
        ############ Bridle 7 to 9 #######################
for i in range(len(conP3)):
    bx = [buoy2_pos2[0], center2[0] + r*np.cos(conP3[i])]
    by = [buoy2_pos2[1], center2[1] - r*np.sin(conP3[i])]
    plt.plot(bx,by,color = 'firebrick',alpha = 0.5)
        ############ Bridle 10 to 12 #####################
for i in range(len(conP1)):
    bx = [buoy4_pos2[0], center2[0] + r*np.cos(conP4[i])]
    by = [buoy4_pos2[1], center2[1] - r*np.sin(conP4[i])]
    plt.plot(bx,by,color = 'firebrick',alpha = 0.5)
##########  Floating collar ###########
plt.plot(xc2,yc2,linewidth = 2, color = 'firebrick',alpha = 0.5, zorder =2)


########### net ###############
for i in range(-25, 25, 4):
    y = i+center2[1]
    plt.hlines(y,center2[0]-np.sqrt(r**2 - (y-center2[1])**2),center2[0]+np.sqrt(r**2 - (y-center2[1])**2), colors = 'firebrick' , linestyle = 'solid',alpha = 0.5)
for i in range(-25, 25, 4):
    x = i+center2[0]
    plt.vlines(x,center2[1]-np.sqrt(r**2 - (x-center2[0])**2), center2[1]+np.sqrt(r**2 - (x-center2[0])**2), colors = 'firebrick' , linestyle = 'solid',alpha = 0.5)


########### Mooring lines ############
# plt.plot(sU1x, sU1y,'firebrick',alpha = 0.5)
plt.plot(sU2x, sU2y,'firebrick',alpha = 0.5)
plt.plot(sU3x, sU3y,'firebrick',alpha = 0.5)
plt.plot(sU4x, sU4y,'firebrick',alpha = 0.5)
plt.plot(sV1x, sV1y,'firebrick',alpha = 0.5)
plt.plot(sV2x, sV2y,'firebrick',alpha = 0.5)
plt.plot(sV3x, sV3y,'firebrick',alpha = 0.5)
plt.plot(sV4x, sV4y,'firebrick',alpha = 0.5)

######### Frame cables #############
plt.plot(sFCU1x,sFCU1y,'firebrick',alpha = 0.5)
plt.plot(sFCU2x,sFCU2y,'firebrick',alpha = 0.5)
plt.plot(sFCV1x,sFCV1y,'firebrick',alpha = 0.5)
plt.plot(sFCV2x,sFCV2y,'firebrick',alpha = 0.5)

# plt.text(-100,51,'U1', color = 'firebrick', weight='bold')
# plt.text(-100,-49,'U2', color = 'firebrick', weight='bold')
# plt.text( 100,51,'U3', color = 'firebrick', weight='bold')
# plt.text(100,-49,'U4', color = 'firebrick', weight='bold')

# plt.text(-49,100,'V1', color = 'firebrick', weight='bold')
# plt.text(51,100,'V2', color = 'firebrick', weight='bold')
# plt.text(-49,-100,'V3', color = 'firebrick', weight='bold')
# plt.text(51,-100,'V4', color = 'firebrick', weight='bold')

# plt.text(-10,51,'FCU1', color = 'firebrick', weight='bold')
# plt.text(-10,-49,'FCU2', color = 'firebrick', weight='bold')
# plt.text(-75,0,'FCV1', color = 'firebrick', weight='bold')
# plt.text(51,0,'FCV2', color = 'firebrick', weight='bold')


plt.tight_layout()
plt.savefig('cage_shift.png', dpi=600)

############################# lengths - Initial #################################

Len_U1 = np.sqrt((U1x[0]-U1x[1])**2 +(U1y[0]-U1y[1])**2)
Len_U2 = np.sqrt((U2x[0]-U2x[1])**2 +(U2y[0]-U2y[1])**2)
Len_U3 = np.sqrt((U3x[0]-U3x[1])**2 +(U3y[0]-U3y[1])**2)
Len_U4 = np.sqrt((U4x[0]-U4x[1])**2 +(U4y[0]-U4y[1])**2)

Len_V1 = np.sqrt((V1x[0]-V1x[1])**2 +(V1y[0]-V1y[1])**2)
Len_V2 = np.sqrt((V2x[0]-V2x[1])**2 +(V2y[0]-V2y[1])**2)
Len_V3 = np.sqrt((V3x[0]-V3x[1])**2 +(V3y[0]-V3y[1])**2)
Len_V4 = np.sqrt((V4x[0]-V4x[1])**2 +(V4y[0]-V4y[1])**2)

Len_FCU1 = np.sqrt((FCU1x[0]-FCU1x[1])**2 + (FCU1y[0]-FCU1y[1])**2 )
Len_FCU2 = np.sqrt((FCU2x[0]-FCU2x[1])**2 + (FCU2y[0]-FCU2y[1])**2 )
Len_FCV1 = np.sqrt((FCV1x[0]-FCV1x[1])**2 + (FCV1y[0]-FCV1y[1])**2 )
Len_FCV2 = np.sqrt((FCV2x[0]-FCV2x[1])**2 + (FCV2y[0]-FCV2y[1])**2 )


############################# lengths - after loading #################################

Len_sU1 = np.sqrt((sU1x[0]-sU1x[1])**2 +(sU1y[0]-sU1y[1])**2)
Len_sU2 = np.sqrt((sU2x[0]-sU2x[1])**2 +(sU2y[0]-sU2y[1])**2)
Len_sU3 = np.sqrt((sU3x[0]-sU3x[1])**2 +(sU3y[0]-sU3y[1])**2)
Len_sU4 = np.sqrt((sU4x[0]-sU4x[1])**2 +(sU4y[0]-sU4y[1])**2)

Len_sV1 = np.sqrt((sV1x[0]-sV1x[1])**2 +(sV1y[0]-sV1y[1])**2)
Len_sV2 = np.sqrt((sV2x[0]-sV2x[1])**2 +(sV2y[0]-sV2y[1])**2)
Len_sV3 = np.sqrt((sV3x[0]-sV3x[1])**2 +(sV3y[0]-sV3y[1])**2)
Len_sV4 = np.sqrt((sV4x[0]-sV4x[1])**2 +(sV4y[0]-sV4y[1])**2)

Len_sFCU1 = np.sqrt((sFCU1x[0]-sFCU1x[1])**2 + (sFCU1y[0]-sFCU1y[1])**2 )
Len_sFCU2 = np.sqrt((sFCU2x[0]-sFCU2x[1])**2 + (sFCU2y[0]-sFCU2y[1])**2 )
Len_sFCV1 = np.sqrt((sFCV1x[0]-sFCV1x[1])**2 + (sFCV1y[0]-sFCV1y[1])**2 )
Len_sFCV2 = np.sqrt((sFCV2x[0]-sFCV2x[1])**2 + (sFCV2y[0]-sFCV2y[1])**2 )

