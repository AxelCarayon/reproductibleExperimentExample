import os
import numberGenerator
import importlib
import yaml

PARAMERTERS_FILE = "parameters.yaml"

outputModule = None
input_folder = None
output_folder = None

def folderExists(folder) -> bool:
    return os.path.isdir(folder)

def folderIsEmpty(folder) -> bool:
    return len(os.listdir(folder)) == 0

def loadParameters(file) -> None:
    global outputModule, input_folder,output_folder
    yaml_file = open(file, 'r')
    yaml_content = yaml.safe_load(yaml_file)
    outputModule = yaml_content.get('main').get('outputModule')
    input_folder = yaml_content.get('main').get('input_folder')
    output_folder = yaml_content.get('main').get('output_folder')

if __name__ == '__main__':
    loadParameters(PARAMERTERS_FILE)
    print("Generating input files...")
    if not folderExists(input_folder):
        os.mkdir(input_folder)
    filesGenerated = numberGenerator.generateInputFiles(input_folder)

    print(f"Generating output with {outputModule}.py ...")

    module = importlib.import_module(outputModule)
    module.startExperiment(filesGenerated,output_folder)
    