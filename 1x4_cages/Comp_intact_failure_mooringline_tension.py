##### Enter failed cable
Fail = 'V3'
########################

##### Enter Flow direction
Deg = '90'
########################


import pickle
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (6.3, 3)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = 10
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"

anchors = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10']
anchors2 = ['U0_0_ForceA', 'U1_0_ForceA', 'U0_6_ForceB', 'U1_6_ForceB', 'V0_0_ForceA', 'V1_0_ForceA',
            'V2_0_ForceA', 'V3_0_ForceA', 'V4_0_ForceA', 'V0_3_ForceB', 'V1_3_ForceB', 'V2_3_ForceB',
            'V3_3_ForceB', 'V4_3_ForceB']
fcables = ['FCU1', 'FCU2', 'FCU3', 'FCU4', 'FCU5', 'FCU6', 'FCU7', 'FCU8', 'FCV1', 'FCV2', 'FCV3', 'FCV4', 'FCV5']
fcables2 = ['U0_1_ForceA', 'U0_2_ForceA', 'U0_3_ForceA', 'U0_4_ForceA', 'U1_1_ForceA', 'U1_2_ForceA', 'U1_3_ForceA',
            'U1_4_ForceA', 'V0_1_ForceA', 'V1_1_ForceA', 'V2_1_ForceA', 'V3_1_ForceA', 'V4_1_ForceA']
fmodes = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
          'FCU1', 'FCU2', 'FCU3', 'FCU4', 'FCU5', 'FCU6', 'FCU7', 'FCU8', 'FCV1', 'FCV2', 'FCV3', 'FCV4', 'FCV5']

####### Initial condition without any external load############
# with open('processed_resu1x4_noloading.csv', 'rb') as handle:
#     resui = pickle.load(handle)
######## intact model ########################
with open('..\\..\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree' + str(Deg) + '.csv', 'rb') as handle:
    resui = pickle.load(handle)
######## failed model ########################
with open('..\\..\\Results_1x4cages_failure\\' + str(Fail) + '\\cprocessed_Mul1x4Vel0.5Degree' + str(Deg) + '.csv',
          'rb') as handle:
    resu = pickle.load(handle)

# Failulre mode - Mooring line and frame cable tension
anchorF_fail = np.zeros((14, 1))
for i in anchors2:
    xf = np.mean(resu['mooring3']['frameCable' + i][980:1000, 0])
    yf = np.mean(resu['mooring3']['frameCable' + i][980:1000, 1])
    zf = np.mean(resu['mooring3']['frameCable' + i][980:1000, 2])
    anchorF_fail[anchors2.index(i)][0] = np.sqrt(xf ** 2 + yf ** 2 + zf ** 2) / 1000
fcableT_fail = np.zeros((13, 1))
for i in fcables2:
    x1 = np.mean(resu['mooring3']['frameCable' + i][240:250, 0])
    y1 = np.mean(resu['mooring3']['frameCable' + i][240:250, 1])
    z1 = np.mean(resu['mooring3']['frameCable' + i][240:250, 2])
    fcableT_fail[fcables2.index(i)][0] = np.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2) / 1000

# Failulre mode - Mooring line and frame cable tension
anchorF_i = np.zeros((14, 1))
for i in anchors2:
    xf = np.mean(resui['mooring3']['frameCable' + i][980:1000, 0])
    yf = np.mean(resui['mooring3']['frameCable' + i][980:1000, 1])
    zf = np.mean(resui['mooring3']['frameCable' + i][980:1000, 2])
    anchorF_i[anchors2.index(i)][0] = np.sqrt(xf ** 2 + yf ** 2 + zf ** 2) / 1000
fcableT_i = np.zeros((13, 1))
for i in fcables2:
    x1 = np.mean(resui['mooring3']['frameCable' + i][240:250, 0])
    y1 = np.mean(resui['mooring3']['frameCable' + i][240:250, 1])
    z1 = np.mean(resui['mooring3']['frameCable' + i][240:250, 2])
    fcableT_i[fcables2.index(i)][0] = np.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2) / 1000

Tension_f = np.zeros((28, 1))
Tension_i = np.zeros((28, 1))

for i in range(len(anchorF_fail)):
    Tension_f[i][0] = anchorF_fail[i][0]

for i in range(len(fcableT_fail)):
    Tension_f[len(anchorF_fail) + 1 + i][0] = fcableT_fail[i][0]

for i in range(len(anchorF_i)):
    Tension_i[i][0] = anchorF_i[i][0]

for i in range(len(fcableT_i)):
    Tension_i[len(anchorF_i) + 1 + i][0] = fcableT_i[i][0]

gap = np.zeros((28, 1))
gap = Tension_f - Tension_i
x = np.arange(len(Tension_f))
width = 0.5

plt.figure()
plt.bar(x[0:14], Tension_f[0:14, 0], width, color='teal', edgecolor='k', zorder=1)
plt.bar(x[15:28], Tension_f[15:28, 0], width, color='darkred', edgecolor='k', zorder=1)

for j in range(len(Tension_f)):
    if gap[j] >= 0:
        plt.hlines(Tension_f[j] - gap[j], x[j] - width / 2, x[j] + width / 2, color='k')
        plt.vlines(x[j], Tension_f[j] - gap[j], Tension_f[j], color='k')
    else:
        plt.hlines(Tension_f[j] - gap[j], x[j] - width / 2, x[j] + width / 2, color='firebrick')
        plt.vlines(x[j], Tension_f[j] - gap[j], Tension_f[j], color='firebrick')

xaxis = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7',
         'V8', 'V9', 'V10', '  ', 'FCU1', 'FCU2', 'FCU3', 'FCU4', 'FCU5', 'FCU6',
         'FCU7', 'FCU8', 'FCV1', 'FCV2', 'FCV3', 'FCV4', 'FCV5']
yaxis = np.arange(0, 300, 50)
plt.xticks(np.arange(len(Tension_f)), xaxis, rotation=70)
plt.yticks(yaxis)
plt.ylim(0, 250)
plt.ylabel('Tension [kN]')
plt.vlines(14, 0, 250, color='k', linestyle='--')
plt.text(4, 200, 'Mooring lines')
plt.text(19, 200, 'Frame cables')
plt.tight_layout()
plt.savefig('Comp_intact_failure_mooringlines_fc_tensions(' + str(Fail) + 'fail_' + str(Deg) + 'deg).png', dpi=600)
