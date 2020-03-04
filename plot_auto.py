# Created by Hui Cheng
# Plot the real-time result when the simulation is going on.

import Fun_read as fr
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
# set up the style
matplotlib.rc('font',family='Times New Roman')
font = {'family': 'Times New Roman', 'style': 'normal','weight':'regular', 'size': 10}
plt.style.use('default')

plt.figure(figsize=(6.3, 3.6)) # generate a figure which the figure size in rinche
def animate(i):
    resu = fr.readresu("..\\sibaljotgatne.csv")  # the file name should be the same with your outputfile
    x = resu['Time']  # plot the parameters with time
    plt.cla()
    for i in range(8):
        if i<4:
            plt.plot(x,resu['NetStructure'+str(i)]['VolumeEst'],'-',label=['Cage'+str(i)])
        else:
            plt.plot(x,resu['NetStructure'+str(i)]['VolumeEst'],'--',label=['Cage'+str(i)])

    plt.legend(loc='lower right',frameon=False,fontsize=10)
    plt.ylabel('Fish cage volume  ($m^3$)' ,font)
    plt.xlabel('Time (s)' ,font)#     , fontsize=18)
    plt.xlim(0,600)
    plt.ylim(0,36000)
    plt.tight_layout()
    
ani = FuncAnimation(plt.gcf(), animate, interval=60000)  #ms
plt.tight_layout()
plt.show()