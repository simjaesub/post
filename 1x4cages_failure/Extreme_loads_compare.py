import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (6.3, 3)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = 10
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"

U1 = [184.4,
      203.7,
      212.5,
      206.8,
      188.5,
      166.6,
      141.6,
      113.0,
      87.9,
      66.4]

U2 = [184.7,
      203.4,
      211.5,
      200.3,
      180.1,
      157.5,
      132.2,
      103.9,
      76.9,
      54.2]

V2 = [91.7,
      106.0,
      118.5,
      126.3,
      129.1,
      131.8,
      138.2,
      144.5,
      148.5,
      152.0]

V3 = [85.3,
      102.8,
      117.5,
      129.6,
      137.2,
      142.9,
      148.8,
      153.3,
      152.5,
      151.2]

V4 = [78.2,
      95.2,
      114.1,
      128.0,
      134.0,
      138.6,
      146.1,
      150.2,
      150.5,
      150.6]

x = np.arange(0, 100, 10)
cols = ['firebrick', 'darkgreen', 'rebeccapurple', 'royalblue', 'lightcoral', 'mediumseagreen', 'mediumpurple',
        'deepskyblue', 'lawngreen']
plt.figure()
plt.plot(x, U1, label='U1', Marker='o', linestyle='-', markersize=6, mfc='none', color=cols[0])
plt.plot(x, U2, label='U2', Marker='s', linestyle='-', markersize=6, mfc='none', color=cols[4])
plt.plot(x, V2, label='V2', Marker='o', linestyle='--', markersize=4, color=cols[1])
plt.plot(x, V3, label='V3', Marker='s', linestyle='--', markersize=4, color=cols[5])
plt.plot(x, V4, label='V4', Marker='^', linestyle='--', markersize=4, color=cols[8])
plt.xlim(0, 90)
plt.ylim(0, 250)
plt.legend(frameon=False, ncol=5, loc='lower center')
plt.xlabel('Flow direction [\u00B0]')
plt.ylabel('Tension [kN]')
plt.tight_layout()
plt.savefig('Extreme_load(MooringlineTs).png', dpi=600)
