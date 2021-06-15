import configparser
import os


class ConfigFileReader:

    def get_value_of(self, filepath, section, key):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(filepath))
        value = config[section][key]
        return value
