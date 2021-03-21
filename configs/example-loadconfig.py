##### Imports #####
import yaml
import os

##### Define config file #####
configFile = os.path.join('.', 'configs', 'config.yaml')

##### Open file and load content #####
def loader(filepath):
    with open(filepath, 'r') as s:
        data = yaml.safe_load(s)
    return data

##### Define vars and values for later imports #####
if os.path.isfile(configFile):
    try:
        temp = loader(configFile)
        token = temp['Bot']['token']
    except ImportError:
        print('Loadconfig, import ERROR: Bot token')
    try:
        temp = loader(configFile)
        prefix = temp['Bot']['prefix']
    except ImportError:
        print('Loadconfig, import ERROR: Bot prefix')
    try:
        temp = loader(configFile)
        serverId = temp['Bot']['serverid']
    except ImportError:
        print('Loadconfig, import ERROR: Server ID')
    try:
        temp = loader(configFile)
        DB = temp['Db']['main']
    except ImportError:
        print('Loadconfig, import ERROR: DB')