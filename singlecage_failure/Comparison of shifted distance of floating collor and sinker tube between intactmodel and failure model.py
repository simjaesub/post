import numpy as np
import pickle

# with open('..\\..\\Results_singlecage_intact_d\\dprocessed_Mul1x1Vel0.5Degree0.csv', 'rb') as handle:
#     resui = pickle.load(handle)
# with open('..\\..\\Results_singlecage_failure\\U1_fail\\dprocessed_Mul1x1Vel0.5Degree0_U1_fail.csv', 'rb') as handle:
#     resuf = pickle.load(handle)

pos_intact = np.array([])
pos_fail = np.array([])

theta = np.arange(0, 100, 10)
for i in theta:
    with open('..\\..\\Results_singlecage_intact_d\\dprocessed_Mul1x1Vel0.5Degree' + str(i) + '.csv', 'rb') as handle:
        resui = pickle.load(handle)
    pos_intact = np.append(pos_intact, [np.mean(resui['collar0']['FloaterCenterPos'][240:250, 0]),
                                        np.mean(resui['collar0']['FloaterCenterPos'][240:250, 1]),
                                        np.mean(resui['collar0']['FloaterCenterPos'][240:250, 2])])
colloar_i = np.reshape(pos_intact, (10, 3))

fail = ['U1', 'U2', 'U3', 'U4', 'V1', 'V2', 'V3', 'V4', 'FCU1', 'FCU2', 'FCV1',
        'FCV2']
shifted_distance = np.zeros((10, 12))

for deg in theta:
    for i in fail:
        with open('..\\..\\Results_singlecage_failure\\' + str(i) + '_fail\\dprocessed_Mul1x1Vel0.5Degree' + str(
                deg) + '_' + str(i) + '_fail.csv', 'rb') as handle:
            resuf = pickle.load(handle)

        pos_fail = np.append(pos_fail, [np.mean(resuf['collar0']['FloaterCenterPos'][900:1000, 0]),
                                        np.mean(resuf['collar0']['FloaterCenterPos'][900:1000, 1]),
                                        np.mean(resuf['collar0']['FloaterCenterPos'][900:1000, 2])])
    collar_f = np.reshape(pos_fail, (12, 3))

    for j in range(0, 12):
        x = collar_f[j][0] - colloar_i[int(deg / 10)][0]
        y = collar_f[j][1] - colloar_i[int(deg / 10)][1]
        z = collar_f[j][2] - colloar_i[int(deg / 10)][2]
        shifted_distance[int(deg / 10)][j] = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    pos_fail = np.array([])
