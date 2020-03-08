import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (6.5, 3.0)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = '10'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"

Vol = np.array([[17008.9, 17085.4, 16804.7, 16916.2, 17118.6, 17116.4, 17039.7, 17027.8, 17043.5, 17055.8],
                [18909.7, 18419.4, 16964.9, 16674.6, 16980.4, 17038.0, 16935.2, 16981.4, 17024.4, 17062.2],
                [23464.7, 20575.6, 17675.7, 16962.4, 17299.4, 17381.3, 17245.5, 16967.2, 17310.1, 17417.2],
                [31434.9, 22005.0, 18741.0, 17293.3, 17655.8, 17755.6, 17508.6, 17353.2, 17668.4, 17797.6]])
Drag = np.array([[72.1, 71.6, 74.4, 73.4, 71.8, 70.7, 71.7, 71.8, 72.0, 71.4],
                 [42.9, 51.5, 67.9, 73.5, 72.7, 70.9, 71.2, 71.8, 72.4, 71.8],
                 [26.6, 51.0, 66.2, 72.2, 71.8, 70.5, 71.8, 73.0, 70.6, 70.7],
                 [16.8, 51.3, 63.7, 71.6, 71.2, 69.9, 71.6, 71.2, 69.9, 69.3]])

deg = np.arange(0, 100, 10)
cols = ['firebrick', 'darkgreen', 'rebeccapurple', 'royalblue', 'lightcoral', 'mediumseagreen', 'mediumpurple',
        'deepskyblue']
stys = ['-', '-', '-', '-']
mark = ['s', '^', 'D', 'o', 's', '^', 'D', 'o']

xaxis = np.arange(0, 100, 10)
#### Cultivation volume
plt.figure()
plt.subplot(1, 2, 1)
for i in range(0, 4):
    plt.plot(deg, Vol[i], label='Cage' + str(i + 1), color=cols[i], marker=mark[i], linestyle=stys[i], mfc='none',
             markersize=4)
plt.legend(frameon=False)
plt.xlabel('Flow direction [\u00B0]\n(a)')
plt.ylabel('Volume [$m^3$]')
plt.xticks(xaxis)
plt.ylim(0, 35000)
plt.xlim(0, 90)

##### Drag force
plt.subplot(1, 2, 2)
for i in range(0, 4):
    plt.plot(deg, Drag[i], label='Cage' + str(i + 1), color=cols[i], marker=mark[i], linestyle=stys[i], mfc='none',
             markersize=4)
plt.legend(frameon=False)
plt.xlabel('Flow direction [\u00B0]\n(b)')
plt.ylabel('Force [kN]')
plt.ylim(0, 150)
plt.xticks(xaxis)
plt.xlim(0, 90)
plt.tight_layout(pad=0.03)
plt.savefig('drag_vol_1x4_intact_alldeg.png', dpi=600)
