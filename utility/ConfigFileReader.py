import configparser
import os


class ConfigFileReader:

    def get_value_of(self, filepath, section, key):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(filepath))
        value = config[section][key]
        return value

    def set_value_of(self, filepath,section, key, value):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(filepath))
        config.set(section, key, value)
        configfile = open(os.path.abspath(filepath), 'w')
        config.write(configfile)
        configfile.close()