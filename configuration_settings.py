import json


def configuration_settings():

    configuration_file = open('config.json')
    config_settings = json.load(configuration_file)

    return config_settings
