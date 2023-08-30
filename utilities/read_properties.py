from jproperties import Properties
import os
import yaml
from yaml.loader import SafeLoader
import json


def read_properties(keys):
    config_filepath = os.path.normpath(os.getcwd() + os.sep).rstrip(
        "/utilities/") + "/data/config.properties"
    prop = Properties()
    with open(config_filepath, 'rb') as config_file:
        prop.load(config_file)
    return prop.properties[keys]

def read_json(filename):
    base_path =os.path.join(os.getcwd())
    json_path = f"{base_path}/data/{filename}.json"
    with open(json_path,'r') as file:
        data = json.load(file)
    return data    


def read_yaml(key):
    config_filepath = os.path.normpath(os.getcwd() + os.sep).rstrip(
        "/utilities/") + "/data/constants.yaml"
    # Open the file and load the file
    with open(config_filepath) as f:
        data = yaml.load(f, Loader=SafeLoader)

    return data[key]

def read_multiple_json_files():
    data = []
    path = "../data"
    for filename in os.listdir(path):
        if filename.endswith('.json'):
            file_path = os.path.join(path, filename)
            with open(file_path) as file:
                json_data = json.load(file)
                data.append(json_data)
    return data