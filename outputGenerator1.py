from numpy.lib.npyio import load
import matplotlib.pyplot as plt
import numpy as np
import yaml
from numpy import loadtxt

PARAMERTERS_FILE = "parameters.yaml"

def startExperiment(inputFiles,output_folder):
    cpt = 0
    for inputFile in inputFiles:
        data = loadtxt(inputFile, delimiter="\n")
        data.sort()
        plt.hist(data,bins=np.arange(data.min(),data.max()+2,1))
        plt.savefig(f"{output_folder}/output{cpt}.png")
        plt.clf()
        cpt+=1
