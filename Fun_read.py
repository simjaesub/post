# this is a function to read the output file based on Fhsim.


import numpy as np
import csv 
def readresu(fname):
    with open(fname) as f:
        creader = csv.reader(f,delimiter=";")
        objects = np.array(next(creader))[:-1]
        k_signals = np.array(next(creader))[:-1]
        data = np.loadtxt(fname,delimiter=";",skiprows=2,usecols=range(0,len(k_signals)))
    
    signals = np.array([])
    for i,element in enumerate(k_signals[1:]):
        signals = np.append(signals, (element[:-2]) )

    object_set=list(set(objects))
    dict_data = { }

    for obj in object_set:
        obj_index = [obj == element for element in objects]
        if not obj in dict_data: dict_data[obj]={}
        subsignals=signals[[obj == element for element in objects][1:]]
        subdata=data[:,[obj == element for element in objects]]
        for signal in subsignals:
            signal_index = [signal == element for element in subsignals]    
            dict_data[obj][signal] = subdata[:, signal_index]  

    dict_data["Time"] = data[:,0]
    return dict_data
