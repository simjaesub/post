# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:56:11 2020

@author: shuer
"""

import Fun_read as fr
import numpy as np
resu1 = fr.readresu('testforVol_c2c_05vel_0deg.csv')

import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (6.3,3.0)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.weight'] = 'regular'
plt.rcParams['font.size'] = '10'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"

EstVol_alldeg_c2c = np.zeros((1,8))
for i in range(0,8):
    EstVol_alldeg_c2c[0][i] = np.mean(resu1['NetStructure'+str(i)]['VolumeEst'][950:1000])

import pickle
with open('C:\\Users\\shuer\\OneDrive - Universitetet i Stavanger\\Fhsim_wake\\bin\\Results_only_shielding_on\\postprocessing\\Net_volume_vel05_alldeg_onlyshieldingon.csv', 'rb') as handle:
    EstVol_alldeg_c2c_2 = pickle.load(handle)

deg = np.arange(0,100,10)
xaxis = np.arange(0,100,10)
yaxis = np.arange(0,250,50)

cols = [ 'firebrick' , 'slategray' , 'mediumpurple' , 'mediumturquoise' , 'forestgreen' , 'cornflowerblue' , 'goldenrod' , 'tomato' ]
stys = [ '--' , ':' , '-.' , '--' , '--' , ':' , '-.' , '--' ]
mark = ['*', '^' , 'D' , 'x' , 'o' , '^' , 's' , 'p']


x_c2c_0deg_allcages = np.arange(0.75,4.75,0.5)
volumes_0deg_allcages_c2c = [EstVol_alldeg_c2c[0][0], EstVol_alldeg_c2c[0][1], EstVol_alldeg_c2c[0][2], EstVol_alldeg_c2c[0][3],
                             EstVol_alldeg_c2c[0][4], EstVol_alldeg_c2c[0][5], EstVol_alldeg_c2c[0][6], EstVol_alldeg_c2c[0][7]]

volumes_0deg_allcages_c2c_2 = [EstVol_alldeg_c2c_2[0][0], EstVol_alldeg_c2c_2[0][1], EstVol_alldeg_c2c_2[0][2], EstVol_alldeg_c2c_2[0][3],
                               EstVol_alldeg_c2c_2[0][4], EstVol_alldeg_c2c_2[0][5], EstVol_alldeg_c2c_2[0][6], EstVol_alldeg_c2c_2[0][7]]

plt.figure(figsize=(7,3))
plt.subplot(121)
for i in range(0,8):
    plt.bar(x_c2c_0deg_allcages[i],volumes_0deg_allcages_c2c[i], width=0.5, label='Cage '+str(i+1), color = cols[i],  edgecolor = 'k' )
plt.ylim(0,35000)
plt.xlim(0,5)
plt.xticks(x_c2c_0deg_allcages, ['1', '2', '3', '4', '5', '6', '7', '8'])
# plt.legend(frameon=False, ncol=2)
plt.xlabel('Cage Number')
plt.ylabel('Volume [$m^3$]')
plt.title('Case2, 0\u00B0, New inputfile')

plt.subplot(122)
for i in range(0,8):
    plt.bar(x_c2c_0deg_allcages[i],volumes_0deg_allcages_c2c_2[i], width=0.5, label='Cage '+str(i+1), color = cols[i],  edgecolor = 'k' )
plt.ylim(0,35000)
plt.xlim(0,5)
plt.xticks(x_c2c_0deg_allcages, ['1', '2', '3', '4', '5', '6', '7', '8'])
# plt.legend(frameon=False, ncol=2)
plt.xlabel('Cage Number')
plt.ylabel('Volume [$m^3$]')
plt.title('Case2, 0\u00B0, Old inputfile')
plt.tight_layout()
plt.savefig('Difference between inputfiles for the volume of cage.png', dpi=600)