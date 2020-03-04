import numpy as np
import pickle

with open('..\\..\\Results_singlecage_intact_d\\dprocessed_Mul1x1Vel0.5Degree0.csv', 'rb') as handle:
    resu = pickle.load(handle)

with open('..\\..\\Results_singlecage_intact_d\\Processed_Initial_condition_vel05_singlecage.csv', 'rb') as handle:
    resui = pickle.load(handle)

anchors = [[-150, -50, 80],
           [-150, 50, 80],
           [150, -50, 80],
           [150, 50, 80],
           [-50, -150, 80],
           [50, -150, 80],
           [-50, 150, 80],
           [50, 150, 80]]

Steelplate = [resu['mooring3']['platePosition0_0'][250, :],
              resu['mooring3']['platePosition0_1'][250, :],
              resu['mooring3']['platePosition1_0'][250, :],
              resu['mooring3']['platePosition1_1'][250, :]]
Steelplate_V = [resu['mooring3']['platePosition0_0'][250, :],
                resu['mooring3']['platePosition1_0'][250, :],
                resu['mooring3']['platePosition0_1'][250, :],
                resu['mooring3']['platePosition1_1'][250, :]]
Steelplate_i = [resui['mooring3']['platePosition0_0'][1000, :],
                resui['mooring3']['platePosition0_1'][1000, :],
                resui['mooring3']['platePosition1_0'][1000, :],
                resui['mooring3']['platePosition1_1'][1000, :]]
Steelplate_i_V = [resui['mooring3']['platePosition0_0'][1000, :],
                  resui['mooring3']['platePosition1_0'][1000, :],
                  resui['mooring3']['platePosition0_1'][1000, :],
                  resui['mooring3']['platePosition1_1'][1000, :]]
Lens = np.ones((12, 2))

## Cable lengths for the single cage under loading
U_lens = np.zeros((4, 1))
for i in range(0, 4):
    x = anchors[i][0] - Steelplate[i][0]
    y = anchors[i][1] - Steelplate[i][1]
    z = anchors[i][2] - Steelplate[i][2]
    U_lens[i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2)

V_lens = np.zeros((4, 1))
for i in range(0, 4):
    x = anchors[len(U_lens) + i][0] - Steelplate_V[i][0]
    y = anchors[len(U_lens) + i][1] - Steelplate_V[i][1]
    z = anchors[len(U_lens) + i][2] - Steelplate_V[i][2]
    V_lens[i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2)

fc_lens = np.zeros((4, 1))
x_fcu1 = Steelplate[0][0] - Steelplate[2][0]
y_fcu1 = Steelplate[0][1] - Steelplate[2][1]
z_fcu1 = Steelplate[0][2] - Steelplate[2][2]
fc_lens[0][0] = np.sqrt(x_fcu1 ** 2 + y_fcu1 ** 2 + z_fcu1 ** 2)

x_fcu2 = Steelplate[1][0] - Steelplate[3][0]
y_fcu2 = Steelplate[1][1] - Steelplate[3][1]
z_fcu2 = Steelplate[1][2] - Steelplate[3][2]
fc_lens[1][0] = np.sqrt(x_fcu1 ** 2 + y_fcu1 ** 2 + z_fcu1 ** 2)

x_fcv1 = Steelplate[0][0] - Steelplate[1][0]
y_fcv1 = Steelplate[0][1] - Steelplate[1][1]
z_fcv1 = Steelplate[0][2] - Steelplate[1][2]
fc_lens[2][0] = np.sqrt(x_fcu1 ** 2 + y_fcu1 ** 2 + z_fcu1 ** 2)

x_fcv2 = Steelplate[2][0] - Steelplate[3][0]
y_fcv2 = Steelplate[2][1] - Steelplate[3][1]
z_fcv2 = Steelplate[2][2] - Steelplate[3][2]
fc_lens[3][0] = np.sqrt(x_fcu1 ** 2 + y_fcu1 ** 2 + z_fcu1 ** 2)

## Cable lengths for the single cage without loading
U_lens_i = np.zeros((4, 1))
for i in range(0, 4):
    x = anchors[i][0] - Steelplate_i[i][0]
    y = anchors[i][1] - Steelplate_i[i][1]
    z = anchors[i][2] - Steelplate_i[i][2]
    U_lens_i[i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2)

V_lens_i = np.zeros((4, 1))
for i in range(0, 4):
    x = anchors[len(U_lens_i) + i][0] - Steelplate_i_V[i][0]
    y = anchors[len(U_lens_i) + i][1] - Steelplate_i_V[i][1]
    z = anchors[len(U_lens_i) + i][2] - Steelplate_i_V[i][2]
    V_lens_i[i][0] = np.sqrt(x ** 2 + y ** 2 + z ** 2)

fc_lens_i = np.zeros((4, 1))
x_fcu1 = Steelplate_i[0][0] - Steelplate_i[2][0]
y_fcu1 = Steelplate_i[0][1] - Steelplate_i[2][1]
z_fcu1 = Steelplate_i[0][2] - Steelplate_i[2][2]
fc_lens_i[0][0] = np.sqrt(x_fcu1 ** 2 + y_fcu1 ** 2 + z_fcu1 ** 2)

x_fcu2 = Steelplate_i[1][0] - Steelplate_i[3][0]
y_fcu2 = Steelplate_i[1][1] - Steelplate_i[3][1]
z_fcu2 = Steelplate_i[1][2] - Steelplate_i[3][2]
fc_lens_i[1][0] = np.sqrt(x_fcu1 ** 2 + y_fcu1 ** 2 + z_fcu1 ** 2)

x_fcv1 = Steelplate_i[0][0] - Steelplate_i[1][0]
y_fcv1 = Steelplate_i[0][1] - Steelplate_i[1][1]
z_fcv1 = Steelplate_i[0][2] - Steelplate_i[1][2]
fc_lens_i[2][0] = np.sqrt(x_fcu1 ** 2 + y_fcu1 ** 2 + z_fcu1 ** 2)

x_fcv2 = Steelplate[2][0] - Steelplate[3][0]
y_fcv2 = Steelplate[2][1] - Steelplate[3][1]
z_fcv2 = Steelplate[2][2] - Steelplate[3][2]
fc_lens_i[3][0] = np.sqrt(x_fcu1 ** 2 + y_fcu1 ** 2 + z_fcu1 ** 2)

############################
for i in range(len(U_lens)):
    Lens[i][0] = U_lens[i]
for i in range(len(V_lens)):
    Lens[len(U_lens) + i][0] = V_lens[i]
for i in range(len(fc_lens)):
    Lens[len(U_lens) + len(V_lens) + i][0] = fc_lens[i]

for i in range(len(U_lens_i)):
    Lens[i][1] = U_lens_i[i]
for i in range(len(V_lens_i)):
    Lens[len(U_lens_i) + i][1] = V_lens_i[i]
for i in range(len(fc_lens_i)):
    Lens[len(U_lens_i) + len(V_lens_i) + i][1] = fc_lens_i[i]

import pandas as pd

## convert your array into a dataframe
df = pd.DataFrame(Lens)

## save to xlsx file
filepath = 'Length_cables_2.xlsx'
df.to_excel(filepath, index=False)
