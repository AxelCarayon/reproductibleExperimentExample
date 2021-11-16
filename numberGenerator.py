import io
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

def streamNumbers(n) -> io.BytesIO:
    global seed
    stream = io.BytesIO()
    random.seed(seed)
    for _ in range(n):
        stream.write((str(random.randint(0, maxValue)) + "\n").encode())
    seed+=1
    return stream

def readStream(stream):
    stream.seek(0)
    liste = []
    for line in stream.readlines():
        liste.append(int(line.strip()))
    return liste

def generateNumbers(n) -> list[int]:
    global seed
    numbers = []
    random.seed(seed)
    for _ in range(n):
        numbers.append(random.randint(0, maxValue))
    seed+=1
    return numbers


def generateInputFiles(inputFolder, storeInputPath = None, streamedData = None) -> list[str]:
    inputFiles = []
    if (storeInputPath) :
        pathFile = open(storeInputPath, 'w')
    for i in range(numberOfFiles):
        if (not streamedData):
            numbers = generateNumbers(valuesPerFiles)
        if (streamedData):
            stream = streamNumbers(valuesPerFiles)
            numbers = readStream(stream)
        inputFiles.append(f"{inputFolder}/input{i}.txt")
        if (storeInputPath) :
            pathFile.write(f"{inputFolder}/input{i}.txt\n")
        file = open(f"{inputFolder}/input{i}.txt", "w")
        for number in numbers:
            file.write(str(number) + "\n")
    return inputFiles


loadParameters(PARAMERTERS_FILE)
