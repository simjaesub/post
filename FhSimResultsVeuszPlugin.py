import csv
from veusz.plugins import *

class FhSimImporter(ImportPlugin):
    """An example plugin for reading a set of unformatted numbers
    from a file."""
 
    name = "FhSim Importer"
    author = "Karl Gunnar Aarsaether"
    description = "Reads a FhSim results file"
 
    def __init__(self):
        ImportPlugin.__init__(self)
 
    def doImport(self, params):
        """Actually import data
        params is a ImportPluginParams object.
        Return a list of ImportDataset1D, ImportDataset2D objects
        """
        data = {}
        creader = csv.reader( open(params.filename),delimiter=";",skipinitialspace=True)
        try:
            objects= creader.__next__();
            variables = creader.__next__();
        except StopIteration: 
            return []

        variables[0] ="T"
        MyReturnList= []

        for o in objects:
            data[o]={};
        for i in range(0,len(variables)-1):
            data[objects[i]][variables[i]] = [];
        for r in creader:
            for i in range(0,len(r)-1):
                try:
                    data[objects[i]][variables[i]].append(float(r[i])); 
                except:
                    data[objects[i]][variables[i]].append(float('NaN'));
        for o in data.keys():
            for k in data[o].keys():
                MyReturnList.append(ImportDataset1D(o+"."+k, data[o][k]) )
                
        return MyReturnList
 
importpluginregistry.append(FhSimImporter())