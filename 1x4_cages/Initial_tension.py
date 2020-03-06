import numpy as np
import pickle

with open('processed_resu1x4_noloading.csv', 'rb') as handle:
    resu = pickle.load(handle)

key_moor = ['U0_0_ForceA', 'U1_0_ForceA', 'U0_6_ForceB', 'U1_6_ForceB',
            'V0_0_ForceA', 'V1_0_ForceA', 'V2_0_ForceA', 'V3_0_ForceA',
            'V4_0_ForceA', 'V0_3_ForceB', 'V1_3_ForceB', 'V2_3_ForceB',
            'V3_3_ForceB', 'V4_3_ForceB']
key_FC = ['U0_1_ForceA', 'U0_2_ForceA', 'U0_3_ForceA', 'U0_4_ForceA',
          'U1_1_ForceA', 'U1_2_ForceA', 'U1_3_ForceA', 'U1_4_ForceA',
          'V0_1_ForceA', 'V1_1_ForceA', 'V2_1_ForceA', 'V3_1_ForceA',
          'V4_1_ForceA']
all_cables = np.ones((1, 77))

# mooring lines
mooringline = np.zeros((1, 14))
for i in key_moor:
    x = np.mean(resu['mooring3']['frameCable' + i][980:1000, 0])
    y = np.mean(resu['mooring3']['frameCable' + i][980:1000, 1])
    z = np.mean(resu['mooring3']['frameCable' + i][980:1000, 2])
    mooringline[0][key_moor.index(i)] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000

# frame cables
framecable = np.zeros((1, 13))
for i in key_FC:
    x1 = np.mean(resu['mooring3']['frameCable' + i][980:1000, 0])
    y1 = np.mean(resu['mooring3']['frameCable' + i][980:1000, 1])
    z1 = np.mean(resu['mooring3']['frameCable' + i][980:1000, 2])
    framecable[0][key_FC.index(i)] = np.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2) / 1000
# bridles

bridlenum = np.arange(12)
bridles = np.zeros((48, 1))
for j in range(0, 4):
    for i in bridlenum:
        x = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 0])
        y = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 1])
        z = np.mean(resu['mooring3']['forceFloater' + str(j) + '_0' + str(i)][980:1000, 2])
        bridles[12 * j + i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2) / 1000

# combine the arrays into all_cables array
# column 0 - 13 - mooring lines
for i in range(len(key_moor)):
    all_cables[0][i] = mooringline[0][i]
# column 15 - 27 - frame cables
for i in range(len(key_FC)):
    all_cables[0][len(key_moor) + 1 + i] = framecable[0][i]
# column 29 - 76 bridles
for i in range(len(bridles)):
    all_cables[0][len(key_moor) + 1 + len(key_FC) + 1 + i] = bridles[i][0]

import pandas as pd

tensions = pd.DataFrame(all_cables)

tensions.to_excel('Initial_Tensions.xlsx')
