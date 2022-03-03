import configparser
from os.path import *

config_path = join(dirname(__file__), '../config.ini')


def set_config(section, key, value):
    if exists(config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        config[section][key] = value
        with open(config_path, 'w') as configfile:
            config.write(configfile)
    else:
        return False


def get_config(section, key):
    if exists(config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        try:
            return config[section][key]
        except KeyError:
            return None
    else:
        return None
