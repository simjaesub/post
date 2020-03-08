###### Enter Flow direction #########
Deg = '20'
#####################################
###### Enter Failure mode   #########
Fail = 'U2'
#####################################
###### Enter Cage Number    #########
Cage = 1
#####################################

#### Intact 1x4 model
## 0deg: 0-418s [0-836] // 10deg: 0-442s [0-884] // all the other degs: 0-500s [0-1000]
## 0deg: 0-418s [0-836] // 10deg: 0-442s [0-884] // all the other degs: 0-500s [0-1000]
## 0deg: 0-418s [0-836] // 10deg: 0-442s [0-884] // all the other degs: 0-500s [0-1000]
import numpy as np
import pickle
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (6.5, 3.5)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = '10'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"

with open('..\\..\\Results_1x4cages_failure\\' + str(Fail) + '\\cprocessed_Mul1x4Vel0.5Degree' + str(Deg) + '.csv',
          'rb') as handle:
    resu = pickle.load(handle)
with open('..\\..\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree' + str(Deg) + '.csv', 'rb') as handle:
    resu_intact = pickle.load(handle)

Bridles = np.zeros((48, 1))
Bridles_intact = np.zeros((48, 1))
bridlenum = np.arange(12)

for j in range(0, 4):
    for i in bridlenum:
        x = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 0])
        y = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 1])
        z = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 2])
        Bridles[12 * j + i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000
if Deg == '0':
    for j in range(0, 4):
        for i in bridlenum:
            x = np.mean(resu_intact['mooring3']['forceFloater' + str(j) + '_0' + str(i)][820:836, 0])
            y = np.mean(resu_intact['mooring3']['forceFloater' + str(j) + '_0' + str(i)][820:836, 1])
            z = np.mean(resu_intact['mooring3']['forceFloater' + str(j) + '_0' + str(i)][820:836, 2])
            Bridles_intact[12 * j + i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000
if Deg == '10':
    for j in range(0, 4):
        for i in bridlenum:
            x = np.mean(resu_intact['mooring3']['forceFloater' + str(j) + '_0' + str(i)][860:884, 0])
            y = np.mean(resu_intact['mooring3']['forceFloater' + str(j) + '_0' + str(i)][860:884, 1])
            z = np.mean(resu_intact['mooring3']['forceFloater' + str(j) + '_0' + str(i)][860:884, 2])
            Bridles_intact[12 * j + i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000
else:
    for j in range(0, 4):
        for i in bridlenum:
            x = np.mean(resu_intact['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 0])
            y = np.mean(resu_intact['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 1])
            z = np.mean(resu_intact['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 2])
            Bridles_intact[12 * j + i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000
Bridles_initial = [[23.9, 0.2, 29.0, 25.2, 0.3, 32.2, 32.3, 0.3, 25.2, 29.0, 0.2, 23.9],
                   [22.8, 0.2, 22.8, 23.4, 0.2, 21.7, 21.7, 0.2, 23.4, 22.8, 0.2, 22.8],
                   [21.7, 0.2, 23.4, 22.8, 0.2, 22.8, 22.8, 0.2, 22.8, 23.4, 0.2, 21.7],
                   [32.3, 0.3, 25.2, 29.0, 0.2, 23.9, 23.9, 0.2, 29.0, 25.2, 0.3, 32.2]]

gap = Bridles - Bridles_intact
x = np.arange(len(Bridles))
width = 0.5

Cages = [np.arange(0, 12),
         np.arange(12, 24),
         np.arange(24, 36),
         np.arange(36, 48)]

plt.figure()
plt.bar(x[Cages[Cage - 1]], Bridles[Cages[Cage - 1], 0], width, color='seagreen', edgecolor='k')
plt.bar(x[Cages[Cage - 1]], Bridles_initial[Cage - 1], width=0.1, color='k', edgecolor='k', alpha=0.5, zorder=2,
        label='Initial')
plt.legend(frameon=False)
for j in Cages[Cage - 1]:
    if gap[j] >= 0:
        plt.hlines(Bridles[j] - gap[j], x[j] - width / 2, x[j] + width / 2, color='k')
        plt.vlines(x[j], Bridles[j] - gap[j], Bridles[j], color='k')
    else:
        plt.hlines(Bridles[j] - gap[j], x[j] - width / 2, x[j] + width / 2, color='firebrick')
        plt.vlines(x[j], Bridles[j] - gap[j], Bridles[j], color='firebrick')
plt.ylim(0, 150)
xaxis = Cages[Cage - 1]
xaxis_tag = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12']
plt.xticks(xaxis, xaxis_tag, rotation=70)
plt.ylabel('Tension [kN]')
plt.tight_layout()
