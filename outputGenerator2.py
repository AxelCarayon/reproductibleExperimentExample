import matplotlib.pyplot as plt
from operator import add
import yaml

PARAMERTERS_FILE = "parameters.yaml"

maxValue = 0

def readValues(file) -> list[int] :
    values = [0 for _ in range(maxValue+1)]
    for line in open(file,'r').readlines() :
        values[int(line)] += 1
    return values

def loadParameters(file) -> None:
    global maxValue
    yaml_file = open(file, 'r')
    yaml_content = yaml.safe_load(yaml_file)
    maxValue = yaml_content.get('numberGenerator').get('maxValue')


def startExperiment(inputFiles,output_folder) -> None :
    cpt = 0
    labels = [i for i in range(maxValue+1)]
    values = [0 for _ in range(maxValue+1)]
    width = 0.35
    fig,ax = plt.subplots()
    for inputFile in inputFiles :
        value = readValues(inputFile)
        ax.bar(labels,value,width,bottom=values,label=f"input{cpt}") 
        values = list(map(add,values,value))
        cpt+=1
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    
    plt.legend(loc='center left',bbox_to_anchor=(1, 0.5))
    plt.savefig(f"{output_folder}/outputSumInputs.png")

loadParameters(PARAMERTERS_FILE)