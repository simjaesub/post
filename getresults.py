"""
Original from Karl Gunnar, modified by Hui cheng
"""
import numpy as np
import csv 

# >>>>>>>>>>>>>>>do not change>>>>>>>>>>>>>>>>>>>>>>
def readFhsim( fname ):
    with open(fname) as f:
        creader = csv.reader(f,delimiter=";")
        objects = np.array(next(creader))[:-1]
        _signals = np.array(next(creader))[:-1]
        data = np.loadtxt(fname,delimiter=";",skiprows=2,usecols=range(0,len(_signals)))
       
    signals = np.array([])
    for i,element in enumerate(_signals[1:]):
        signals = np.append(signals, (element[:-2]) )
    
    signal_set = list(set(signals))
    
    dict_data = { };
    
    for signal in signal_set:
        signal_index = [signal in element for element in signals]
        object_name = list(set(objects[1:][ signal_index ]))
        for i in range(len(object_name)):
            if not object_name[i] in dict_data: dict_data[object_name[i]]={}
            dict_data[object_name[i]][signal] = data[:,[False]+signal_index]  
    
    dict_data["Time"] = data[:,0]
    return dict_data
# >>>>>>>>>>>>>>>>>>>>>>do not change>>>>>>>>>>>>

resu=readFhsim("..\\resu32.csv");

import matplotlib.pyplot as plt
plt.figure()
x=resu['Time']
y1=resu['mooring3']['frameCableU0_0_ForceA'][:,0]

plt.plot(x,y1)
plt.show()


