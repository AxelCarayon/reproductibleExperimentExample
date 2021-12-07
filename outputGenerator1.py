import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt

def startExperiment(inputFiles,output_folder):
    cpt = 0
    labels = []
    sums = []
    for inputFile in inputFiles:
        data = loadtxt(inputFile, delimiter="\n")
        plt.hist(data,bins=np.arange(data.min(),data.max()+2,1))
        plt.savefig(f"{output_folder}/output{cpt}.png")
        plt.clf()
        cpt+=1
