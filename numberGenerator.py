import random
import yaml

PARAMERTERS_FILE = "parameters.yaml"

maxValue = 0
seed = 0
valuesPerFiles = 0
numberOfFiles = 0

def loadParameters(file) -> None:
    global maxValue, seed, valuesPerFiles,numberOfFiles
    yaml_file = open(file, 'r')
    yaml_content = yaml.safe_load(yaml_file)
    maxValue = yaml_content.get('numberGenerator').get('maxValue')
    seed = yaml_content.get('numberGenerator').get('seed')
    valuesPerFiles = yaml_content.get('numberGenerator').get('valuesPerFiles')
    numberOfFiles = yaml_content.get('numberGenerator').get('numberOfFiles')

def generateNumbers(n) -> list[int]:
    global seed
    numbers = []
    random.seed(seed)
    for _ in range(n):
        numbers.append(random.randint(0, maxValue))
    seed+=1
    return numbers

def generateInputFiles(inputFolder) -> list[str]:
    inputFiles = []
    for i in range(numberOfFiles):
        numbers = generateNumbers(valuesPerFiles)
        inputFiles.append(f"{inputFolder}/input{i}.txt")
        file = open(f"{inputFolder}/input{i}.txt", "w")
        for number in numbers:
            file.write(str(number) + "\n")
        file.close()
    return inputFiles


loadParameters(PARAMERTERS_FILE)
