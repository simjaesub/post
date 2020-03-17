import numpy as np
import pickle

with open('..\\..\\Results_1x4cages_intact_c\\cprocessed_Mul1x4Vel0.5Degree20.csv', 'rb') as handle:
    resu = pickle.load(handle)

with open('..\\1x4_cages\\processed_resu1x4_noloading.csv', 'rb') as handle:
    resui = pickle.load(handle)

Pos = []
Posi = []

for i in range(0, 5):
    for j in range(0, 2):
        Pos = np.append(Pos, resu['mooring3']['platePosition' + str(i) + '_' + str(j)][1000, :])

for i in range(0, 5):
    for j in range(0, 2):
        Posi = np.append(Posi, resui['mooring3']['platePosition' + str(i) + '_' + str(j)][1000, :])

posb = np.reshape(Pos, newshape=(10, 3))
posbi = np.reshape(Posi, newshape=(10, 3))
