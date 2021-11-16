import os
import numberGenerator
import importlib
import yaml
import argparse
import io

PARAMERTERS_FILE = "parameters.yaml"
INPUT_FILE = "input.yaml"

inputModule = None
outputModule = None
input_folder = None
output_folder = None

def folderExists(folder) -> bool:
    return os.path.isdir(folder)

def folderIsEmpty(folder) -> bool:
    return len(os.listdir(folder)) == 0

def fileExists(file) -> bool:
    return os.path.isfile(file)

def loadParameters(file) -> None:
    global inputModule, outputModule, input_folder,output_folder
    yaml_file = open(file, 'r')
    yaml_content = yaml.safe_load(yaml_file)
    inputModule = yaml_content.get('main').get('inputModule')
    outputModule = yaml_content.get('main').get('outputModule')
    input_folder = yaml_content.get('main').get('input_folder')
    output_folder = yaml_content.get('main').get('output_folder')

def readInputFile(file) -> list[str]:
    f = open(file, 'r')
    return f.read().splitlines()

def streamAndReadInputFile(file) -> list[str]:
    return io.TextIOWrapper.read(open(file,'r')).splitlines()


if __name__ == '__main__':
    loadParameters(PARAMERTERS_FILE)
    parser = argparse.ArgumentParser("prototype")
    g = parser.add_mutually_exclusive_group()
    g.add_argument("-g", "--generate", action='store_true', help="Generate input files")
    g.add_argument("-gs","--generateAndStore", help="Generate input files and store them in the specified folder")
    g.add_argument("-i", "--input", help="Read input files described in the inputs.txt file")
    parser.add_argument("-s","--stream", action='store_true', help="If data is generated, the data will be streamed")

    args = parser.parse_args()
    inputFiles = None
    if args.generate:
        module = importlib.import_module(inputModule)
        print(f"Generating input files with {inputModule}.py ...")
        if not folderExists(input_folder):
            os.mkdir(input_folder)
        inputFiles = numberGenerator.generateInputFiles(input_folder,streamedData=args.stream)

    elif args.generateAndStore:
        print(f"Generating input files with {inputModule}.py and generating path in {args.generateAndStore} ...")
        module = importlib.import_module(inputModule)
        if (not fileExists(args.generateAndStore)):
            raise Exception("The specified folder does not exist")
        inputFiles = numberGenerator.generateInputFiles(input_folder, args.generateAndStore, args.stream)
    elif args.input:
        print(f"Using inputs described in the {INPUT_FILE}.yaml file ...")
        inputFiles = readInputFile(args.input)
    else:
        parser.error("You must specify an input method")
    print(f"Generating output with {outputModule}.py ...")

    module = importlib.import_module(outputModule)
    module.startExperiment(inputFiles,output_folder)
    