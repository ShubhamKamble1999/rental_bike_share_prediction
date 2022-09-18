import sys
import yaml
import os
from bike.exception import BikingException

def read_yaml_file(file_path:str)->dict:
    """
    Function to read yaml file
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise BikingException(e,sys) from e